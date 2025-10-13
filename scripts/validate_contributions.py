#!/usr/bin/env python3
"""
Profile and Contribution Validation Script

Validates that contributions meet the project standards and guidelines.
"""

import os
import re
import yaml
from pathlib import Path
from typing import List, Dict, Tuple


class ContributionValidator:
    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)
        self.errors = []
        self.warnings = []

    def validate_profile(self, profile_path: Path) -> bool:
        """Validate a contributor profile"""
        is_valid = True

        try:
            with open(profile_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            self.errors.append(f"Could not read profile {profile_path}: {e}")
            return False

        # Check required sections
        required_sections = [
            "## 👋 Quick Intro",
            "## 🎯 Interactive Skills Radar",
            "## 🏆 Hacktoberfest 2025 Goals",
            "## 🚀 My Contributions",
        ]

        for section in required_sections:
            if section not in content:
                self.errors.append(
                    f"Profile {profile_path.name} missing required section: {section}"
                )
                is_valid = False

        # Check for basic information
        if not re.search(r"Name.*:", content, re.IGNORECASE):
            self.warnings.append(f"Profile {profile_path.name} should include name")

        if not re.search(r"Location.*:", content, re.IGNORECASE):
            self.warnings.append(f"Profile {profile_path.name} should include location")

        # Check for contact information
        has_contact = any(
            contact in content.lower()
            for contact in ["github.com", "linkedin", "twitter", "@"]
        )
        if not has_contact:
            self.warnings.append(
                f"Profile {profile_path.name} should include contact information"
            )

        # Check file naming
        expected_name = profile_path.stem + ".md"
        if profile_path.name != expected_name:
            self.errors.append(
                f"Profile file should be named {expected_name}, got {profile_path.name}"
            )
            is_valid = False

        return is_valid

    def validate_challenge_solution(self, solution_path: Path) -> bool:
        """Validate a challenge solution"""
        is_valid = True

        # Check file extension
        allowed_extensions = [
            ".py",
            ".js",
            ".java",
            ".cpp",
            ".c",
            ".go",
            ".rs",
            ".php",
            ".rb",
            ".sh",
            ".pl",
        ]
        if solution_path.suffix not in allowed_extensions:
            self.warnings.append(
                f"Solution {solution_path.name} uses uncommon language ({solution_path.suffix})"
            )

        # Check file naming convention (username_description.ext)
        parts = solution_path.stem.split("_", 1)
        if len(parts) < 2:
            self.errors.append(
                f"Solution {solution_path.name} should follow naming convention: username_description.ext"
            )
            is_valid = False

        # Check if solution actually contains code
        try:
            with open(solution_path, "r", encoding="utf-8") as f:
                content = f.read()

            if len(content.strip()) < 10:
                self.errors.append(
                    f"Solution {solution_path.name} appears to be too short"
                )
                is_valid = False

            # Language-specific checks
            if solution_path.suffix == ".py":
                if not self._validate_python_code(content):
                    is_valid = False
            elif solution_path.suffix == ".js":
                if not self._validate_javascript_code(content):
                    is_valid = False

        except Exception as e:
            self.errors.append(f"Could not read solution {solution_path}: {e}")
            is_valid = False

        return is_valid

    def _validate_python_code(self, content: str) -> bool:
        """Basic Python code validation"""
        # Check for basic syntax issues
        if "print(" in content and not content.strip().startswith("#"):
            return True  # Has some Python code
        if "def " in content or "class " in content:
            return True  # Has functions or classes
        if "import " in content:
            return True  # Has imports

        self.warnings.append(
            "Python solution should contain actual code (functions, classes, or print statements)"
        )
        return False

    def _validate_javascript_code(self, content: str) -> bool:
        """Basic JavaScript code validation"""
        if (
            "console.log(" in content
            or "function " in content
            or "const " in content
            or "let " in content
        ):
            return True

        self.warnings.append("JavaScript solution should contain actual code")
        return False

    def validate_project(self, project_path: Path) -> bool:
        """Validate a project submission"""
        is_valid = True

        # Check if it's a directory
        if not project_path.is_dir():
            self.errors.append(f"Project {project_path.name} should be a directory")
            return False

        # Check for README
        readme_files = ["README.md", "readme.md", "Readme.md"]
        has_readme = any((project_path / readme).exists() for readme in readme_files)
        if not has_readme:
            self.errors.append(
                f"Project {project_path.name} should include a README.md file"
            )
            is_valid = False

        # Check for code files
        code_files = []
        for ext in [
            ".py",
            ".js",
            ".java",
            ".cpp",
            ".c",
            ".go",
            ".rs",
            ".php",
            ".rb",
            ".html",
            ".css",
        ]:
            code_files.extend(list(project_path.rglob(f"*{ext}")))

        if len(code_files) == 0:
            self.errors.append(f"Project {project_path.name} should contain code files")
            is_valid = False

        # Check project naming convention
        parts = project_path.name.split("_", 1)
        if len(parts) < 2:
            self.errors.append(
                f"Project directory should follow naming convention: username_projectname"
            )
            is_valid = False

        return is_valid

    def validate_script(self, script_path: Path) -> bool:
        """Validate a utility script"""
        is_valid = True

        # Check file naming convention
        parts = script_path.stem.split("_", 1)
        if len(parts) < 2:
            self.errors.append(
                f"Script {script_path.name} should follow naming convention: username_description.ext"
            )
            is_valid = False

        # Check if file is executable (for shell scripts)
        if script_path.suffix in [".sh", ".py", ".pl"]:
            if not os.access(script_path, os.X_OK) and script_path.suffix != ".py":
                self.warnings.append(f"Script {script_path.name} should be executable")

        # Check for shebang in script files
        try:
            with open(script_path, "r", encoding="utf-8") as f:
                first_line = f.readline().strip()
                if script_path.suffix in [
                    ".sh",
                    ".py",
                    ".pl",
                ] and not first_line.startswith("#!"):
                    self.warnings.append(
                        f"Script {script_path.name} should include a shebang line"
                    )
        except Exception as e:
            self.errors.append(f"Could not read script {script_path}: {e}")
            is_valid = False

        return is_valid

    def validate_all_contributions(self) -> Tuple[bool, List[str], List[str]]:
        """Validate all contributions in the repository"""
        self.errors = []
        self.warnings = []

        # Validate profiles
        profiles_dir = self.repo_path / "profiles"
        if profiles_dir.exists():
            for profile_file in profiles_dir.iterdir():
                if profile_file.suffix == ".md":
                    self.validate_profile(profile_file)

        # Validate challenge solutions
        challenges_dir = self.repo_path / "challenges"
        if challenges_dir.exists():
            for solution_file in challenges_dir.rglob("solutions/*"):
                if solution_file.is_file():
                    self.validate_challenge_solution(solution_file)

        # Validate projects
        projects_dir = self.repo_path / "projects"
        if projects_dir.exists():
            for category_dir in projects_dir.iterdir():
                if category_dir.is_dir() and category_dir.name in [
                    "web",
                    "cli",
                    "games",
                    "utilities",
                ]:
                    for project_dir in category_dir.iterdir():
                        if project_dir.is_dir():
                            self.validate_project(project_dir)

        # Validate scripts
        scripts_dir = self.repo_path / "scripts"
        if scripts_dir.exists():
            for script_file in scripts_dir.iterdir():
                if script_file.is_file() and not script_file.name.startswith("."):
                    self.validate_script(script_file)

        is_valid = len(self.errors) == 0
        return is_valid, self.errors, self.warnings


def main():
    validator = ContributionValidator("/home/gilbert/Desktop/hacktoberfest")
    is_valid, errors, warnings = validator.validate_all_contributions()

    print("🔍 Contribution Validation Results")
    print("=" * 50)

    if is_valid:
        print("✅ All contributions are valid!")
    else:
        print("❌ Found validation errors:")
        for error in errors:
            print(f"  - {error}")

    if warnings:
        print("\n⚠️  Warnings:")
        for warning in warnings:
            print(f"  - {warning}")

    print(f"\n📊 Summary: {len(errors)} errors, {len(warnings)} warnings")

    return is_valid


if __name__ == "__main__":
    main()

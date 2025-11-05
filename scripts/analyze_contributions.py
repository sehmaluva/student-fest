#!/usr/bin/env python3
"""
Contribution Analysis and Statistics Generator

Analyzes all contributions in the repository and generates comprehensive statistics
for the interactive Student Fest project.
"""

import os
import json
import yaml
from datetime import datetime
from pathlib import Path
from collections import defaultdict, Counter


class ContributionAnalyzer:
    def __init__(self, repo_path):
        self.repo_path = Path(repo_path)
        self.stats = {
            "total_contributors": 0,
            "total_profiles": 0,
            "total_challenges": 0,
            "total_projects": 0,
            "total_scripts": 0,
            "contributors_by_type": {},
            "language_distribution": {},
            "difficulty_distribution": {},
            "contribution_timeline": {},
            "top_contributors": [],
            "recent_activity": [],
        }

    def analyze_profiles(self):
        """Analyze contributor profiles"""
        profiles_dir = self.repo_path / "profiles"
        if not profiles_dir.exists():
            return

        profiles = []
        for profile_file in profiles_dir.iterdir():
            if profile_file.suffix == ".md":
                try:
                    with open(profile_file, "r", encoding="utf-8") as f:
                        content = f.read()

                    # Extract basic info from profile
                    username = profile_file.stem
                    profile_data = {
                        "username": username,
                        "file_path": str(profile_file.relative_to(self.repo_path)),
                        "skills": [],
                        "contributions": [],
                    }

                    # Parse profile content (basic parsing)
                    lines = content.split("\n")
                    for line in lines:
                        if "Programming Languages:" in line or "Skills:" in line:
                            # Extract skills (this is a simple parser)
                            pass
                        elif "- **" in line and "**" in line:
                            profile_data["contributions"].append(line.strip())

                    profiles.append(profile_data)

                except Exception as e:
                    print(f"Error parsing profile {profile_file}: {e}")

        self.stats["total_profiles"] = len(profiles)
        return profiles

    def analyze_challenges(self):
        """Analyze coding challenges and solutions"""
        challenges_dir = self.repo_path / "challenges"
        if not challenges_dir.exists():
            return

        challenge_stats = {
            "by_difficulty": defaultdict(int),
            "by_language": defaultdict(int),
            "total_solutions": 0,
            "challenges": [],
        }

        for difficulty in ["beginner", "intermediate", "advanced"]:
            difficulty_dir = challenges_dir / difficulty
            if difficulty_dir.exists():
                for challenge_dir in difficulty_dir.iterdir():
                    if challenge_dir.is_dir():
                        challenge_info = {
                            "name": challenge_dir.name,
                            "difficulty": difficulty,
                            "solutions": [],
                        }

                        solutions_dir = challenge_dir / "solutions"
                        if solutions_dir.exists():
                            for solution_file in solutions_dir.iterdir():
                                if solution_file.is_file():
                                    # Extract language from file extension
                                    language = (
                                        solution_file.suffix[1:]
                                        if solution_file.suffix
                                        else "unknown"
                                    )
                                    username = solution_file.name.split("_")[0]

                                    solution_info = {
                                        "username": username,
                                        "language": language,
                                        "file_path": str(
                                            solution_file.relative_to(self.repo_path)
                                        ),
                                    }

                                    challenge_info["solutions"].append(solution_info)
                                    challenge_stats["by_language"][language] += 1
                                    challenge_stats["total_solutions"] += 1

                        if challenge_info["solutions"]:
                            challenge_stats["challenges"].append(challenge_info)
                            challenge_stats["by_difficulty"][difficulty] += 1

        self.stats["total_challenges"] = challenge_stats["total_solutions"]
        self.stats["difficulty_distribution"] = dict(challenge_stats["by_difficulty"])
        self.stats["language_distribution"].update(challenge_stats["by_language"])
        return challenge_stats

    def analyze_projects(self):
        """Analyze real-world projects"""
        projects_dir = self.repo_path / "projects"
        if not projects_dir.exists():
            return

        project_stats = {
            "by_category": defaultdict(int),
            "by_language": defaultdict(int),
            "total_projects": 0,
            "projects": [],
        }

        for category in ["web", "cli", "games", "utilities"]:
            category_dir = projects_dir / category
            if category_dir.exists():
                for project_dir in category_dir.iterdir():
                    if project_dir.is_dir():
                        # Analyze project files
                        project_files = list(project_dir.rglob("*"))
                        languages = set()

                        for file_path in project_files:
                            if file_path.is_file():
                                ext = file_path.suffix[1:]
                                if ext in [
                                    "py",
                                    "js",
                                    "java",
                                    "cpp",
                                    "c",
                                    "go",
                                    "rs",
                                    "php",
                                    "rb",
                                ]:
                                    languages.add(ext)

                        username = project_dir.name.split("_")[0]

                        project_info = {
                            "name": project_dir.name,
                            "username": username,
                            "category": category,
                            "languages": list(languages),
                            "file_count": len(
                                [f for f in project_files if f.is_file()]
                            ),
                            "path": str(project_dir.relative_to(self.repo_path)),
                        }

                        project_stats["projects"].append(project_info)
                        project_stats["by_category"][category] += 1
                        project_stats["total_projects"] += 1

                        for lang in languages:
                            project_stats["by_language"][lang] += 1

        self.stats["total_projects"] = project_stats["total_projects"]
        self.stats["language_distribution"].update(project_stats["by_language"])
        return project_stats

    def analyze_scripts(self):
        """Analyze utility scripts"""
        scripts_dir = self.repo_path / "scripts"
        if not scripts_dir.exists():
            return

        script_stats = {
            "by_language": defaultdict(int),
            "total_scripts": 0,
            "scripts": [],
        }

        for script_file in scripts_dir.iterdir():
            if script_file.is_file() and not script_file.name.startswith("."):
                language = script_file.suffix[1:] if script_file.suffix else "unknown"
                username = script_file.name.split("_")[0]

                script_info = {
                    "name": script_file.name,
                    "username": username,
                    "language": language,
                    "path": str(script_file.relative_to(self.repo_path)),
                }

                script_stats["scripts"].append(script_info)
                script_stats["by_language"][language] += 1
                script_stats["total_scripts"] += 1

        self.stats["total_scripts"] = script_stats["total_scripts"]
        self.stats["language_distribution"].update(script_stats["by_language"])
        return script_stats

    def identify_contributors(self):
        """Identify all unique contributors"""
        contributors = set()

        # From profiles
        profiles_dir = self.repo_path / "profiles"
        if profiles_dir.exists():
            contributors.update(
                [f.stem for f in profiles_dir.iterdir() if f.suffix == ".md"]
            )

        # From challenges
        challenges_dir = self.repo_path / "challenges"
        if challenges_dir.exists():
            for solution_file in challenges_dir.rglob("solutions/*"):
                if solution_file.is_file():
                    username = solution_file.name.split("_")[0]
                    contributors.add(username)

        # From project
        projects_dir = self.repo_path / "projects"
        if projects_dir.exists():
            for project_dir in projects_dir.rglob("*"):
                if project_dir.is_dir() and not any(
                    parent.name in ["web", "cli", "games", "utilities"]
                    for parent in project_dir.parents
                ):
                    username = project_dir.name.split("_")[0]
                    contributors.add(username)

        # From scripts
        scripts_dir = self.repo_path / "scripts"
        if scripts_dir.exists():
            for script_file in scripts_dir.iterdir():
                if script_file.is_file():
                    username = script_file.name.split("_")[0]
                    contributors.add(username)

        self.stats["total_contributors"] = len(contributors)
        return list(contributors)

    def generate_contribution_summary(self):
        """Generate a comprehensive contribution summary"""
        contributors = self.identify_contributors()

        # Analyze all contribution types
        profiles = self.analyze_profiles()
        challenges = self.analyze_challenges()
        projects = self.analyze_projects()
        scripts = self.analyze_scripts()

        # Calculate contributor statistics
        contributor_stats = defaultdict(
            lambda: {
                "profiles": 0,
                "challenges": 0,
                "projects": 0,
                "scripts": 0,
                "total_contributions": 0,
            }
        )

        # Count contributions by type
        for profile in profiles or []:
            contributor_stats[profile["username"]]["profiles"] += 1
            contributor_stats[profile["username"]]["total_contributions"] += 1

        if challenges and "challenges" in challenges:
            for challenge in challenges["challenges"]:
                for solution in challenge["solutions"]:
                    contributor_stats[solution["username"]]["challenges"] += 1
                    contributor_stats[solution["username"]]["total_contributions"] += 1

        if projects and "projects" in projects:
            for project in projects["projects"]:
                contributor_stats[project["username"]]["projects"] += 1
                contributor_stats[project["username"]]["total_contributions"] += 1

        if scripts and "scripts" in scripts:
            for script in scripts["scripts"]:
                contributor_stats[script["username"]]["scripts"] += 1
                contributor_stats[script["username"]]["total_contributions"] += 1

        # Sort top contributors
        self.stats["top_contributors"] = sorted(
            [{"username": user, **stats} for user, stats in contributor_stats.items()],
            key=lambda x: x["total_contributions"],
            reverse=True,
        )[
            :10
        ]  # Top 10

        # Save detailed statistics
        output_path = self.repo_path / "stats.json"
        with open(output_path, "w") as f:
            json.dump(self.stats, f, indent=2, default=str)

        return self.stats


def main():
    analyzer = ContributionAnalyzer("/home/gilbert/Desktop/student-fest")
    stats = analyzer.generate_contribution_summary()

    print("📊 Contribution Analysis Complete!")
    print(f"Total Contributors: {stats['total_contributors']}")
    print(f"Total Profiles: {stats['total_profiles']}")
    print(f"Total Challenges Solved: {stats['total_challenges']}")
    print(f"Total Projects: {stats['total_projects']}")
    print(f"Total Scripts: {stats['total_scripts']}")

    if stats["top_contributors"]:
        print("\n🏆 Top Contributors:")
        for i, contributor in enumerate(stats["top_contributors"][:5], 1):
            print(
                f"{i}. {contributor['username']} - {contributor['total_contributions']} contributions"
            )


if __name__ == "__main__":
    main()

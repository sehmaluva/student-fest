#!/usr/bin/env python3
"""
Badge Generation System for Hacktoberfest Interactive Project

This script generates dynamic achievement badges for contributors based on:
- Number of contributions
- Types of contributions (profiles, challenges, projects, scripts)
- Difficulty levels tackled
- Quality of contributions
- Community engagement
"""

import os
import json
import yaml
from datetime import datetime
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO


class BadgeGenerator:
    def __init__(self, repo_path):
        self.repo_path = Path(repo_path)
        self.badges_dir = self.repo_path / "badges"
        self.assets_dir = self.repo_path / "assets"
        self.badges_dir.mkdir(exist_ok=True)

        # Badge configurations
        self.badge_configs = {
            "first-contribution": {
                "name": "First Steps",
                "description": "Made your first contribution",
                "color": "#4CAF50",
                "icon": "🌱",
            },
            "profile-creator": {
                "name": "Profile Builder",
                "description": "Created an interactive profile",
                "color": "#2196F3",
                "icon": "👤",
            },
            "challenge-solver": {
                "name": "Problem Solver",
                "description": "Completed coding challenges",
                "color": "#FF9800",
                "icon": "🧩",
            },
            "project-builder": {
                "name": "Project Creator",
                "description": "Built real-world applications",
                "color": "#9C27B0",
                "icon": "🚀",
            },
            "script-writer": {
                "name": "Script Master",
                "description": "Created utility scripts",
                "color": "#607D8B",
                "icon": "📜",
            },
            "mentor": {
                "name": "Community Mentor",
                "description": "Helped other contributors",
                "color": "#E91E63",
                "icon": "🤝",
            },
            "hacktoberfest-hero": {
                "name": "Hacktoberfest Hero",
                "description": "Outstanding contributions",
                "color": "#FF5722",
                "icon": "🏆",
            },
        }

    def analyze_contributions(self, username):
        """Analyze a user's contributions to determine earned badges"""
        badges_earned = []

        # Check for profile
        profile_path = self.repo_path / "profiles" / f"{username}.md"
        if profile_path.exists():
            badges_earned.append("profile-creator")

        # Check challenges solved
        challenges_solved = 0
        for difficulty in ["beginner", "intermediate", "advanced"]:
            challenge_dir = self.repo_path / "challenges" / difficulty
            if challenge_dir.exists():
                for challenge_dir in challenge_dir.iterdir():
                    if challenge_dir.is_dir():
                        solutions_dir = challenge_dir / "solutions"
                        if solutions_dir.exists():
                            for solution_file in solutions_dir.iterdir():
                                if solution_file.name.startswith(username):
                                    challenges_solved += 1

        if challenges_solved > 0:
            badges_earned.append("challenge-solver")
            if challenges_solved >= 5:
                badges_earned.append("hacktoberfest-hero")

        # Check projects
        projects_built = 0
        for category in ["web", "cli", "games", "utilities"]:
            project_dir = self.repo_path / "projects" / category
            if project_dir.exists():
                for project in project_dir.iterdir():
                    if project.is_dir() and project.name.startswith(username):
                        projects_built += 1

        if projects_built > 0:
            badges_earned.append("project-builder")

        # Check scripts
        scripts_created = 0
        scripts_dir = self.repo_path / "scripts"
        if scripts_dir.exists():
            for script_file in scripts_dir.iterdir():
                if script_file.name.startswith(username):
                    scripts_created += 1

        if scripts_created > 0:
            badges_earned.append("script-writer")

        # Always give first contribution badge to active contributors
        if len(badges_earned) > 0:
            badges_earned.insert(0, "first-contribution")

        return list(set(badges_earned))  # Remove duplicates

    def generate_badge_image(self, badge_type, username):
        """Generate a PNG badge image"""
        config = self.badge_configs[badge_type]

        # Create badge image (300x100)
        img = Image.new("RGBA", (300, 100), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)

        # Draw rounded rectangle background
        draw.rounded_rectangle([10, 10, 290, 90], radius=15, fill=config["color"])

        # Add icon (using text for now, could be replaced with actual icons)
        try:
            # Try to use a system font
            font_large = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 36)
            font_small = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 16)
        except:
            # Fallback to default font
            font_large = ImageFont.load_default()
            font_small = ImageFont.load_default()

        # Draw icon
        draw.text((25, 25), config["icon"], fill="white", font=font_large)

        # Draw badge name
        draw.text((80, 20), config["name"], fill="white", font=font_small)

        # Draw description
        draw.text((80, 45), config["description"], fill="white", font=font_small)

        # Draw username
        draw.text((80, 65), f"@{username}", fill="white", font=font_small)

        return img

    def generate_user_badges(self, username):
        """Generate all badges for a specific user"""
        earned_badges = self.analyze_contributions(username)

        user_badge_dir = self.badges_dir / username
        user_badge_dir.mkdir(exist_ok=True)

        generated_badges = []

        for badge_type in earned_badges:
            badge_image = self.generate_badge_image(badge_type, username)
            badge_filename = f"{badge_type}.png"
            badge_path = user_badge_dir / badge_filename

            badge_image.save(badge_path)
            generated_badges.append(
                {
                    "type": badge_type,
                    "name": self.badge_configs[badge_type]["name"],
                    "description": self.badge_configs[badge_type]["description"],
                    "image_path": str(badge_path.relative_to(self.repo_path)),
                    "earned_date": datetime.now().isoformat(),
                }
            )

        # Save badge metadata
        metadata_path = user_badge_dir / "metadata.json"
        with open(metadata_path, "w") as f:
            json.dump(
                {
                    "username": username,
                    "badges": generated_badges,
                    "total_badges": len(generated_badges),
                    "generated_at": datetime.now().isoformat(),
                },
                f,
                indent=2,
            )

        return generated_badges

    def generate_all_badges(self):
        """Generate badges for all contributors"""
        contributors = []

        # Get all profile files
        profiles_dir = self.repo_path / "profiles"
        if profiles_dir.exists():
            for profile_file in profiles_dir.iterdir():
                if profile_file.suffix == ".md":
                    username = profile_file.stem
                    contributors.append(username)

        # Also check for contributors who have other contributions but no profile
        for root_dir in ["challenges", "projects", "scripts"]:
            root_path = self.repo_path / root_dir
            if root_path.exists():
                for item in root_path.rglob("*"):
                    if item.is_file() and not item.name.startswith("."):
                        # Extract username from filename (assuming format: username_description.ext)
                        username = item.name.split("_")[0]
                        if username not in contributors:
                            contributors.append(username)

        all_badges = {}
        for username in contributors:
            try:
                user_badges = self.generate_user_badges(username)
                all_badges[username] = user_badges
                print(f"Generated {len(user_badges)} badges for {username}")
            except Exception as e:
                print(f"Error generating badges for {username}: {e}")

        # Save global badge statistics
        stats_path = self.badges_dir / "stats.json"
        with open(stats_path, "w") as f:
            json.dump(
                {
                    "total_contributors": len(contributors),
                    "contributors": list(all_badges.keys()),
                    "badge_distribution": {
                        badge_type: sum(
                            1
                            for user_badges in all_badges.values()
                            for badge in user_badges
                            if badge["type"] == badge_type
                        )
                        for badge_type in self.badge_configs.keys()
                    },
                    "generated_at": datetime.now().isoformat(),
                },
                f,
                indent=2,
            )

        return all_badges


def main():
    import sys

    if len(sys.argv) > 1:
        username = sys.argv[1]
        generator = BadgeGenerator("/home/gilbert/Desktop/hacktoberfest")
        badges = generator.generate_user_badges(username)
        print(f"Generated {len(badges)} badges for {username}")
    else:
        generator = BadgeGenerator("/home/gilbert/Desktop/hacktoberfest")
        all_badges = generator.generate_all_badges()
        print(f"Generated badges for {len(all_badges)} contributors")


if __name__ == "__main__":
    main()

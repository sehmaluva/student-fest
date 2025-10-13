#!/usr/bin/env python3
"""
Hacktoberfest Interactive Contributor Badge Generator
A simple Python script to generate ASCII art badges for contributors

Created by: sehmaluva
Date: October 13, 2025
Purpose: Example script for the new interactive Hacktoberfest experience
"""

import datetime
from typing import List, Dict


class BadgeGenerator:
    """Generate ASCII art badges for Hacktoberfest contributors"""

    THEMES = {
        "classic": {"border": "=", "fill": " ", "accent": "*"},
        "modern": {"border": "─", "fill": " ", "accent": "●"},
        "retro": {"border": "#", "fill": ".", "accent": "@"},
    }

    def __init__(self, theme: str = "classic"):
        """Initialize badge generator with specified theme"""
        self.theme = self.THEMES.get(theme, self.THEMES["classic"])
        self.width = 60

    def create_border(self, text: str = "") -> str:
        """Create a decorative border line"""
        if text:
            padding = (self.width - len(text) - 2) // 2
            return f"{self.theme['border'] * padding} {text} {self.theme['border'] * padding}"
        return self.theme["border"] * self.width

    def create_text_line(self, text: str, center: bool = True) -> str:
        """Create a formatted text line"""
        if center:
            padding = (self.width - len(text) - 2) // 2
            return f"{self.theme['border']}{' ' * padding}{text}{' ' * padding}{self.theme['border']}"
        else:
            spaces_needed = self.width - len(text) - 2
            return f"{self.theme['border']} {text}{' ' * spaces_needed}{self.theme['border']}"

    def generate_badge(self, contributor_data: Dict[str, any]) -> str:
        """Generate a complete ASCII badge"""
        lines = []

        # Header
        lines.append(self.create_border())
        lines.append(self.create_border("🎃 HACKTOBERFEST 2025 CONTRIBUTOR 🎃"))
        lines.append(self.create_border())
        lines.append(self.create_text_line(""))

        # Contributor info
        lines.append(self.create_text_line(f"Name: {contributor_data['name']}"))
        lines.append(self.create_text_line(f"GitHub: @{contributor_data['github']}"))
        lines.append(self.create_text_line(""))

        # Achievements
        if contributor_data.get("achievements"):
            lines.append(self.create_text_line("🏆 ACHIEVEMENTS 🏆"))
            lines.append(self.create_text_line(""))
            for achievement in contributor_data["achievements"]:
                lines.append(
                    self.create_text_line(
                        f"{self.theme['accent']} {achievement}", False
                    )
                )
            lines.append(self.create_text_line(""))

        # Stats
        lines.append(self.create_text_line("📊 CONTRIBUTIONS 📊"))
        lines.append(self.create_text_line(""))
        lines.append(
            self.create_text_line(f"Pull Requests: {contributor_data.get('prs', 0)}")
        )
        lines.append(
            self.create_text_line(
                f"Challenges Solved: {contributor_data.get('challenges', 0)}"
            )
        )
        lines.append(
            self.create_text_line(
                f"Projects Built: {contributor_data.get('projects', 0)}"
            )
        )
        lines.append(self.create_text_line(""))

        # Footer
        lines.append(
            self.create_text_line(
                f"Generated: {datetime.datetime.now().strftime('%B %d, %Y')}"
            )
        )
        lines.append(self.create_text_line(""))
        lines.append(self.create_border("Keep Contributing! 🚀"))
        lines.append(self.create_border())

        return "\n".join(lines)


def get_user_input() -> Dict[str, any]:
    """Get contributor information from user input"""
    print("🎃 Welcome to the Hacktoberfest Badge Generator! 🎃\n")

    data = {}
    data["name"] = input("Enter your name: ").strip()
    data["github"] = input("Enter your GitHub username: ").strip()

    # Get achievements
    print("\n🏆 Select your achievements (press Enter when done):")
    achievements = [
        "First Time Contributor",
        "Challenge Solver",
        "Project Builder",
        "Code Reviewer",
        "Documentation Hero",
        "Bug Hunter",
        "Community Helper",
        "Multi-Language Contributor",
    ]

    selected_achievements = []
    for i, achievement in enumerate(achievements, 1):
        choice = input(f"{i}. {achievement} (y/n): ").lower()
        if choice in ["y", "yes"]:
            selected_achievements.append(achievement)

    data["achievements"] = selected_achievements

    # Get stats
    print("\n📊 Enter your contribution stats:")
    try:
        data["prs"] = int(input("Number of Pull Requests: "))
        data["challenges"] = int(input("Challenges Completed: "))
        data["projects"] = int(input("Projects Built: "))
    except ValueError:
        data["prs"] = data["challenges"] = data["projects"] = 0

    return data


def main():
    """Main function to run the badge generator"""
    try:
        # Get user data
        contributor_data = get_user_input()

        # Choose theme
        print("\n🎨 Choose a badge theme:")
        print("1. Classic")
        print("2. Modern")
        print("3. Retro")

        theme_choice = input("Select theme (1-3): ").strip()
        theme_map = {"1": "classic", "2": "modern", "3": "retro"}
        theme = theme_map.get(theme_choice, "classic")

        # Generate badge
        generator = BadgeGenerator(theme)
        badge = generator.generate_badge(contributor_data)

        # Display result
        print("\n" + "=" * 60)
        print("🎉 YOUR HACKTOBERFEST BADGE IS READY! 🎉")
        print("=" * 60)
        print(badge)
        print("=" * 60)

        # Save option
        save = input("\nWould you like to save this badge to a file? (y/n): ")
        if save.lower() in ["y", "yes"]:
            filename = f"hacktoberfest_badge_{contributor_data['github']}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(badge)
            print(f"✅ Badge saved as {filename}")

        print("\n🎃 Thank you for being part of Hacktoberfest 2025! 🎃")
        print("🚀 Keep contributing and building awesome things! 🚀")

    except KeyboardInterrupt:
        print("\n\n👋 Thanks for trying the badge generator!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please try again or report this issue on GitHub.")


if __name__ == "__main__":
    main()

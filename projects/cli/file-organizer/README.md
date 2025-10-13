# 📂 Project: CLI File Organizer

**Difficulty**: Intermediate  
**Topics**: Command-Line Interface (CLI), File System Operations, Automation

## 📝 Project Description

Create a command-line tool that organizes files in a directory based on their file extension. For example, it could move all `.jpg` and `.png` files into an `Images` folder, and all `.pdf` files into a `Documents` folder.

## 🎯 Core Features

1.  **Command-Line Arguments**: The tool should accept a directory path as a command-line argument.
2.  **File Scanning**: Scan all files in the specified directory.
3.  **Categorization**: Group files by their extension (e.g., images, documents, videos, etc.).
4.  **Folder Creation**: Create new subdirectories for each file category if they don't already exist.
5.  **File Moving**: Move the files into their corresponding new folders.
6.  **Logging**: Print a summary of the actions taken (e.g., "Moved 15 files into 4 new folders.").

## ✨ Bonus Features (Optional)

*   **Custom Rules**: Allow users to define their own organization rules in a configuration file (e.g., a JSON or YAML file).
*   **Undo Functionality**: Add a feature to revert the organization process.
*   **Dry Run Mode**: A flag (`--dry-run`) that shows what changes would be made without actually moving any files.
*   **Recursive Organizing**: An option to organize files in subdirectories as well.

## 🛠️ Tech Stack Suggestions

This is a great project for practicing with system-level scripting languages:

*   **Python**: Using the `os` and `shutil` modules. Libraries like `argparse` or `click` are great for CLI arguments.
*   **Node.js**: Using the `fs` module. Libraries like `yargs` or `commander` for CLI arguments.
*   **Go**: A powerful choice for creating fast, compiled CLI tools.
*   **Bash/Shell Scripting**: For a classic, Unix-style utility.

## 🧪 How to Contribute

1.  Create a new directory for your solution under `projects/cli/file-organizer/solutions/`.
2.  Develop your CLI tool within that directory.
3.  Update this `README.md` with clear instructions on how to install and run your script.
4.  Open a pull request with your contribution.

This project is a practical way to learn about file system automation and building useful developer tools. Good luck! 🚀

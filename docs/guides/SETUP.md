# 🛠️ Setup Guide - Student Fest Interactive Experience

Welcome! This guide will help you set up your local development environment to contribute to our interactive Student Fest project.

## 📋 Prerequisites

Before you start, make sure you have:

### Required Tools
- **Git** (version 2.20+)
- **GitHub Account** with 2FA enabled
- **Text Editor** (VS Code, Sublime, Atom, etc.)
- **Web Browser** (Chrome, Firefox, Safari, Edge)

### Optional Tools (Depending on Your Contributions)
- **Node.js** (v16+) for JavaScript projects
- **Python** (3.8+) for Python scripts
- **Go** (1.18+) for Go applications
- **Docker** for containerized projects

## 🚀 Quick Start

### 1. Fork the Repository

1. Go to [https://github.com/sehmaluva/student-fest](https://github.com/sehmaluva/student-fest)
2. Click the "Fork" button in the top-right corner
3. Choose your GitHub account as the destination

### 2. Clone Your Fork

```bash
# Replace YOUR_USERNAME with your GitHub username
git clone https://github.com/YOUR_USERNAME/student-fest.git

# Navigate to the project directory
cd student-fest

# Add upstream remote (to sync with original repo)
git remote add upstream https://github.com/sehmaluva/student-fest.git

# Verify remotes
git remote -v
```

### 3. Explore the Project Structure

```bash
# List all directories
ls -la

# Check the project structure
tree -L 3  # If you have tree installed
# OR
find . -type d -not -path '*/.*' | head -20
```

### 4. Create Your First Branch

```bash
# Always start from the latest main branch
git checkout main
git pull upstream main

# Create a new branch for your contribution
git checkout -b feature/your-contribution-name

# Examples:
# git checkout -b profile/alice-smith
# git checkout -b challenge/fibonacci-solver
# git checkout -b project/todo-app
```

## 🎯 Choose Your Contribution Type

### 📝 Profile Creation
Perfect for first-time contributors!

```bash
# Copy the template
cp docs/templates/PROFILE_TEMPLATE.md profiles/YOUR_GITHUB_USERNAME.md

# Edit your profile
code profiles/YOUR_GITHUB_USERNAME.md  # If using VS Code
# OR use your preferred editor
```

### 🧩 Solve a Challenge
Learn by doing!

```bash
# Browse available challenges
ls challenges/beginner/
ls challenges/intermediate/
ls challenges/advanced/

# Choose a challenge and read the instructions
cat challenges/beginner/hello-world-plus/README.md
```

### 🚀 Build a Project
Create something awesome!

```bash
# Check out project ideas
ls projects/web/
ls projects/cli/
ls projects/games/
ls projects/utilities/

# Read project requirements
cat projects/web/badge-generator/README.md
```

### 📚 Improve Documentation
Help others learn!

```bash
# Look for documentation opportunities
ls docs/guides/
ls docs/templates/

# Check for TODO items or areas to improve
grep -r "TODO\|FIXME\|Coming soon" docs/
```

## 🛠️ Development Environment Setup

### For Web Development

If you're working on web projects:

```bash
# Install Node.js dependencies (if package.json exists)
npm install

# OR if using Yarn
yarn install

# Start development server (project-specific)
npm start
# OR
npm run dev
```

### For Python Development

If you're working with Python scripts:

```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies (if requirements.txt exists)
pip install -r requirements.txt

# Run Python scripts
python scripts/your_script.py
```

### For Go Development

If you're working with Go:

```bash
# Initialize Go module (if go.mod doesn't exist)
go mod init student-fest-contribution

# Install dependencies
go mod tidy

# Run Go programs
go run main.go

# Build executable
go build -o app main.go
```

## ✅ Testing Your Changes

### Before Committing

1. **Test your code locally**
   ```bash
   # For web projects
   npm test
   
   # For Python
   python -m pytest
   
   # For Go
   go test ./...
   ```

2. **Check for formatting issues**
   ```bash
   # For JavaScript
   npm run lint
   
   # For Python
   flake8 your_file.py
   
   # For Markdown
   markdownlint *.md
   ```

3. **Verify all files are included**
   ```bash
   git status
   git diff
   ```

### Manual Testing

- **Profiles**: Ensure markdown renders correctly
- **Challenges**: Run through the solution step-by-step
- **Projects**: Test all features and edge cases
- **Scripts**: Try different inputs and scenarios

## 📤 Submitting Your Contribution

### 1. Stage and Commit Your Changes

```bash
# Add your changes
git add .

# Commit with a descriptive message
git commit -m "feat: add interactive profile for alice-smith"

# Examples of good commit messages:
# git commit -m "feat: solve hello-world-plus challenge in Python"
# git commit -m "docs: update setup guide with Go instructions"
# git commit -m "fix: resolve badge generation bug in web app"
```

### 2. Push to Your Fork

```bash
# Push your branch to your fork
git push origin feature/your-contribution-name
```

### 3. Create a Pull Request

1. Go to your fork on GitHub
2. Click "Compare & pull request"
3. Fill out the PR template:
   - Clear title describing your contribution
   - Detailed description of what you built/changed
   - Screenshots or examples if applicable
   - Checklist items completed

### 4. Respond to Feedback

- Address any requested changes promptly
- Ask questions if feedback is unclear
- Be open to suggestions and improvements
- Thank reviewers for their time

## 🔄 Keeping Your Fork Updated

Regularly sync with the main repository:

```bash
# Switch to main branch
git checkout main

# Pull latest changes from upstream
git pull upstream main

# Push updates to your fork
git push origin main

# Update your feature branch (if needed)
git checkout feature/your-contribution-name
git rebase main
```

## ⚡ Pro Tips

### Git Best Practices
- **Small, focused commits**: One feature/fix per commit
- **Descriptive commit messages**: Use conventional commit format
- **Regular syncing**: Keep your fork up to date
- **Branch per feature**: Don't mix different contributions

### Code Quality
- **Follow project conventions**: Check existing code style
- **Add comments**: Explain complex logic
- **Include documentation**: Update README files
- **Test thoroughly**: Verify everything works

### Community Interaction
- **Be respectful**: Kind and constructive communication
- **Ask questions**: Don't hesitate to seek help
- **Help others**: Review other contributions
- **Share knowledge**: Document your learning process

## 🆘 Troubleshooting

### Common Git Issues

**Merge Conflicts:**
```bash
# Pull latest changes
git pull upstream main

# Resolve conflicts in your editor
# Then commit the resolution
git add .
git commit -m "resolve merge conflicts"
```

**Wrong Branch:**
```bash
# Move uncommitted changes to correct branch
git stash
git checkout correct-branch
git stash pop
```

**Reset to Clean State:**
```bash
# Discard all local changes (be careful!)
git reset --hard HEAD
git clean -fd
```

### Getting Help

- 🐛 **Issues**: [GitHub Issues](https://github.com/sehmaluva/student-fest/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/sehmaluva/student-fest/discussions)
- 📧 **Direct Contact**: Reach out to [@sehmaluva](https://github.com/sehmaluva)
- 📚 **Documentation**: Check our comprehensive guides in `docs/`

## 🎉 Ready to Contribute?

You're all set! Choose your adventure and start building something amazing:

1. 👤 **Create your profile** - Show off your skills
2. 🧩 **Solve challenges** - Learn while contributing
3. 🚀 **Build projects** - Create something meaningful
4. 📚 **Improve docs** - Help others get started

**Remember**: Every contribution matters, no matter how small. We're here to help you succeed!

---

**Happy Hacking! � Let's make Student Fest 2025 unforgettable! 🚀**

*Setup guide created by: sehmaluva*  
*Last updated: October 13, 2025*
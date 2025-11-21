# 🤖 GitHub Actions Workflows Documentation

This document explains the automated workflows that run on this repository to help maintain quality and provide a great contributor experience.

## 📋 Overview

Our workflows automate various tasks when contributors:
- Create or update Pull Requests
- Push to the main branch
- Open issues
- Merge contributions

## 🔄 Active Workflows

### 1. 🧪 Multi-Language Testing (`multi-language-testing.yml`)

**When it runs:** On Pull Requests that change files in `challenges/` or `projects/`

**What it does:**
- Detects which programming languages were changed (Python, JavaScript, Java, Go, C++)
- Runs language-specific tests and linting only for changed files
- Uses the `dorny/paths-filter` action to efficiently detect file changes

**Language Support:**
- **Python**: Runs `flake8` linting and `pytest` tests
- **JavaScript**: Runs `ESLint` linting and `Jest` tests
- **Java**: Compiles Java files and runs tests
- **Go**: Runs `go test` for Go modules
- **C++**: Uses CMake to build and run CTest

**Why it's important:** Ensures code quality and prevents broken submissions

### 2. 🙏 Update Contributors (`update-contributors.yml`)

**When it runs:** 
- On pushes to main branch
- When Pull Requests are merged

**What it does:**
- Automatically updates the `CONTRIBUTORS.md` file
- Uses the `akhilmhdh/contributors-readme-action` to maintain contributor list
- Commits changes with `[skip ci]` to avoid triggering other workflows

**Why it's important:** Recognizes and celebrates all contributors automatically

### 3. 🏆 Badge Generator & Stats (`badge-generator.yml`)

**When it runs:**
- On pushes to main branch
- When Pull Requests are merged

**What it does:**
- Runs existing contribution analysis scripts (if they exist)
- Generates contributor statistics badge using `wow-actions/contributors-svg`
- Uploads artifacts for debugging
- Auto-commits updated statistics

**Why it's important:** Provides visual recognition of contributions and project activity

### 4. 🚀 Contribution Validator (`contribution-validator.yml`)

**When it runs:** On Pull Requests that change files in `profiles/`, `challenges/`, `projects/`, or `scripts/`

**What it does:**
- Validates markdown files for broken links
- Runs existing validation scripts for contributions
- Checks file structure (profiles, challenges, projects directories)
- Automatically labels PRs based on changed files using `actions/labeler`

**Labels applied:**
- `profile` - for profile contributions
- `challenge` - for challenge solutions
- `project` - for project submissions
- `script` - for utility scripts
- `documentation` - for docs changes
- `beginner-friendly`, `intermediate`, `advanced` - difficulty levels

**Why it's important:** Ensures contributions meet quality standards and are properly categorized

### 5. 🎉 First-Time Contributor Welcome (`welcome-contributors.yml`)

**When it runs:**
- When a Pull Request is opened
- When an Issue is opened

**What it does:**
- Welcomes first-time contributors with helpful information
- Provides links to contribution guides and resources
- Auto-labels PRs based on file types and difficulty
- Explains what happens next in the review process

**Why it's important:** Makes new contributors feel welcome and provides guidance

## 🔧 Configuration Files

### `.github/labeler.yml`
Defines rules for automatically labeling PRs based on which files were changed.

### `.github/workflows/markdown-link-check-config.json`
Configuration for the markdown link checker:
- Ignores localhost URLs
- Retries failed requests
- Handles Discord invite links

## 💡 Tips for Contributors

### How to Test Locally

Before submitting a PR, you can run the same checks locally:

**Python:**
```bash
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
pytest challenges/ projects/ -v
```

**JavaScript:**
```bash
npm install
npx eslint challenges/ projects/ --ext .js
npm test
```

**Java:**
```bash
find challenges/ projects/ -name "*.java" -exec javac {} \;
```

### Understanding Workflow Failures

If a workflow fails on your PR:
1. Click on "Details" next to the failed check
2. Read the error message in the logs
3. Fix the issue locally
4. Push the fix to your branch
5. The workflows will run automatically again

### Skipping CI

If you need to make a documentation-only change that doesn't need testing:
- Add `[skip ci]` to your commit message
- Example: `docs: update README [skip ci]`

## 🚨 Common Issues & Solutions

### Issue: Python linting fails
**Solution:** Run `flake8` locally and fix reported issues

### Issue: Markdown link check fails
**Solution:** Check that all links in your markdown files are valid and accessible

### Issue: Workflow runs but nothing happens
**Solution:** Check if the workflow's trigger conditions match your changes (e.g., file paths)

### Issue: Auto-labeling doesn't work
**Solution:** Ensure your changes match patterns in `.github/labeler.yml`

## 🔐 Permissions & Secrets

The workflows use `GITHUB_TOKEN` which is automatically provided by GitHub Actions:
- Read access to repository contents
- Write access to create comments and labels
- Ability to commit changes (for auto-updates)

No additional secrets are required for basic functionality.

## 📊 Monitoring Workflow Health

Maintainers can check workflow status at:
```
https://github.com/sehmaluva/student-fest/actions
```

Each workflow run shows:
- Which files triggered it
- Detailed logs for each step
- Any errors or warnings
- Artifacts generated (if any)

## 🛠️ Maintenance

### Updating Actions

Keep actions up to date by checking for newer versions:
- `actions/checkout` - currently v4
- `actions/setup-python` - currently v5
- `actions/setup-node` - currently v4
- `actions/setup-java` - currently v4
- `actions/setup-go` - currently v5
- `dorny/paths-filter` - currently v3
- `actions/labeler` - currently v5

### Adding New Languages

To add support for a new language in multi-language testing:

1. Add file pattern to `detect-changes` job filters
2. Create a new test job with the language setup
3. Define linting and testing commands
4. Update this documentation

### Modifying Labels

To change auto-labeling behavior:
1. Edit `.github/labeler.yml`
2. Add/modify path patterns
3. Ensure labels exist in the repository

## 🤝 Contributing to Workflows

If you want to improve our workflows:
1. Test changes in your fork first
2. Ensure workflows are syntactically valid using `yamllint`
3. Document any new features or changes
4. Submit a PR with clear explanation of improvements

## 📚 Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax Reference](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
- [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)
- [YAML Syntax Guide](https://yaml.org/spec/1.2/spec.html)

## 🎯 Goals

Our automation aims to:
1. **Reduce manual work** for maintainers
2. **Improve code quality** through automated checks
3. **Welcome new contributors** with helpful guidance
4. **Recognize contributions** automatically
5. **Maintain consistency** across the project

---

**Last Updated:** 2025-11-21

For questions about workflows, open an issue or ask in discussions!

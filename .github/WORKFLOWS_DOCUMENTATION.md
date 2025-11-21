# GitHub Actions Workflows Documentation

This document provides an overview of all GitHub Actions workflows in this repository and how they help automate the Student Fest project.

## 📋 Workflow Overview

### 1. 🏆 Badge Generator & Deployer (`badge-generator.yml`)

**Trigger:** Push to main, PR closed on main

**Purpose:** Generates contributor badges and statistics

**What it does:**
- Analyzes all contributions to the repository
- Generates visual badges for contributors
- Deploys badges to GitHub Pages
- Updates README with contribution statistics

**Jobs:**
- `generate-badges`: Analyzes contributions and generates badge images
- `deploy-badges`: Deploys badges to gh-pages branch
- `update-readme`: Updates README with latest statistics

**Note:** Currently uses only scripts that exist in the repository. Future scripts can be added when implemented.

---

### 2. 🚀 Contribution Validator (`contribution-validator.yml`)

**Trigger:** PR to main, push to main (for specific paths)

**Purpose:** Validates contributions and ensures quality

**What it does:**
- Validates all types of contributions (profiles, challenges, projects, scripts)
- Runs quality checks
- Generates contribution badges
- Deploys badges automatically on merge to main

**Jobs:**
- `validate-contribution`: Runs validation scripts
- `badge-generator`: Generates and deploys badges (only on main)

**Monitored paths:**
- `profiles/**` - Student profiles
- `challenges/**` - Coding challenges
- `projects/**` - Student projects
- `scripts/**` - Automation scripts

---

### 3. 🧪 Multi-Language Testing (`multi-language-testing.yml`)

**Trigger:** PR to main (when challenges or projects change)

**Purpose:** Tests code in multiple programming languages

**What it does:**
- Detects which language files changed in a PR
- Runs appropriate language-specific tests
- Ensures code quality across Python, JavaScript, Java, Go, and C++

**Languages supported:**
- **Python**: pytest, flake8
- **JavaScript**: Jest, ESLint
- **Java**: javac, JUnit
- **Go**: go test
- **C++**: CMake, ctest

**Note:** Tests only run if relevant file types are changed in the PR

---

### 4. 🔄 Update Contributors (`update-contributors.yml`)

**Trigger:** PR merged to main

**Purpose:** Automatically adds new contributors to the contributors list

**What it does:**
- Detects when a PR is merged
- Extracts PR author information
- Updates contributors.json with new contributor data
- Commits changes automatically

**Uses:** 
- `stefanzweifel/git-auto-commit-action@v4` for automatic commits
- `jq` for JSON manipulation

---

### 5. 🎉 First-Time Contributor Welcome (`welcome-contributors.yml`)

**Trigger:** New PR or issue opened

**Purpose:** Welcomes new contributors and provides guidance

**What it does:**
- Detects first-time contributors
- Posts comprehensive welcome message with:
  - Step-by-step guidance on what happens next
  - Links to essential documentation
  - Quick tips for success
  - Common issues and solutions
- Automatically labels PRs based on file changes
- Labels difficulty level based on PR content

**Two jobs:**
- `welcome`: Welcomes PR contributors
- `issue-welcome`: Welcomes issue creators

**Smart features:**
- Checks if this is the user's first contribution
- Provides context-specific guidance
- Links to helpful resources

---

### 6. 🏷️ PR Auto Labeler (`pr-labeler.yml`)

**Trigger:** PR opened, synchronized, or reopened

**Purpose:** Automatically labels PRs for better organization

**What it does:**
- Analyzes changed files in the PR
- Adds appropriate labels based on:
  - **Type**: profile, challenge, project, script, documentation, workflow
  - **Language**: python, javascript, java, go, cpp, rust, ruby
  - **Size**: XS, S, M, L, XL (based on lines changed)
  - **Status**: first-contribution, good-first-issue (for first-timers)
- Posts PR size comment with advice
- Provides review checklist

**Size thresholds:**
- XS: < 10 lines
- S: 10-49 lines
- M: 50-199 lines
- L: 200-499 lines
- XL: 500+ lines

---

### 7. 🔍 PR Quality Checker (`pr-quality-checker.yml`)

**Trigger:** PR opened, synchronized, or reopened

**Purpose:** Provides helpful feedback on PR quality

**What it does:**
- **Checks PR title:**
  - Length (minimum 10 characters)
  - Format (suggests conventional commit style)
  - Clarity (warns about vague titles)
  
- **Checks PR description:**
  - Completeness (warns if too short)
  - Template usage
  - Issue references (reminds to use "Closes #" syntax)
  
- **Checks for common mistakes:**
  - node_modules/ in commits
  - .DS_Store files
  - Very large files (>1000 lines)
  - Too many files changed (>50)

**Provides:**
- Actionable suggestions for improvement
- Examples of good practices
- Commands to fix common issues

---

## 🔧 Maintenance Guide

### Adding a New Workflow

1. Create a new `.yml` file in `.github/workflows/`
2. Define the trigger events (`on:`)
3. Define jobs and steps
4. Test locally using act: `act -l` to list events
5. Validate YAML: `python3 -c "import yaml; yaml.safe_load(open('file.yml'))"`
6. Commit and push to a test branch first

### Updating Existing Workflows

1. Make your changes
2. Validate YAML syntax (see above)
3. Test on a draft PR if possible
4. Update this documentation if behavior changes
5. Commit with clear description of changes

### Troubleshooting Workflows

**Workflow not running?**
- Check trigger conditions match your event
- Verify `paths:` filters if used
- Check branch protection rules

**Workflow failing?**
- Check the Actions tab for detailed logs
- Verify all referenced scripts exist
- Check for typos in action names/versions
- Ensure secrets are properly configured

**Script not found error?**
- Verify the script exists in `scripts/` directory
- Check file permissions
- Ensure Python dependencies are installed

---

## 📊 Workflow Best Practices

### For Contributors
- Let workflows run completely before pushing fixes
- Read automation feedback carefully
- Don't disable workflows unless absolutely necessary
- Ask for help if workflows consistently fail

### For Maintainers
- Keep workflows focused on one task
- Use descriptive names and emojis for clarity
- Add comments explaining complex logic
- Version lock action dependencies for stability
- Test workflow changes on non-main branches first
- Update documentation when workflows change

---

## 🔒 Security Considerations

### Permissions
- Workflows use least-privilege access
- `pull_request_target` used carefully to avoid injection
- Secrets only exposed to trusted actions

### Safe Practices
- Never use unvalidated user input in shell commands
- Validate all external actions before using
- Keep action versions pinned
- Review script outputs before committing

---

## 📈 Future Improvements

Potential enhancements for workflows:

1. **Code coverage tracking**: Add codecov integration
2. **Performance testing**: Add benchmark comparisons
3. **Dependency updates**: Add dependabot or renovate
4. **Security scanning**: Add CodeQL analysis
5. **Accessibility testing**: Add a11y checks for web projects
6. **Visual regression**: Add screenshot comparisons for UI changes

---

## 🆘 Getting Help

If you need help with workflows:

1. Check existing workflow runs for examples
2. Read GitHub Actions documentation: https://docs.github.com/actions
3. Ask in repository discussions
4. Tag maintainers in issues

---

## 📝 Changelog

### 2025-11-21
- ✅ Fixed deprecated `set-output` command in update-contributors.yml
- ✅ Updated artifact actions from v3 to v4
- ✅ Removed references to non-existent scripts
- ✅ Added PR auto-labeler workflow
- ✅ Added PR quality checker workflow
- ✅ Enhanced welcome messages with detailed guidance
- ✅ Created comprehensive PR template
- ✅ Validated all workflows for YAML correctness

---

*Last updated: 2025-11-21*
*Maintainer: @sehmaluva*

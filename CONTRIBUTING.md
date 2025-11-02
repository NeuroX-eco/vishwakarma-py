# Contributing to Vishwakarma AI

**© 2025 Vishwakarma Industries**

Thank you for your interest in contributing to Vishwakarma AI! This document provides guidelines for contributing to the project.

---

## 📋 Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Development Setup](#development-setup)
4. [Coding Standards](#coding-standards)
5. [Commit Guidelines](#commit-guidelines)
6. [Pull Request Process](#pull-request-process)
7. [Testing](#testing)

---

## 🤝 Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Maintain professional communication
- Respect intellectual property rights

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Git
- Basic understanding of voice assistants
- Familiarity with Python, JavaScript, HTML/CSS

### Fork and Clone
```bash
git clone <your-fork-url>
cd jarvis-main
```

---

## 💻 Development Setup

1. **Create Virtual Environment**
```bash
python -m venv envvishwakarma
envvishwakarma\Scripts\activate  # Windows
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Setup Face Recognition**
```bash
python engine/auth/sample.py
python engine/auth/trainer.py
```

4. **Create Feature Branch**
```bash
git checkout -b feature/your-feature-name
```

---

## 📝 Coding Standards

### Python Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and small

**Example:**
```python
"""
Vishwakarma AI - Module Name
© 2025 Vishwakarma Industries
"""

def function_name(param1, param2):
    """
    Brief description of function.
    
    Args:
        param1 (type): Description
        param2 (type): Description
        
    Returns:
        type: Description
    """
    # Implementation
    pass
```

### JavaScript Code Style
- Use JSDoc comments
- Use camelCase for variables
- Use const/let instead of var
- Add semicolons

**Example:**
```javascript
/**
 * Vishwakarma AI - Module Name
 * © 2025 Vishwakarma Industries
 */

/**
 * Function description
 * @param {string} param1 - Description
 * @returns {boolean} Description
 */
function functionName(param1) {
    // Implementation
}
```

### File Headers
All files must include copyright header:
```python
"""
Vishwakarma AI - [Module Name]
© 2025 Vishwakarma Industries
"""
```

---

## 📌 Commit Guidelines

### Commit Message Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting)
- **refactor**: Code refactoring
- **test**: Adding tests
- **chore**: Maintenance tasks

### Examples
```
feat(voice): Add multi-language support

- Added Spanish language support
- Updated language detection
- Modified TTS engine configuration

Closes #123
```

```
fix(auth): Resolve face recognition timeout issue

Fixed timeout error when camera initialization takes longer than expected.

Fixes #456
```

---

## 🔄 Pull Request Process

1. **Update Documentation**
   - Update README.md if needed
   - Update CHANGELOG.md
   - Add inline comments

2. **Test Your Changes**
   - Test all affected features
   - Ensure no regressions
   - Test on Windows (primary platform)

3. **Create Pull Request**
   - Use descriptive title
   - Reference related issues
   - Provide detailed description
   - Include screenshots/videos if UI changes

4. **PR Template**
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

## Testing
- [ ] Tested on Windows
- [ ] Face recognition works
- [ ] Voice commands work
- [ ] No console errors

## Screenshots
(if applicable)

## Related Issues
Closes #issue_number
```

---

## 🧪 Testing

### Manual Testing Checklist
- [ ] Face authentication works
- [ ] Voice recognition responds correctly
- [ ] Wake word detection triggers
- [ ] Text-to-speech is clear
- [ ] UI animations work smoothly
- [ ] Database operations succeed
- [ ] No console errors
- [ ] Application starts without errors

### Test Voice Commands
- "Open Chrome"
- "Play music on YouTube"
- "What is AI?"

---

## 🐛 Reporting Bugs

### Bug Report Template
```markdown
**Description**
Clear description of the bug

**Steps to Reproduce**
1. Step 1
2. Step 2
3. Step 3

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Environment**
- OS: Windows 10/11
- Python Version: 3.x
- Vishwakarma AI Version: 1.0.0

**Screenshots**
(if applicable)

**Additional Context**
Any other relevant information
```

---

## 💡 Feature Requests

### Feature Request Template
```markdown
**Feature Description**
Clear description of the proposed feature

**Use Case**
Why is this feature needed?

**Proposed Solution**
How should it work?

**Alternatives Considered**
Other approaches you've thought about

**Additional Context**
Any other relevant information
```

---

## 📚 Documentation

- Keep README.md updated
- Document new features in CHANGELOG.md
- Add inline comments for complex logic
- Update QUICKSTART.md if setup changes

---

## 🏗️ Project Structure

```
jarvis-main/
├── engine/           # Core Python modules
│   ├── auth/        # Face recognition
│   ├── command.py   # Command processing
│   ├── features.py  # Feature implementations
│   ├── helper.py    # Utilities
│   ├── db.py        # Database
│   └── config.py    # Configuration
├── www/             # Web interface
│   ├── assets/      # Static files
│   └── *.html/js/css
├── main.py          # Application entry
├── run.py           # Launcher
└── device.bat       # ADB setup
```

---

## 🎯 Development Priorities

### High Priority
- Bug fixes
- Security improvements
- Performance optimization

### Medium Priority
- New features
- UI/UX enhancements
- Documentation improvements

### Low Priority
- Code refactoring
- Style improvements
- Minor enhancements

---

## 📞 Questions?

For questions or discussions, please open an issue with the "question" label.

---

## 📄 License

By contributing, you agree that your contributions will be licensed under the same proprietary license as Vishwakarma AI.

---

**Thank you for contributing to Vishwakarma AI!**

*Crafting Intelligence, Building Solutions*

© 2025 Vishwakarma Industries. All rights reserved.

# Contributing to CS Crawler MCP

First off, thank you for considering contributing to this project!

## How Can I Contribute?

### Reporting Bugs

If you find a bug, please open an issue and provide the following information:

*   A clear and descriptive title.
*   A step-by-step description of how to reproduce the bug.
*   The expected behavior and what actually happened.
*   Your environment details (e.g., Python version, OS).

### Suggesting Enhancements

If you have an idea for an enhancement, please open an issue to discuss it. This allows us to coordinate efforts and ensure the change aligns with the project's goals.

### Pull Requests

1.  Fork the repository and create your branch from `main`.
2.  If you've added code that should be tested, add tests.
3.  Ensure your code lints and follows the existing style.
4.  Make sure your commit messages are clear and descriptive.
5.  Open a pull request, and link it to any relevant issues.

We look forward to your contributions!
   pip install -r requirements.txt
   pip install crawl4ai mcp
   ```

4. **Install Playwright browsers:**
   ```bash
   python -m playwright install chromium
   ```

5. **Set up development configuration:**
   ```bash
   cp config.json.template config.json
   # Edit config.json with your paths
   ```

6. **Test the installation:**
   ```bash
   python3 tests/test_wrapper.py
   ```

## 🛠️ Development Workflow

### Making Changes

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes:**
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed

3. **Test your changes:**
   ```bash
   # Test the wrapper
   python3 tests/test_wrapper.py
   
   # Test the server directly
   python3 server.py
   ```

4. **Commit your changes:**
   ```bash
   git add .
   git commit -m "Add: brief description of your changes"
   ```

### Code Style

- Use Python 3.8+ features
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused

### Testing

- All new features should include tests
- Test both success and error cases
- Ensure tests pass before submitting PR

## 📝 Submitting Changes

### Pull Request Process

1. **Update your fork:**
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Push your changes:**
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create a Pull Request:**
   - Use a clear, descriptive title
   - Describe what changes you made and why
   - Reference any related issues
   - Include screenshots if applicable

### Pull Request Template

```markdown
## Description
Brief description of the changes made.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing
- [ ] I have tested these changes locally
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
```

## 🐛 Reporting Issues

### Before Reporting

1. Check if the issue already exists
2. Try the latest version
3. Test with a minimal configuration

### Issue Template

```markdown
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Environment (please complete the following information):**
- OS: [e.g. macOS, Windows, Linux]
- Python version: [e.g. 3.8, 3.9, 3.10]
- Crawl4AI version: [e.g. 0.3.0]
- MCP client: [e.g. Claude Desktop, BoltAI]

**Additional context**
Add any other context about the problem here.
```

## 🎯 Areas for Contribution

### High Priority
- **Bug fixes** - Any issues you encounter
- **Documentation improvements** - Better examples, clearer instructions
- **Test coverage** - More comprehensive testing
- **Performance optimizations** - Faster crawling, better memory usage

### Medium Priority
- **New features** - Additional crawling options, output formats
- **Docker improvements** - Better containerization
- **CI/CD enhancements** - Automated testing, deployment
- **Cross-platform support** - Windows, Linux compatibility

### Low Priority
- **Code refactoring** - Cleaner code structure
- **UI improvements** - Better error messages, logging
- **Integration examples** - More MCP client examples

## 📚 Documentation

### Adding Documentation

- Update README.md for user-facing changes
- Add examples to the examples/ directory
- Update docstrings for code changes
- Create new documentation files in docs/ if needed

### Documentation Style

- Use clear, concise language
- Include code examples
- Add screenshots for UI changes
- Keep documentation up-to-date with code changes

## 🔧 Development Tools

### Recommended Tools

- **Code Editor:** VS Code, PyCharm, or your preferred editor
- **Python Linting:** flake8, black, isort
- **Testing:** pytest
- **Version Control:** Git with meaningful commit messages

### Pre-commit Hooks (Optional)

```bash
pip install pre-commit
pre-commit install
```

## 📞 Getting Help

- **GitHub Issues** - For bug reports and feature requests
- **GitHub Discussions** - For questions and general discussion
- **Pull Request Comments** - For code review feedback

## 🏆 Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- GitHub contributor list

Thank you for contributing to CS Crawler MCP! 🎉

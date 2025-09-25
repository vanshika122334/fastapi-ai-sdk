# Contributing to FastAPI AI SDK

First off, thank you for considering contributing to FastAPI AI SDK! It's people like you that make FastAPI AI SDK such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to me@arif.sh.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- Use a clear and descriptive title
- Describe the exact steps which reproduce the problem
- Provide specific examples to demonstrate the steps
- Describe the behavior you observed after following the steps
- Explain which behavior you expected to see instead and why
- Include any error messages or stack traces

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. Create an issue and provide the following information:

- Use a clear and descriptive title
- Provide a step-by-step description of the suggested enhancement
- Provide specific examples to demonstrate the steps
- Describe the current behavior and explain which behavior you expected to see instead
- Explain why this enhancement would be useful

### Pull Requests

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Development Setup

1. Fork and clone the repository:

```bash
git clone https://github.com/your-username/fastapi-ai-sdk.git
cd fastapi-ai-sdk
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install in development mode:

```bash
pip install -e ".[dev]"
```

4. Create a branch:

```bash
git checkout -b feature/your-feature-name
```

## Development Workflow

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=fastapi_ai_sdk --cov-report=term-missing

# Run specific test file
pytest tests/test_models.py

# Run tests matching pattern
pytest -k "test_stream"
```

### Code Quality

Before submitting, ensure your code passes all quality checks:

```bash
# Format code with Black
black fastapi_ai_sdk tests examples

# Sort imports with isort
isort fastapi_ai_sdk tests examples

# Lint with flake8
flake8 fastapi_ai_sdk tests examples

# Type check with mypy
mypy fastapi_ai_sdk
```

### Building Documentation

If you're updating documentation:

```bash
# Install documentation dependencies
pip install -e ".[docs]"

# Build docs
cd docs
make html
```

## Style Guide

### Python Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use [Black](https://black.readthedocs.io/) for code formatting (line length: 88)
- Use [isort](https://pycqa.github.io/isort/) for import sorting
- Add type hints for all public functions
- Write docstrings for all public modules, functions, classes, and methods

### Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

Example:

```
Add support for custom event types

- Implement DataEvent.create() factory method
- Add validation for event type prefixes
- Update tests to cover new functionality

Fixes #123
```

### Testing

- Write tests for all new functionality
- Maintain or increase code coverage
- Use pytest fixtures for common setup
- Use descriptive test names that explain what is being tested
- Group related tests in classes

Example:

```python
class TestAIStreamBuilder:
    def test_text_method_adds_three_events(self):
        """Test that text() method adds start, delta, and end events."""
        # Test implementation
```

## Project Structure

```
fastapi_ai_sdk/
├── fastapi_ai_sdk/       # Main package
│   ├── __init__.py       # Package initialization and exports
│   ├── models.py         # Pydantic models for events
│   ├── stream.py         # Stream builder and utilities
│   ├── response.py       # FastAPI response helpers
│   └── decorators.py     # Endpoint decorators
├── tests/                # Test suite
│   ├── test_models.py    # Model tests
│   ├── test_stream.py    # Stream tests
│   └── test_fastapi_integration.py  # Integration tests
├── examples/             # Example applications
├── docs/                 # Documentation
└── pyproject.toml        # Project configuration
```

## Release Process

1. Update version in `pyproject.toml` and `setup.py`
2. Update CHANGELOG.md
3. Commit changes: `git commit -am "Release version X.Y.Z"`
4. Tag the release: `git tag -a vX.Y.Z -m "Version X.Y.Z"`
5. Push changes: `git push && git push --tags`
6. Create GitHub release
7. Package will be automatically published to PyPI

## Getting Help

- Create an issue for bugs or feature requests
- Start a discussion for questions or ideas
- Email me@arif.sh for security issues (do not create public issues)

## Recognition

Contributors will be recognized in:

- The project README
- Release notes
- GitHub contributors page

Thank you for contributing to FastAPI AI SDK! 🎉

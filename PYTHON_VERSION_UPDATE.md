# Python Version Update

## Python 3.8 Support Dropped

As of September 2025, Python 3.8 has reached end-of-life (October 2024) and several modern dependencies no longer support it:

- **black** >=24.10.0 requires Python >=3.9
- Many other tools are dropping Python 3.8 support

### Changes Made:

1. **Minimum Python version**: Changed from `>=3.8` to `>=3.9`
2. **Updated all configuration files**:
   - `pyproject.toml` - requires-python, classifiers, tool configs
   - `setup.py` - python_requires and classifiers
   - `.github/workflows/ci.yml` - removed 3.8 from test matrix
   - `README.md` - updated badge to show Python 3.9+

### Supported Python Versions:

- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12
- Python 3.13

### Migration for Users:

If you're still using Python 3.8, you'll need to upgrade to Python 3.9 or later to use this library. Python 3.8 reached end-of-life in October 2024, so upgrading is recommended for security and compatibility reasons.

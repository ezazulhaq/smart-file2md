# Contributing to markdown-convert

Thank you for your interest in contributing to markdown-convert! This document provides guidelines and instructions for contributing.

## Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/markdown-convert.git
   cd markdown-convert
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install in development mode**
   ```bash
   pip install -e ".[dev]"
   ```

4. **Install Tesseract OCR** (if not already installed)
   - Ubuntu/Debian: `sudo apt-get install tesseract-ocr`
   - macOS: `brew install tesseract`
   - Windows: Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)

## Code Style

We follow standard Python conventions:

- **PEP 8**: Python code style guide
- **Black**: Code formatter (line length: 88)
- **Type hints**: All functions should have type annotations
- **Docstrings**: All public classes and functions should have docstrings

### Running Code Formatters

```bash
# Format code with Black
black src/ tests/

# Check linting with Ruff
ruff check src/ tests/

# Type checking with mypy
mypy src/
```

## Testing

All new features should include tests.

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=markdown_convert --cov-report=html

# Run specific test file
pytest tests/test_converters.py

# Run specific test
pytest tests/test_converters.py::test_pdf_converter
```

### Writing Tests

- Place tests in the `tests/` directory
- Name test files as `test_*.py`
- Name test functions as `test_*`
- Use descriptive test names that explain what is being tested

Example:
```python
def test_pdf_converter_extracts_text_from_valid_pdf():
    """Test that PDFConverter successfully extracts text from a valid PDF."""
    # Test implementation
    pass
```

## Pull Request Process

1. **Create a new branch** for your feature or bugfix
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the code style guidelines

3. **Add tests** for new functionality

4. **Run tests and linters** to ensure everything passes
   ```bash
   pytest
   black src/ tests/
   ruff check src/ tests/
   mypy src/
   ```

5. **Commit your changes** with clear, descriptive commit messages
   ```bash
   git commit -m "Add feature: description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request** on GitHub with:
   - Clear description of changes
   - Reference to any related issues
   - Screenshots (if applicable)

## Code Architecture

The project follows OOP and SOLID principles:

- **`converters/`**: Converter implementations (Strategy pattern)
  - `base.py`: Abstract base class
  - `pdf_converter.py`: Text extraction converter
  - `ocr_converter.py`: OCR-based converter
  - `factory.py`: Factory for creating converters

- **`config.py`**: Configuration management using dataclasses

- **`exceptions.py`**: Custom exception hierarchy

- **`utils/`**: Utility functions
  - `file_utils.py`: File handling utilities

- **`cli.py`**: Command-line interface

## Adding New Features

### Adding a New Converter

1. Create a new class in `src/markdown_convert/converters/`
2. Inherit from `BaseConverter`
3. Implement `_convert_to_markdown()` and `can_convert()` methods
4. Update `ConverterFactory` to include the new converter
5. Add tests in `tests/test_converters.py`

Example:
```python
from .base import BaseConverter

class MyNewConverter(BaseConverter):
    def can_convert(self, pdf_path: Path) -> bool:
        # Implementation
        pass
    
    def _convert_to_markdown(self, pdf_path: Path) -> str:
        # Implementation
        pass
```

## Reporting Issues

When reporting issues, please include:

- Python version
- Operating system
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Error messages (if any)

## Questions?

If you have questions, feel free to:
- Open an issue on GitHub
- Contact the maintainers

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

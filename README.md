# Smart File to Markdown Converter

[![PyPI version](https://badge.fury.io/py/smart-file2md.svg)](https://badge.fury.io/py/smart-file2md)
[![Python Support](https://img.shields.io/pypi/pyversions/smart-file2md.svg)](https://pypi.org/project/smart-file2md/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful and flexible tool to convert **PDF and DOCX files** to Markdown format with intelligent OCR fallback support for scanned documents.

## Features

- 🚀 **Fast text extraction** from text-based PDFs and DOCX files
- 🔍 **Automatic OCR fallback** for scanned PDFs and DOCX documents
- � **DOCX Support** with embedded image OCR for scanned Word documents
- �📦 **Batch processing** of multiple files
- 🔄 **Recursive directory processing**
- ⚙️ **Flexible configuration** options
- 🎯 **Smart converter selection** based on file type
- 📝 **Clean, well-structured code** following OOP and SOLID principles

## Installation

### From PyPI (recommended)

```bash
pip install smart-file2md
```

### From source

```bash
git clone https://github.com/ezazulhaq/smart-file2md.git
cd smart-file2md
pip install -e .
```

### System Requirements

This package requires **Tesseract OCR** to be installed on your system for OCR functionality:

**Ubuntu/Debian:**
```bash
sudo apt-get install tesseract-ocr
```

**macOS:**
```bash
brew install tesseract
```

**Windows:**
Download the installer from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)

## Usage

### Command Line Interface

```bash
# Convert a single PDF file
smart-file2md document.pdf

# Convert a DOCX file (OCR automatic for scanned documents)
smart-file2md document.docx

# Convert multiple files (mixed types supported)
smart-file2md file1.pdf file2.docx file3.pdf

# Convert all files in a directory
smart-file2md /path/to/files/

# Convert recursively with subdirectories
smart-file2md /path/to/files/ --recursive

# Specify an output directory
smart-file2md document.pdf --output-dir output/

# Process only the first 10 pages (PDF only)
smart-file2md document.pdf --max-pages 10

# Force OCR even for text-based PDFs
smart-file2md document.pdf --force-ocr

# Overwrite existing output files
smart-file2md document.pdf --overwrite
```

### Programmatic API

```python
from markdown_convert import convert_pdf

# Simple conversion
convert_pdf('document.pdf')

# With custom options
convert_pdf(
    'document.pdf',
    output_dir='output/',
    max_pages=10,
    force_ocr=False
)
```

### Advanced Usage

```python
from pathlib import Path
from markdown_convert import ConverterConfig, ConverterFactory

# Create custom configuration
config = ConverterConfig(
    output_dir=Path('output/'),
    max_pages=20,
    force_ocr=False,
    skip_existing=True,
    ocr_dpi=2,
    progress_interval=5
)

# Create converter and process
pdf_path = Path('document.pdf')
converter = ConverterFactory.create(pdf_path, config)
output_path = converter.convert(pdf_path)

print(f"Converted to: {output_path}")
```

## Output Location

If no output directory is specified with `--output-dir`, the tool creates a `markdown` directory in the same location as the source files and saves the converted files there.

## Options

| Option | Description |
|--------|-------------|
| `-o, --output-dir` | Specify output directory for markdown files |
| `-m, --max-pages` | Maximum number of pages to process per PDF |
| `--force-ocr` | Force using OCR even if text can be extracted directly |
| `-r, --recursive` | Recursively process directories |
| `--overwrite` | Overwrite existing output files (default: skip existing) |
| `--version` | Show version information |

## Performance Notes

- **Text-based PDFs/DOCX**: Very fast extraction using direct text extraction
- **Scanned PDFs/DOCX**: Slower due to OCR processing, but automatic fallback ensures compatibility
- **DOCX with images**: OCR automatically processes embedded images when no text is found

## Architecture

This project follows best practices in software design:

- **OOP Principles**: Encapsulation, inheritance, polymorphism, and abstraction
- **SOLID Principles**: Single responsibility, open/closed, Liskov substitution, interface segregation, and dependency inversion
- **Design Patterns**: Strategy pattern for converters, Factory pattern for converter selection, Template Method for conversion workflow
- **Type Safety**: Full type hints throughout the codebase
- **Separation of Concerns**: Clear separation between CLI, business logic, and utilities

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/ezazulhaq/markdown-convert.git
cd markdown-convert

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=markdown_convert --cov-report=html
```

### Code Quality

```bash
# Format code
black src/ tests/

# Lint code
ruff check src/ tests/

# Type checking
mypy src/
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Ezaz Ul Haq**

## Acknowledgments

- [PyMuPDF](https://pymupdf.readthedocs.io/) for PDF processing
- [pymupdf4llm](https://github.com/pymupdf/pymupdf4llm) for PDF to markdown conversion
- [Mammoth](https://github.com/mwilliamson/python-mammoth) for DOCX to HTML conversion
- [Markdownify](https://github.com/matthewwithanm/python-markdownify) for HTML to markdown conversion
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for optical character recognition
- [Pillow](https://python-pillow.org/) for image processing
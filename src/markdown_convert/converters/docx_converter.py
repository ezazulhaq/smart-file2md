"""Docx converter using mammoth and markdownify."""

from pathlib import Path
from typing import Optional

import mammoth
from markdownify import markdownify as md

from .base import BaseConverter
from ..config import ConverterConfig
from ..exceptions import ConversionError


class DocxConverter(BaseConverter):
    """Converter for Docx files.

    This converter uses mammoth to convert Docx to HTML,
    and then uses markdownify to convert HTML to Markdown.
    """

    def __init__(self, config: Optional[ConverterConfig] = None):
        """Initialize the Docx converter.

        Args:
            config: Converter configuration.
        """
        super().__init__(config)

    def can_convert(self, file_path: Path) -> bool:
        """Check if file is a Docx file.

        Args:
            file_path: Path to the file.

        Returns:
            True if file is a .docx file, False otherwise.
        """
        return file_path.suffix.lower() == '.docx'

    def _convert_to_markdown(self, file_path: Path) -> str:
        """Convert Docx to markdown.

        Args:
            file_path: Path to the Docx file.

        Returns:
            Markdown text content.

        Raises:
            ConversionError: If conversion fails.
        """
        try:
            print(f"Processing: {file_path}")
            print("Using Docx converter...")

            with open(file_path, "rb") as docx_file:
                result = mammoth.convert_to_html(docx_file)
                html = result.value
                messages = result.messages

                if messages:
                    for message in messages:
                        print(f"Docx warning: {message}")

            # Convert HTML to Markdown
            markdown_text = md(html, heading_style="ATX")

            print(f"Extracted {len(markdown_text)} characters")
            return markdown_text

        except Exception as e:
            raise ConversionError(
                str(file_path),
                f"Docx conversion failed: {str(e)}"
            )

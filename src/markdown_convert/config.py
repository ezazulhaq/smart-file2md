"""Configuration management for markdown-convert."""

from dataclasses import dataclass
from typing import Optional
from pathlib import Path

from .exceptions import InvalidConfigError


@dataclass(frozen=True)
class ConverterConfig:
    """Configuration for PDF to Markdown conversion.
    
    Attributes:
        output_dir: Optional output directory for markdown files.
                   If None, creates 'markdown' directory next to PDF.
        max_pages: Maximum number of pages to process. None means all pages.
        force_ocr: Force OCR even if text can be extracted directly.
        skip_existing: Skip conversion if output file already exists.
        ocr_dpi: DPI for rendering PDF pages to images for OCR (default: 2x = 144 DPI).
        progress_interval: Show progress every N pages during OCR.
    """
    
    output_dir: Optional[Path] = None
    max_pages: Optional[int] = None
    force_ocr: bool = False
    skip_existing: bool = True
    ocr_dpi: int = 2
    progress_interval: int = 5
    
    def __post_init__(self):
        """Validate configuration after initialization."""
        if self.max_pages is not None and self.max_pages < 1:
            raise InvalidConfigError("max_pages must be at least 1")
        
        if self.ocr_dpi < 1:
            raise InvalidConfigError("ocr_dpi must be at least 1")
        
        if self.progress_interval < 1:
            raise InvalidConfigError("progress_interval must be at least 1")
        
        # Convert output_dir to Path if it's a string
        if self.output_dir is not None and not isinstance(self.output_dir, Path):
            object.__setattr__(self, 'output_dir', Path(self.output_dir))
    
    @classmethod
    def default(cls) -> 'ConverterConfig':
        """Create a default configuration."""
        return cls()
    
    def with_updates(self, **kwargs) -> 'ConverterConfig':
        """Create a new config with updated values.
        
        Args:
            **kwargs: Fields to update.
            
        Returns:
            New ConverterConfig instance with updated values.
        """
        # Get current values as dict
        current = {
            'output_dir': self.output_dir,
            'max_pages': self.max_pages,
            'force_ocr': self.force_ocr,
            'skip_existing': self.skip_existing,
            'ocr_dpi': self.ocr_dpi,
            'progress_interval': self.progress_interval,
        }
        # Update with new values
        current.update(kwargs)
        return ConverterConfig(**current)

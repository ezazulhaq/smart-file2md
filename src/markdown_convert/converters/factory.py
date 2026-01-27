"""Factory for creating appropriate PDF converters."""

from pathlib import Path
from typing import Optional

from .base import BaseConverter
from .pdf_converter import PDFConverter
from .ocr_converter import OCRConverter
from ..config import ConverterConfig


class ConverterFactory:
    """Factory for creating appropriate converters based on PDF type.
    
    This factory implements the Factory pattern to automatically select
    the best converter for a given PDF file.
    """
    
    @staticmethod
    def create(
        pdf_path: Path,
        config: Optional[ConverterConfig] = None
    ) -> BaseConverter:
        """Create an appropriate converter for the given PDF.
        
        Selection logic:
        1. If force_ocr is True, use OCRConverter
        2. If PDF has extractable text, use PDFConverter
        3. Otherwise, fall back to OCRConverter
        
        Args:
            pdf_path: Path to the PDF file.
            config: Converter configuration.
            
        Returns:
            An appropriate converter instance.
        """
        config = config or ConverterConfig.default()
        
        # If forcing OCR, use OCR converter
        if config.force_ocr:
            print("Force OCR enabled, using OCR converter")
            return OCRConverter(config)
        
        # Try PDF converter first (faster)
        pdf_converter = PDFConverter(config)
        if pdf_converter.can_convert(pdf_path):
            print("PDF contains text, using standard converter")
            return pdf_converter
        
        # Fall back to OCR
        print("PDF appears to be scanned, using OCR converter")
        return OCRConverter(config)
    
    @staticmethod
    def create_pdf_converter(
        config: Optional[ConverterConfig] = None
    ) -> PDFConverter:
        """Create a standard PDF converter.
        
        Args:
            config: Converter configuration.
            
        Returns:
            PDFConverter instance.
        """
        return PDFConverter(config)
    
    @staticmethod
    def create_ocr_converter(
        config: Optional[ConverterConfig] = None
    ) -> OCRConverter:
        """Create an OCR converter.
        
        Args:
            config: Converter configuration.
            
        Returns:
            OCRConverter instance.
        """
        return OCRConverter(config)

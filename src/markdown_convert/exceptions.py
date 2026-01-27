"""Custom exceptions for markdown-convert package."""


class MarkdownConvertError(Exception):
    """Base exception for all markdown-convert errors."""
    pass


class PDFNotFoundError(MarkdownConvertError):
    """Raised when a PDF file cannot be found."""
    
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        super().__init__(f"PDF file not found: {pdf_path}")


class ConversionError(MarkdownConvertError):
    """Raised when PDF conversion fails."""
    
    def __init__(self, pdf_path: str, reason: str):
        self.pdf_path = pdf_path
        self.reason = reason
        super().__init__(f"Failed to convert {pdf_path}: {reason}")


class OCRError(MarkdownConvertError):
    """Raised when OCR processing fails."""
    
    def __init__(self, pdf_path: str, page_num: int, reason: str):
        self.pdf_path = pdf_path
        self.page_num = page_num
        self.reason = reason
        super().__init__(
            f"OCR failed for {pdf_path} at page {page_num}: {reason}"
        )


class InvalidConfigError(MarkdownConvertError):
    """Raised when configuration is invalid."""
    
    def __init__(self, message: str):
        super().__init__(f"Invalid configuration: {message}")

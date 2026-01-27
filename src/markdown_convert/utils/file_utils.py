"""Utility functions for file handling."""

import os
import glob
from pathlib import Path
from typing import List, Optional


def find_pdf_files(paths: List[str], recursive: bool = False) -> List[Path]:
    """Find all PDF files from given paths.
    
    Args:
        paths: List of file paths, directory paths, or glob patterns.
        recursive: If True, search directories recursively.
        
    Returns:
        List of Path objects for found PDF files, sorted and deduplicated.
    """
    pdf_files = []
    
    for path_str in paths:
        path = Path(path_str)
        
        if path.is_dir():
            # Directory: find all PDFs
            if recursive:
                pdf_files.extend(path.rglob('*.pdf'))
            else:
                pdf_files.extend(path.glob('*.pdf'))
        elif path.is_file() and path.suffix.lower() == '.pdf':
            # Direct PDF file
            pdf_files.append(path)
        elif '*' in path_str or '?' in path_str:
            # Glob pattern
            pdf_files.extend(Path(p) for p in glob.glob(path_str))
    
    # Remove duplicates and sort
    return sorted(set(pdf_files))


def get_output_path(pdf_path: Path, output_dir: Optional[Path] = None) -> Path:
    """Determine the output path for a converted markdown file.
    
    Args:
        pdf_path: Path to the input PDF file.
        output_dir: Optional output directory. If None, creates 'markdown'
                   directory next to the PDF.
                   
    Returns:
        Path object for the output markdown file.
    """
    # Get base filename without extension
    md_filename = pdf_path.stem + '.md'
    
    if output_dir:
        return output_dir / md_filename
    else:
        # Create markdown directory next to PDF
        markdown_dir = pdf_path.parent / 'markdown'
        return markdown_dir / md_filename


def ensure_directory(path: Path) -> None:
    """Ensure a directory exists, creating it if necessary.
    
    Args:
        path: Directory path to ensure exists.
    """
    path.mkdir(parents=True, exist_ok=True)


def should_skip_conversion(output_path: Path, skip_existing: bool) -> bool:
    """Check if conversion should be skipped.
    
    Args:
        output_path: Path to the output file.
        skip_existing: If True, skip if output file exists.
        
    Returns:
        True if conversion should be skipped, False otherwise.
    """
    return skip_existing and output_path.exists()

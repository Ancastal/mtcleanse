"""Cleaning module for text data preprocessing.

This module provides classes and functions for cleaning and preprocessing
parallel text datasets for machine translation.
"""

import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

from rich.logging import RichHandler

from mtcleanse.cleaning.clean import TextCleaner
from mtcleanse.cleaning.config import CleaningConfig
from mtcleanse.cleaning.filters import (
    BasicCleaningFilter,
    DomainOutlierFilter,
    Filter,
    LengthOutlierFilter,
    QualityFilter,
)
from mtcleanse.cleaning.kiwi_filter import KiwiQualityFilter
from mtcleanse.cleaning.stats import CleaningStats

# Configure logging
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)
logger = logging.getLogger("mtcleanse")


class ParallelTextCleaner(TextCleaner):
    """Main user-facing class for cleaning parallel text datasets.

    This class inherits from TextCleaner and provides the same functionality
    with a simplified interface.
    """

    def __init__(self, config: Optional[Dict] = None):
        """
        Initialize the parallel text cleaner.

        Args:
            config: Dictionary of configuration parameters to override defaults
        """
        # Create cleaning config and cleaner
        self.config = CleaningConfig.from_dict(config)
        self.cleaner = TextCleaner(self.config)

    def clean_texts(
        self, source_texts: List[str], target_texts: List[str]
    ) -> Tuple[List[str], List[str]]:
        """
        Clean parallel texts directly from lists of strings.

        Args:
            source_texts: List of source language texts
            target_texts: List of target language texts

        Returns:
            Tuple of (cleaned source texts, cleaned target texts)
        """
        return self.clean_parallel_texts(source_texts, target_texts)

    def clean_files(
        self,
        source_file: Union[str, Path],
        target_file: Union[str, Path],
        output_source: Optional[Union[str, Path]] = None,
        output_target: Optional[Union[str, Path]] = None,
        stats_output: Optional[Union[str, Path]] = None,
        filtered_source: Optional[Union[str, Path]] = None,
        filtered_target: Optional[Union[str, Path]] = None,
        json_output: Optional[Union[str, Path]] = None,
        instruction: Optional[str] = None,
    ) -> Tuple[int, int]:
        """
        Clean parallel text files and save results.

        Args:
            source_file: Input source language file path
            target_file: Input target language file path
            output_source: Output path for cleaned source text
            output_target: Output path for cleaned target text
            stats_output: Optional path to save cleaning statistics
            filtered_source: Optional path to save filtered source text
            filtered_target: Optional path to save filtered target text
            json_output: Optional path to save cleaned data as JSON
            instruction: Optional instruction to include in JSON output

        Returns:
            Tuple of (original count, cleaned count)
        """
        # Default output file paths if not provided
        if output_source is None:
            source_path = Path(source_file)
            output_source = source_path.parent / f"clean_{source_path.name}"

        if output_target is None:
            target_path = Path(target_file)
            output_target = target_path.parent / f"clean_{target_path.name}"

        return self.clean_file(
            source_file=str(source_file),
            target_file=str(target_file),
            output_source=str(output_source),
            output_target=str(output_target),
            stats_output=str(stats_output) if stats_output else None,
            filtered_source=str(filtered_source) if filtered_source else None,
            filtered_target=str(filtered_target) if filtered_target else None,
            json_output=str(json_output) if json_output else None,
            instruction=instruction,
        )

    def get_stats(self) -> Dict:
        """Get statistics from the latest cleaning operation."""
        return self.cleaner.stats.to_dict()


# Export public classes and functions
__all__ = [
    "TextCleaner",
    "ParallelTextCleaner",
    "CleaningConfig",
    "CleaningStats",
    "KiwiQualityFilter",
    "Filter",
    "BasicCleaningFilter",
    "LengthOutlierFilter",
    "DomainOutlierFilter",
    "QualityFilter",
]

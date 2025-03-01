"""C3PO: Corpus Cleaning and Processing Operations.

A Python library for cleaning and processing parallel text datasets,
particularly useful for machine translation and other NLP tasks.
"""

__version__ = "0.1.0"

from c3po.cleaning import ParallelTextCleaner, CleaningConfig

__all__ = ['ParallelTextCleaner', 'CleaningConfig']

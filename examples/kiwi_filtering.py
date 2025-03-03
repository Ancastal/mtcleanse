#!/usr/bin/env python3
"""Minimal example demonstrating CometKiwi quality filtering for parallel corpora."""

import json
from pathlib import Path

from mtcleanse.cleaning import CleaningConfig, TextCleaner
from mtcleanse.utils import get_console

console = get_console()

# Input/output paths
input_file = "filtered_biomedical.json"
output_dir = Path("cleaned")
output_dir.mkdir(exist_ok=True)

# Load data
console.print("[bold]Loading data[/]")
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)
source_texts = [item["source"] for item in data]
target_texts = [item["target"] for item in data]
console.print(f"Loaded {len(source_texts)} translation pairs")

# Configure and run quality filtering
console.print("[bold]Running quality filtering[/]")
config = CleaningConfig(
    # Disable other filters
    min_chars=1,
    max_chars=100000,
    min_words=1,
    max_words=100000,
    enable_domain_filtering=False,
    # Enable only quality filtering
    enable_quality_filtering=True,
    quality_threshold=0.5,
)

cleaner = TextCleaner(config)
cleaned_source, cleaned_target = cleaner.clean_parallel_texts(
    source_texts, target_texts
)

# Save filtered pairs
source_output = output_dir / "filtered.src"
target_output = output_dir / "filtered.tgt"

with open(source_output, "w", encoding="utf-8") as f:
    f.write("\n".join(cleaned_source))
with open(target_output, "w", encoding="utf-8") as f:
    f.write("\n".join(cleaned_target))

# Print summary
console.print("\n[bold green]Filtering completed![/]")
console.print(f"Original pairs: {len(source_texts)}")
console.print(f"Filtered pairs: {len(cleaned_source)}")
console.print(f"Reduction: {(1 - len(cleaned_source)/len(source_texts))*100:.1f}%")
console.print(f"\nOutput files saved to:\n{source_output}\n{target_output}")

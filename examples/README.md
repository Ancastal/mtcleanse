# MTCleanse Examples

This directory contains example scripts that demonstrate how to use the MTCleanse library for parallel corpus cleaning.

## Quality Filtering with CometKiwi

The [`kiwi_filtering.py`](kiwi_filtering.py) script demonstrates how to use CometKiwi quality filtering to clean a parallel corpus. This approach doesn't require reference translations and provides a reliable way to filter out low-quality translation pairs.

### Requirements

To use the quality filtering example, you need to install the CometKiwi dependencies:

```bash
pip install mtcleanse[quality]
```

Or install the COMET package directly:

```bash
pip install unbabel-comet>=2.0.0
```

### Usage

Basic usage example:

```bash
python kiwi_filtering.py --source data/en.txt --target data/de.txt --output-dir cleaned_data --quality-threshold 0.5
```

### Command-line Arguments

The script supports the following arguments:

- `--source`, `-s`: Path to source language file (required)
- `--target`, `-t`: Path to target language file (required)
- `--output-dir`, `-o`: Directory to save cleaned files (default: "cleaned")
- `--quality-threshold`, `-q`: Quality threshold in range 0-1, higher values mean better quality (default: 0.5)
- `--source-lang`: Source language code (default: "en")
- `--target-lang`: Target language code, use "xx" for auto-detection (default: "xx")
- `--batch-size`, `-b`: Batch size for quality prediction (default: 8)
- `--save-scores`: Save quality scores to a CSV file (flag)

### Output Files

The script produces the following output files:

- `quality_clean_{source_file}`: Cleaned source file
- `quality_clean_{target_file}`: Cleaned target file
- `quality_filtered_{source_file}`: Filtered out source segments
- `quality_filtered_{target_file}`: Filtered out target segments
- `quality_stats.json`: Statistics about the cleaning process
- `quality_scores.csv`: CSV file with quality scores (if `--save-scores` is used)

### Example Output

The script will print information about the cleaning process, including:

- Quality statistics (mean, median, min, max, etc.)
- Number of pairs kept and filtered
- Examples of filtered pairs

Example command to clean an English-Spanish parallel corpus:

```bash
python kiwi_filtering.py \
    --source data/newstest.en \
    --target data/newstest.es \
    --output-dir cleaned \
    --quality-threshold 0.6 \
    --source-lang en \
    --target-lang es \
    --batch-size 16 \
    --save-scores
```

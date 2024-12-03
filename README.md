# Kurdish-Dataset

This repository aims to be a comprehensive dataset written in the Kurdish language, sourced from various materials. The resulting dataset will facilitate diverse studies on the Kurdish language.

## Repository Contents

### Data Directory
The `data` folder is the main container for dataset-related files. It is organized into three subfolders:

- **data_files**: Contains data tables (e.g., PDFs) to be added to the dataset.
- **raw**: Serves as a backup folder. It includes:
  - `raw_kurmanji.txt`: Stores unprocessed text extracted using the `PDFTextExtractor` from `pdf_to_text.py`. This file is used for manual review and corrections before processing.
- **processed**: The final output folder, containing:
  - `kurmanji.txt`: The plain text file of the final dataset.
  - `kurmanji.json`: The JSON representation of the final dataset, automatically populated with the following fields:
    - `file_name`: The source file name.
    - `char_count`: The character count of the text.
    - `word_count`: The word count of the text.
    - `text`: The actual text content.

### Scripts Directory
The `scripts` folder contains:
- **pdf_to_text.py**: A script to convert PDF files to text.

### Main Script
`main.py` is the primary Python script, enabling streamlined data integration without dealing directly with intermediate processing scripts. Below is an example usage:

```python
from scripts.pdf_to_text import PDFTextExtractor

# Converts the PDF file to text and transfers it to data/raw/raw_kurmanji.txt for manual review.
pdftextextractor = PDFTextExtractor("data/data_files/file_name.pdf")

# After manual review, the final data is transferred to kurmanji.txt and kurmanji.json.
pdftextextractor.append_raw_to_processed_data()
```

## Data Integration Workflow
1. Add the desired file to the `data/data_files` directory.
2. Use the `PDFTextExtractor` class to extract raw text:
   ```python
   pdftextextractor = PDFTextExtractor("data/data_files/file_name.pdf")
   ```
   The extracted text will be saved in `data/raw/raw_kurmanji.txt` for manual review.
3. Manually review and correct the contents of `data/raw/raw_kurmanji.txt`.
4. Transfer the reviewed data to the processed files:
   ```python
   pdftextextractor.append_raw_to_processed_data()
   ```
   The reviewed data will be appended to `data/processed/kurmanji.txt` and `data/processed/kurmanji.json`.

### Customizing Page Ranges
The `PDFTextExtractor` class supports two optional parameters: `start_page` and `end_page`. These parameters allow users to specify the range of pages to extract text from a PDF. By default, both parameters are `None`, meaning the entire PDF is processed. To process specific pages, specify the range as shown below:

```python
pdftextextractor = PDFTextExtractor("data/data_files/file_name.pdf", start_page=1, end_page=5)
```
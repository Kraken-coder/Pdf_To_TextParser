
# PdfReader

## Overview
`PdfReader` is a Python class that converts PDF files into readable markdown text using OCR and a large language model (LLM) to improve the extracted text. It utilizes the `easyocr` library for optical character recognition and `fitz` (PyMuPDF) for handling PDF files. The output is processed by the specified LLM to enhance readability and structure (Best Suited for Non searchable PDFs).

## Features
- Converts PDF pages to images and performs OCR on each page.
- Uses a specified large language model to refine and format the extracted text.
- Outputs the processed text to a markdown file.

## Requirements
- Python 3.x
- `easyocr`
- `PyMuPDF` (fitz)
- `llama_index` for LLM support

## Installation
Install the required Python packages using pip:
```sh
pip install easyocr pymupdf llama_index
```

## Usage
1. Import the `PdfReader` class.
2. Instantiate the class with the PDF path, output folder, and other optional parameters.
3. Call the `pdf_to_markdowntxt` method to process the PDF.

### Example
```python
from pdf_reader import PdfReader

# Path to the PDF file
pdf_path = "path/to/your/document.pdf"

# Directory where the output will be saved
output_folder = "path/to/output/directory"

# Instantiate PdfReader
reader = PdfReader(pdf_path, output_folder, llm='llama3', timeout=60, language='en')

# Convert PDF to markdown text
reader.pdf_to_markdowntxt(dpi=300)
```

## Parameters
- `pdf_path` (str): Path to the PDF file.
- `output_fold` (str): Directory where the output files will be saved.
- `llm` (str, optional): Large language model to use for text processing. Default is `'llama3'`.
- `timeout` (int, optional): Timeout for the LLM request in seconds. Default is `60`.
- `language` (str, optional): Language for OCR. Default is `'en'`.

## Methods
### `perform_OCR(output_path)`
Performs OCR on the provided image file and appends the extracted text to the class variable `self.paragraph`.

### `pdf_to_markdowntxt(dpi=300)`
Converts the PDF to images, performs OCR, and processes the text using the specified LLM. Saves the output as a markdown file.

### `llm_parse(text)`
Uses the specified LLM to refine and format the extracted text.

## Notes
- Ensure that the `output_fold` directory exists before running the script.
- The quality of OCR results may vary based on the quality and content of the PDF file.

## License
This project is licensed under the MIT License.

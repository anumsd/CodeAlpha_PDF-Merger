# CodeAlpha_PDF-Merger
This Python project is a powerful PDF merging tool that allows users to combine multiple PDF files into a single document with added features such as:

- **Custom Page Range Selection**: Choose specific page ranges from each PDF to merge only the parts you need.
- **Merge into an Existing PDF**: Optionally merge new files into an existing PDF document.
- **Simple User Input**: The tool prompts users to input file paths, page ranges, and output options directly through the command line, making it highly user-friendly.

## Features
1. **Merge PDFs**: Combines two or more PDFs into one, while allowing specific page ranges to be merged.
2. **Merge with Existing PDF**: Supports merging files into an already existing PDF.
3. **Custom Page Ranges**: Users can specify start and end pages for each PDF file (1-indexed for user convenience).

## How It Works
- Prompts the user to enter the paths of the PDF files to be merged.
- Optionally asks for custom page ranges (start and end pages) for each file.
- Outputs the final merged PDF to a specified location.
- Option to merge the content into an existing PDF document if provided.

## Requirements
- Python 3.x
- `pypdf` library

Install the required library using pip:
```
pip install pypdf
```

## Usage

### Example:
```bash
Enter path for file 1: C:/Users/User/Documents/file1.pdf
Enter path for file 2: C:/Users/User/Documents/file2.pdf
Do you want to specify page ranges? (Y/N): Y

For file: C:/Users/User/Documents/file1.pdf
Enter the start page (1-indexed): 1
Enter the end page (inclusive, 1-indexed): 3

For file: C:/Users/User/Documents/file2.pdf
Enter the start page (1-indexed): 2
Enter the end page (inclusive, 1-indexed): 5

Enter the output path for the merged PDF: C:/Users/User/Documents/merged_output.pdf
```

The program will then merge the specified pages and save the output PDF at the chosen location.

## License
This project is licensed under the MIT License.

---

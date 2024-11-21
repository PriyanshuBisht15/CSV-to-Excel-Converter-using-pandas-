# CSV-to-Excel-Converter-using-pandas-
This script allows you to convert CSV files into Excel format in bulk. It reads multiple CSV files, converts each into an Excel file (.xlsx), and saves them in a specified output directory.

## Features:
1. Converts CSV files to Excel format.
2. Handles multiple CSV files in a batch.
3. Automatically creates the output directory if it doesn't exist.
4. Provides error handling for common issues:
- File not found.
- Empty CSV file.
- Unexpected errors.

## Prerequisites
1. Python: Ensure Python is installed on your system. You can download it from python.org.
2. Pandas library: Install the Pandas library if not already installed. You can install it using pip:
pip install pandas

## How to Use
1. Save the script: Copy the provided code and save it as csv_to_excel_converter.py.

2. Run the script: Execute the script using the command:
   python csv_to_excel_converter.py

3. Provide inputs:
- When prompted, enter a comma-separated list of CSV file paths you want to convert. Example:
   Enter comma-separated CSV file paths: file1.csv, file2.csv, path/to/file3.csv
- Specify the output directory for the converted Excel files. The script will create the directory if it doesn’t already exist. Example:
  Enter the output directory for Excel files: output_excel_files

4. View results: The converted Excel files will be saved in the specified output directory with the same base filenames as the original CSV files.

## Error Handling
- File Not Found: If a specified CSV file does not exist, an error message will be displayed, and the script will continue processing other files.
- Empty CSV File: If a CSV file is empty, a warning message will be displayed.
- Unexpected Errors: Any other errors will be logged with details for debugging.



## Requirements
- Python 3.x
- Required library: pandas


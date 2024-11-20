import pandas as pd
import os

def csv_to_excel(csv_file, excel_file):
    try:
        df = pd.read_csv(csv_file)
        df.to_excel(excel_file, index=False)
        print(f"Converted '{csv_file}' to '{excel_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def batch_convert_csv_to_excel():
    csv_files = input("Enter comma-separated CSV file paths: ").split(',')
    output_dir = input("Enter the output directory for Excel files: ")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for csv_file in csv_files:
        csv_file = csv_file.strip()
        excel_file = os.path.join(output_dir, os.path.basename(csv_file).replace('.csv', '.xlsx'))
        csv_to_excel(csv_file, excel_file)

if __name__ == "__main__":
    batch_convert_csv_to_excel()

import pandas as pd

def convert_excel_to_csv(excel_filepath, csv_filepath, sheet_name=0):
    """
    Converts an Excel file (xlsx or xls) to a CSV file without opening it.

    Args:
        excel_filepath (str): Path to the Excel file.
        csv_filepath (str): Path to save the resulting CSV file.
        sheet_name (int or str, optional): Sheet to convert. Defaults to 0 (first sheet).
    """
    try:
        df = pd.read_excel(excel_filepath, sheet_name=sheet_name)
        df.to_csv(csv_filepath, index=False, encoding='utf-8')
        print(f"Successfully converted '{excel_filepath}' to '{csv_filepath}'")
    except FileNotFoundError:
        print(f"Error: Excel file '{excel_filepath}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
report_base_path='/Users/tedspecht/Downloads/'
report_file = 'report(1).xls'
path_to_report = report_base_path + report_file
csv_file = 'thia_csv_input_file.csv'
convert_excel_to_csv(path_to_report, csv_file)

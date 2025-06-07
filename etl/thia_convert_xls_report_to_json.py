import pandas as pd
import json

def excel_to_json(excel_filepath, json_filepath, orient='records'):
    """
    Converts an Excel file to JSON.

    Args:
        excel_filepath (str): Path to the Excel file.
        json_filepath (str): Path to save the JSON file.
        orient (str, optional): Format of the JSON data. 
                               Defaults to 'records'.
                               Other options include 'index', 'columns', 'values', 'table'.
    """
    try:
        df = pd.read_excel(excel_filepath)
        json_data = df.to_json(orient=orient, indent=4)

        with open(json_filepath, 'w') as f:
            f.write(json_data)
        print(f"Successfully converted '{excel_filepath}' to '{json_filepath}'")
    except FileNotFoundError:
         print(f"Error: Excel file not found at '{excel_filepath}'")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
report_base_path='/Users/tedspecht/Downloads/'
report_file = 'report(1).xls'
path_to_report = report_base_path + report_file
json_file = 'my_json_file.json'
excel_to_json(path_to_report, json_file)

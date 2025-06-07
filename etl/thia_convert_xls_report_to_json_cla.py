import pandas as pd
import json
import argparse


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

# retrieve options from command line parameters
parser = argparse.ArgumentParser("thia_convert_xls_report_to_json_cla")
parser.add_argument("-inf", help="input file path", type=str)
parser.add_argument("-out", help="output file path", type=str)
args = parser.parse_args()

excel_to_json(args.inf, args.out)

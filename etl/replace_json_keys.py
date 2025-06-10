import sys
import json
import yaml
from json.decoder import JSONDecodeError
import argparse

# This script reads a JSON file, replaces specific key names according to a mapping,
# and writes the modified JSON to a new file. 
# It also reads a YAML configuration file for additional settings
def read_yaml_config(config_file_path):
    # Reads a YAML configuration file and returns a dictionary.
    try:
        with open(config_file_path, 'r') as file:
            config = yaml.safe_load(file)
            return config
    except FileNotFoundError:
        print(f"Error: Config File not found at {config_file_path}")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML Config file: {e}")
        return None



def read_json_input_file(jin):
      with open(jin, 'r') as file:
         try:
             json_data = json.load(file)
             return json_data
         except JSONDecodeError as e:
             print(f"read_json_input_file\nJSONDecodeError: {e}")
             print(f"Error at position: {e.pos}")
             print(f"Line number: {e.lineno}, Column number: {e.colno}")
             return None
         except Exception as e:
             print(f"read_json_input_file\nAn unexpected error occurred: {e}")
             return None

def replace_key_name(json_data, name_mapping):
    count = 1
    updated_json = []
    for dictionary in json_data:

        new_data = {}
        for key, value in dictionary.items():
            new_key = name_mapping.get(key, key)
            new_data[new_key] = value
        updated_json.append(new_data)
        count += 1
    #print(f"updated json : {updated_json}, count {count}")
    return updated_json

def write_modified_json(output_file_path, modified_json):
    try:
        with open(output_file_path, 'w') as of:
            json.dump(modified_json, of, indent=4)
    except PermissionError:
        print(f"Error: Permission denied to write to {output_file_path}")
    except Exception as e:
       print(f"Exception occurred : {e}")



# retrieve parameters from command line options
parser = argparse.ArgumentParser("replace_json_keys")
parser.add_argument("-in", "--jin", help="input json file path", type=str, required=True)
parser.add_argument("-out", "--jout", help="output json file path", type=str, required=True)
parser.add_argument("-y", "--yaml", help="yaml configuration file path", type=str, required=True)

args = parser.parse_args()

config_data = read_yaml_config(args.yaml)
if config_data is None:
    sys.exit(1)
else:
    # Access CSV header name key value pairs:
    csv_header_names = config_data.get("csv_header_name_mapping", {})
    print(f"CSV Header Names Mapping: {csv_header_names}")

    # read the json file from ivolunteer
    json_data = read_json_input_file(args.jin)
    if json_data is None:
        sys.exit(1)
    else:
        # replace key names 
        modified_json = replace_key_name(json_data, csv_header_names)
        print(f"\n\n\n\nmodified json : {modified_json} ")
        # write modified json
        write_modified_json(args.jout, modified_json)


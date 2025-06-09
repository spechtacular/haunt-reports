import sys
import json
from json.decoder import JSONDecodeError
import argparse

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

# map key names passed from ivolunteer to proper json key names
name_mapping = {'Unnamed: 0': 'id', 'F.Name': 'first_name', 'L.Name' : 'last_name', 'E-Mail' : 'email' }

# retrieve parameters from command line options
parser = argparse.ArgumentParser("replace_json_keys")
parser.add_argument("-in", "--jin", help="input json file path", type=str, required=True)
parser.add_argument("-out", "--jout", help="output json file path", type=str, required=True)
args = parser.parse_args()

# read the json file from ivolunteer
json_data = read_json_input_file(args.jin)
if json_data is None:
   sys.exit(1)
else:
   # replace key names 
   modified_json = replace_key_name(json_data, name_mapping)
   print(f"\n\n\n\nmodified json : {modified_json} ")
   # write modified json
   write_modified_json(args.jout, modified_json)


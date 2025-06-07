import yaml
import argparse

def read_yaml_config(file_path):
    # Reads a YAML configuration file and returns a dictionary.
    try:
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
            return config
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None


# used to define scope
#if __name__ == "__main__":

# retrieve configuration file from command line options
parser = argparse.ArgumentParser("read_configuration")
parser.add_argument("-y", "--yaml", help="yaml configuration file path", type=str, required=True)
args = parser.parse_args()

config_file_path = args.yaml
config_data = read_yaml_config(config_file_path)
    
if config_data:
    print("Configuration data:")
    print(config_data)
    # Access specific values:
    database_host = config_data.get("database", {}).get("host")
    print(f"Database host: {database_host}")

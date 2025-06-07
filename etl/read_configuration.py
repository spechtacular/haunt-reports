import yaml
import argparse
import logging
import logging.handlers

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
   
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler
file_handler = logging.handlers.RotatingFileHandler('./logs/etl.log', maxBytes=1024, backupCount=5)
file_handler.setLevel(logging.DEBUG)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

 
if config_data:
    logger.debug("Configuration data:")
    logger.debug(config_data)
    # Access specific values:
    database_host = config_data.get("database", {}).get("host")
    logger.debug(f"Database host: {database_host}")

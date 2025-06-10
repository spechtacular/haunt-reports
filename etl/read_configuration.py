import yaml
import argparse
import logging
import platform
import sys

class HostnameFilter(logging.Filter):
        hostname = platform.node()

        def filter(self, record):
            record.hostname = HostnameFilter.hostname
            return True

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

   
# logging experiment

# Create a file rotation handler
#file_handler = logging.handlers.RotatingFileHandler('./logs/etl.log', maxBytes=1024, backupCount=5)
#file_handler.setLevel(logging.DEBUG)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.addFilter(HostnameFilter())

# Create a formatter
formatter = logging.Formatter('%(hostname)s %(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Create a logger   
logger = logging.getLogger('etl_logger')
# Add handlers to logger
#logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)



config_data = read_yaml_config(args.yaml)

if config_data is None:
    sys.exit(1)
else:
    logger.debug("Configuration data:")
    logger.debug(config_data)
    # Access specific values:
    database_host = config_data.get("database", {}).get("host")
    logger.debug(f"Database host: {database_host}")
    csv_header_names = config_data.get("csv_header_name_mapping", {})
    logger.debug(f"CSV Header names: {csv_header_names}")

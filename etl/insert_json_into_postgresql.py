import json
###########################################################################
# Using context managers (with statement) to automatically manage resources, 
# including database connections. This ensures that connections are closed 
# correctly, even when errors occur.
###########################################################################
from json.decoder import JSONDecodeError

import psycopg2
from psycopg2 import Error

import logging

def read_json_input_file(jin):
      with open(jin, 'r') as file:
         try:
             json_data = json.load(file)
             return json_data
         except JSONDecodeError as e:
             logging.error("read_json_input_file:JSONDecodeError: %s", e)
             return None
         except Exception as e:
             logging.error("read_json_input_file:Exception: %s", e)
             return None

# initialize logging
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


try:
    with psycopg2.connect(host="localhost", 
               database="thia", 
               user="ghoul", 
               password="NotHalloween2024") 
         as connection:

         with connection.cursor() as cursor:

             cursor.execute("""
                CREATE TABLE IF NOT EXISTS test_thia (
                    id SERIAL PRIMARY KEY,
                    data jsonb
                )
              """)


             insert_sql = """
                INSERT INTO your_table (data)
                SELECT * FROM json_populate_recordset(null::your_table, %s)
            """
            cursor.execute(insert_sql, (json.dumps(data),))
            conn.commit()

except (Exception, Error) as error:
    logging.error("Error while connecting to PostgreSQL: %s", error)


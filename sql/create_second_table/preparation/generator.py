import os
import sqlite3
import sys
from sqlite3 import OperationalError

import pandas as pd

"""
Make database based on the previous solution (overwrites existing database).
After creation, contents and schema of newly created database is printed.
"""

MIN_PYTHON = (3, 9)
if sys.version_info < MIN_PYTHON:
    sys.exit(f"Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]} or later is required.\n")


def execute_sql_from_file(filename: str):
    with open(filename, 'r') as fd:
        sql_file = fd.read()

    sql_commands = sql_file.split(';')

    for command in sql_commands:
        try:
            cursor.execute(command)
        except OperationalError as msg:
            print("Command skipped: ", msg)


db_filename = "../evaluation/maxdb.sqlite"

if os.path.exists(db_filename):
    os.remove(db_filename)

connection = sqlite3.connect(db_filename)
cursor = connection.cursor()

execute_sql_from_file("previous_solution.sql")

table_name = "STORES"

print(pd.read_sql(f"SELECT * FROM {table_name};", connection))
print(pd.read_sql(f"PRAGMA TABLE_INFO({table_name});", connection))

connection.commit()
connection.close()

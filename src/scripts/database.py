import sys
import os
import inspect

CURRENT_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.insert(0, PARENT_DIR + "/database")
from connection import Connector
from sql.data import SQL_INSERT_DATA

if len(sys.argv) > 1:
    if os.environ.get("ENVIRONMENT") == "production":
        print("This script is not allowed in production environment.")
        sys.exit(1)

    if "--delete" in sys.argv:
        connection = Connector()
        connection.cursor.execute("DROP DATABASE IF EXISTS mymoney;")
        connection.cursor.execute("CREATE DATABASE mymoney;")
        connection.close()

    if "--create" in sys.argv:
        connection = Connector()
        with open("./src/database/sql/tables.sql") as f:
            connection.cursor.execute(f.read(), multi=True)
        connection.close()

        connection = Connector()
        with open("./src/database/sql/procedures.sql") as f:
            connection.cursor.execute(f.read(), multi=True)
        connection.close()

    if "--insert" in sys.argv:
        connection = Connector()
        for key in SQL_INSERT_DATA:
            for value in SQL_INSERT_DATA[key]["values"]:
                # print(SQL_INSERT_DATA[key]["sql"] % value)
                connection.cursor.execute(SQL_INSERT_DATA[key]["sql"], value)
            connection.commit()
        connection.close()


else:
    print("Usage: python src/scripts/database.py [--delete] [--create] [--insert]")
    sys.exit(1)

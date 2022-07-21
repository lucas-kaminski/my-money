import sys
import os
import inspect

CURRENT_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.insert(0, PARENT_DIR + "/database")
from connection import Connector

if len(sys.argv) > 1:
    sql = {
        "USERS": [
            'INSERT INTO users (ID, USERNAME, PASSWORD, EMAIL, CREATED_AT, UPDATED_AT) VALUES (1, "admin", "admin", "admin@admin.com", NOW(), NOW())'
        ],
        "TYPES_ENTRIES_CATEGORIES": [
            'INSERT INTO type_entries_categories (ID, NAME) VALUES (1, "Food")',
            'INSERT INTO type_entries_categories (ID, NAME) VALUES (2, "Drink")',
            'INSERT INTO type_entries_categories (ID, NAME) VALUES (3, "Other")',
        ],
        "TYPES_PIX_KEYS": [
            'INSERT INTO type_pix_keys (ID, TYPE) VALUES (1, "CPF")',
            'INSERT INTO type_pix_keys (ID, TYPE) VALUES (2, "CNPJ")',
            'INSERT INTO type_pix_keys (ID, TYPE) VALUES (3, "E-mail")',
            'INSERT INTO type_pix_keys (ID, TYPE) VALUES (4, "Telefone")',
        ],
        "PIX": [
            'INSERT INTO pix (ID, ID_KEY_TYPE, ID_USER, `KEY`) VALUES (1, 1, 1, "TESTE")',
        ],
        "BANKS": [
            'INSERT INTO banks (ID, ID_USER, ID_PIX, NAME, AGENCY, ACCOUNT, OBSERVATION ) VALUES (1, 1, 1, "Banco do Brasil", "1234", "123456789", "Script from database.py")'
        ],
        "ENTRIES": [
            'INSERT INTO entries (ID, ID_BANK, ID_CATEGORY_TYPE, DATE, VALUE, OBSERVATION) VALUES (1, 1, 1, CURRENT_DATE(), 100.00, "Script from database.py")'
        ],
    }

    # if args contains --delete
    if "--delete" in sys.argv:
        connection = Connector()
        with open("./src/database/sql/drop.sql", "r") as f:
            connection.cursor.execute(f.read())
            print("Database recreated")

    if "--create" in sys.argv:
        connection = Connector()
        with open("./src/database/sql/tables.sql") as f:
            for i in connection.cursor.execute(f.read(), multi=True):
                pass

        with open("./src/database/sql/procedures.sql") as f:
            for i in connection.cursor.execute(f.read(), multi=True):
                pass

    if "--insert" in sys.argv:
        for key in sql:
            for i in sql[key]:
              connection.cursor.execute(i)
        connection.commit()
        print("Data inserted")


else:
    print("Usage: python3 seed.py [--delete|--create]")
    sys.exit(1)

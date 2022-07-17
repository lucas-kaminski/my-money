import sys
import os
import inspect

CURRENT_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.insert(0, PARENT_DIR + '/database')
from connection import Connector

if len(sys.argv) > 1:
  INSERT_USERS = False
  # if args contains --delete
  if '--delete' in sys.argv:
    connection = Connector()
    with open('./src/database/sql/drop.sql', 'r') as f:
      connection.cursor.execute(f.read())

  if '--create' in sys.argv:
    connection = Connector()
    with open('./src/database/sql/tables/users.sql') as f:
      connection.cursor.execute(f.read())
      if '--insert' in sys.argv:
        INSERT_USERS = True

  if INSERT_USERS:
    connection = Connector()
    connection.cursor.execute('INSERT INTO users (ID, USERNAME, PASSWORD, EMAIL, CREATED_AT, UPDATED_AT) VALUES (1, "admin", "admin", "admin@admin.com", NOW(), NOW())')
    connection.commit()

else:
  print('Usage: python3 seed.py [--delete|--create]')
  sys.exit(1)




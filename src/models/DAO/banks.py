from database.connection import Connector

def getNameOfBank(bank_id):
  connection = Connector()
  connection.cursor.execute('SELECT NAME FROM banks WHERE id = %s', (bank_id,))
  db_bank = connection.cursor.fetchone()
  if db_bank is None:
    return None
  return db_bank['NAME']
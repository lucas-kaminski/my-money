from database.connection import Connector

def getNameOfCategory(category_id):
  connection = Connector()
  connection.cursor.execute('SELECT NAME FROM type_entries_categories WHERE id = %s', (category_id,))
  db_category = connection.cursor.fetchone()
  if db_category is None:
    return None
  return db_category['NAME']

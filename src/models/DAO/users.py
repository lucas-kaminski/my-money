from database.connection import Connector
from models.user import User

def getByEmail(email) -> User or None:
  connection = Connector()
  connection.cursor.execute('SELECT * FROM users WHERE EMAIL = %s', (email,))
  user = connection.cursor.fetchone()
  print(user)
  return User(**user) if user else None


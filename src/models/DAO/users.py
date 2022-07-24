from database.connection import Connector
from models.user import User


def getByID(id) -> User or None:
    connection = Connector()
    connection.cursor.execute("SELECT * FROM users WHERE ID = %s", (id,))
    user = connection.cursor.fetchone()
    return User(**user) if user else None


def getByEmail(email) -> User or None:
    connection = Connector()
    connection.cursor.execute("SELECT * FROM users WHERE EMAIL = %s", (email,))
    user = connection.cursor.fetchone()
    return User(**user) if user else None

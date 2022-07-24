import os
import mysql.connector

config = {
    "user": os.environ.get("MYSQL_USER"),
    "password": os.environ.get("MYSQL_PASSWORD"),
    "host": os.environ.get("MYSQL_HOST"),
    "port": os.environ.get("MYSQL_PORT"),
    "database": os.environ.get("MYSQL_DATABASE"),
    "raise_on_warnings": True,
}


class Connector:
    def __init__(self):
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor(dictionary=True)

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()

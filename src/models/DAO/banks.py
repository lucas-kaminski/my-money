from database.connection import Connector
from models.banks import Bank


def getNameOfBank(bank_id):
    connection = Connector()
    connection.cursor.execute("SELECT NAME FROM banks WHERE id = %s", (bank_id,))
    db_bank = connection.cursor.fetchone()
    if db_bank is None:
        return None
    return db_bank["NAME"]


def getAllBanksOfUser(user_id):
    connection = Connector()
    connection.cursor.execute("SELECT * FROM banks WHERE ID_USER = %s", (user_id,))
    db_banks = connection.cursor.fetchall()
    if db_banks is None:
        return None
    return [Bank(**bank) for bank in db_banks]

from database.connection import Connector
from models.entries import Entry

from models.DAO.banks import getNameOfBank
from models.DAO.types.entries_categories import getNameOfCategory


def getAllEntriesOfUser(user_id) -> list:
    connection = Connector()
    connection.cursor.execute("CALL getAllEntriesOfUser(%s)", (user_id,))
    db_entries = connection.cursor.fetchall()
    entries = []

    for entry in db_entries:
        entries.append(
            Entry(
                **entry,
                BANK_NAME=getNameOfBank(entry["ID_BANK"]),
                CATEGORY_NAME=getNameOfCategory(entry["ID_CATEGORY_TYPE"])
            )
        )

    return entries

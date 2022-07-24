from datetime import datetime


class Entry:
    id: int
    id_bank: int
    id_category_type: int
    date: datetime
    value: float
    observation: str
    created_at: datetime
    updated_at: datetime
    bank_name: str
    category_name: str

    def __init__(
        self,
        ID,
        ID_BANK,
        ID_CATEGORY_TYPE,
        DATE,
        VALUE,
        OBSERVATION,
        CREATED_AT,
        UPDATED_AT,
        BANK_NAME=None,
        CATEGORY_NAME=None,
    ):
        self.id = ID
        self.id_bank = ID_BANK
        self.id_category_type = ID_CATEGORY_TYPE
        self.date = DATE
        self.value = VALUE
        self.observation = OBSERVATION
        self.created_at = CREATED_AT
        self.updated_at = UPDATED_AT
        self.bank_name = BANK_NAME
        self.category_name = CATEGORY_NAME

    def getBankName(self):
        return self.bank_name

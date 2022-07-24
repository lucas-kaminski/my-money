class Pix:
    id: int
    id_key: int
    id_bank: int
    key: str

    def __init__(self, ID, ID_KEY_TYPE, ID_BANK, KEY):
        self.id = ID
        self.id_key_type = ID_KEY_TYPE
        self.id_user = ID_BANK
        self.key = KEY

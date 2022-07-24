class Bank:
    id: int
    id_user: int
    name: str
    agency: str
    account: str
    observation: str

    def __init__(self, ID, ID_USER, NAME, AGENCY, ACCOUNT, OBSERVATION):
        self.id = ID
        self.id_user = ID_USER
        self.name = NAME
        self.agency = AGENCY
        self.account = ACCOUNT
        self.observation = OBSERVATION

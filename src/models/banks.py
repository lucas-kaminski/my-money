class Bank:
  id: int
  id_user: int
  id_pix: int
  name: str
  agency: str
  account: str
  observation: str

  def __init__(self, ID, ID_USER, ID_PIX, NAME, AGENCY, ACCOUNT, OBSERVATION):
    self.id = ID
    self.id_user = ID_USER
    self.id_pix = ID_PIX
    self.name = NAME
    self.agency = AGENCY
    self.account = ACCOUNT
    self.observation = OBSERVATION
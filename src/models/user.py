class User:
  id: int
  username: str
  password: str
  email: str
  created_at: str
  updated_at: str

  def __init__(self, ID, USERNAME, PASSWORD, EMAIL, CREATED_AT, UPDATED_AT):
    self.id = ID
    self.username = USERNAME
    self.password = PASSWORD
    self.email = EMAIL
    self.created_at = CREATED_AT
    self.updated_at = UPDATED_AT

  def isValidPassword(self, password):
    return self.password == password
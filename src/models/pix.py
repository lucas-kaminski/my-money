class Pix:
  id: int
  id_key: int
  id_user: int
  key: str

  def __init__(self, ID, ID_KEY_TYPE, ID_USER, KEY):
    self.id = ID
    self.id_key_type = ID_KEY_TYPE
    self.id_user = ID_USER
    self.key = KEY
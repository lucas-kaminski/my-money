from datetime import datetime

class Entrie:
  id: int
  id_bank: int
  id_category: int
  date: datetime
  value: float
  observation: str
  created_at: datetime
  updated_at: datetime

  def __init__(self, ID, ID_BANK, ID_CATEGORY, DATE, VALUE, OBSERVATION, CREATED_AT, UPDATED_AT):
    self.id = ID
    self.id_bank = ID_BANK
    self.id_category = ID_CATEGORY
    self.date = DATE
    self.value = VALUE
    self.observation = OBSERVATION
    self.created_at = CREATED_AT
    self.updated_at = UPDATED_AT





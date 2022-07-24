class User:
    id: int
    username: str
    email: str
    created_at: str
    updated_at: str
    _password: str
    _is_authenticated: bool

    def __init__(
        self,
        ID,
        USERNAME,
        PASSWORD,
        EMAIL,
        CREATED_AT,
        UPDATED_AT,
        IS_AUTHENTICATED=False,
    ):
        self.id = ID
        self.username = USERNAME
        self._password = PASSWORD
        self.email = EMAIL
        self.created_at = CREATED_AT
        self.updated_at = UPDATED_AT
        self._is_authenticated = IS_AUTHENTICATED

    def isValidPassword(self, password):
        return self._password == password

    def isAuthenticated(self):
        return self._is_authenticated

    def setIsAuthenticated(self, value: bool):
        self._is_authenticated = value

from src.identities import IIdentity


class TestIdentity(IIdentity):
    _authentication_type: str
    _name: str
    _is_authenticated: bool

    def __init__(self, name: str = '', is_authenticated: bool = False):
        IIdentity.__init__(self)
        self._name = name
        self._is_authenticated = is_authenticated
        self._authentication_type = 'Test'

    @property
    def authentication_type(self):
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, value):
        self._authentication_type = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def is_authenticated(self):
        return self._is_authenticated

    @is_authenticated.setter
    def is_authenticated(self, value):
        self._is_authenticated = value

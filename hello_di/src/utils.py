import os

from src.identities import IIdentity


class MySystem:
    """
    模擬用
    """

    @staticmethod
    def get_identity() -> IIdentity:
        username = os.getenv('USERNAME', default=None) or \
                   os.getenv('USER', default='Anonymous')
        return _GenericIdentity(name=username, is_authenticated=True)


class _GenericIdentity(IIdentity):
    _authentication_type: str
    _name: str
    _is_authenticated: bool

    def __init__(self, name: str, is_authenticated: bool = False):
        IIdentity.__init__(self)
        self._name = name
        self._is_authenticated = is_authenticated
        self._authentication_type = 'Test'

    @property
    def authentication_type(self):
        return self._authentication_type

    @property
    def name(self):
        return self._name

    @property
    def is_authenticated(self):
        return self._is_authenticated

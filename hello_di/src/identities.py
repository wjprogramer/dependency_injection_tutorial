from abc import abstractmethod, ABCMeta


class IIdentity(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @property
    @abstractmethod
    def authentication_type(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def is_authenticated(self):
        pass

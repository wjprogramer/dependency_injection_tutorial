from abc import ABC, abstractmethod

from src.identities import IIdentity


class IMessageWriter(ABC):
    @abstractmethod
    def write(self, message: str) -> None:
        pass


class ConsoleMessageWriter(IMessageWriter):
    def write(self, message: str) -> None:
        print(message)


class SecureMessageWriter(IMessageWriter):
    _writer: IMessageWriter
    _identity: IIdentity

    def __init__(self, writer: IMessageWriter, identity: IIdentity) -> None:
        self._writer = writer
        self._identity = identity

    def write(self, message: str) -> None:
        if self._identity.is_authenticated:
            self._writer.write(message)

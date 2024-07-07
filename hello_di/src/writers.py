from abc import ABC, abstractmethod


class IMessageWriter(ABC):
    @abstractmethod
    def write(self, message: str) -> None:
        pass


class ConsoleMessageWriter(IMessageWriter):
    def write(self, message: str) -> None:
        print(message)

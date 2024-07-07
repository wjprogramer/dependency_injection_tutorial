from src.writers import IMessageWriter


class Salutation:
    _writer: IMessageWriter

    def __init__(self, writer: IMessageWriter) -> None:
        self._writer = writer

    def exclaim(self):
        self._writer.write('Hello DI!')

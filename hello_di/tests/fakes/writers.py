from src.writers import IMessageWriter


class SpyMessageWriter(IMessageWriter):
    _message_count: int = 0
    _written_message: str = ''

    @property
    def message_count(self):
        return self._message_count

    @property
    def written_message(self):
        return self._written_message

    def write(self, message: str) -> None:
        self._written_message += message
        self._message_count += 1

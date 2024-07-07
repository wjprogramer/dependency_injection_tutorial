from src.salutation import Salutation
from tests.fakes.writers import SpyMessageWriter


class TestSalutation:
    def test_exclaim_will_write_correct_message_to_message_writer(self):
        # Arrange
        writer = SpyMessageWriter()
        sut = Salutation(writer)

        # Act
        sut.exclaim()

        # Assert
        assert writer.written_message == 'Hello DI!'

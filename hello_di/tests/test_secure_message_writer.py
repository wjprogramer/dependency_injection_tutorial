from typing import Optional

from src.identities import IIdentity
from src.writers import SecureMessageWriter, IMessageWriter
from tests.fakes.identities import TestIdentity
from tests.fakes.writers import SpyMessageWriter


class TestSecureMessageWriter:
    _authenticated_identity: IIdentity = TestIdentity(is_authenticated=True)
    _anonymous_identity: IIdentity = TestIdentity(is_authenticated=False)

    def test_sut_is_message_writer(self):
        assert issubclass(SecureMessageWriter, IMessageWriter)

    def test_write_invokes_decorated_writer_when_principal_is_authenticated(self):
        # Arrange
        expected_message = 'Whatever'
        writer = SpyMessageWriter()

        sut = self.__create_secure_message_writer(writer, self._authenticated_identity)

        # Act
        sut.write(expected_message)

        # Assert
        assert writer.written_message == expected_message

    def test_write_does_not_invoke_writer_when_principal_is_not_authenticated(self):
        # Arrange
        writer = SpyMessageWriter()

        sut = self.__create_secure_message_writer(writer, self._anonymous_identity)

        # Act
        sut.write('Anonymous value')

        # Assert
        assert writer.message_count == 0

    @staticmethod
    def __create_secure_message_writer(writer: Optional[IMessageWriter],
                                       identity: Optional[IIdentity]) -> SecureMessageWriter:
        return SecureMessageWriter(writer or SpyMessageWriter, identity)

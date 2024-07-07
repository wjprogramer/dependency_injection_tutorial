import configparser
import importlib

from src.salutation import *
from src.utils import *
from src.writers import *


def _early_binding_example():
    writer: IMessageWriter = SecureMessageWriter(
        writer=ConsoleMessageWriter(),
        identity=MySystem.get_identity()
    )
    salutation = Salutation(writer)
    salutation.exclaim()


def _late_binding_example():
    config = configparser.ConfigParser()
    config.read('application.ini')

    module = importlib.import_module('src.writers')
    type_class = getattr(module, config['DEFAULT']['writer'])
    writer_instance: IMessageWriter = type_class()

    writer: IMessageWriter = SecureMessageWriter(
        writer=writer_instance,
        identity=MySystem.get_identity()
    )

    salutation = Salutation(writer)
    salutation.exclaim()


if __name__ == '__main__':
    _early_binding_example()
    _late_binding_example()

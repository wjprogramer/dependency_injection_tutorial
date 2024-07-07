import configparser
import importlib

from src.salutation import *
from src.writers import *


def _late_binding_example():
    config = configparser.ConfigParser()
    config.read('application.ini')

    module = importlib.import_module('src.writers')
    type_class = getattr(module, config['DEFAULT']['writer'])
    writer: IMessageWriter = type_class()

    salutation = Salutation(writer)
    salutation.exclaim()


if __name__ == '__main__':
    _late_binding_example()

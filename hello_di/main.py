from src.salutation import *
from src.writers import *


if __name__ == '__main__':
    writer: IMessageWriter = ConsoleMessageWriter()
    salutation = Salutation(writer)
    salutation.exclaim()

"""
Read DBF files with Python.

Example:

    >>> from dbfread import DBF
    >>> for record in DBF('people.dbf'):
    ...     print(record)
    {'NAME': 'Alice', 'BIRTHDATE': datetime.date(1987, 3, 1)}
    {'NAME': 'Bob', 'BIRTHDATE': datetime.date(1980, 11, 12)}

Full documentation at https://dbfread.readthedocs.io/

"""
__author__ = 'Ole Martin Bjorndalen'
__email__ = 'ombdalen@gmail.com'
__url__ = 'https://dbfread.readthedocs.io/'
__license__ = 'MIT'

from .dbf import DBF
from .deprecated_dbf import open, read
from .exceptions import DBFNotFound, MissingMemoFile
from .field_parser import FieldParser, InvalidValue

# Prevent star import.
__all__ = []

"""
This file contains routines for storing the properties of hexes

When using axial coordinates, we can generate every possible hex coordinate
can be written as a unique linear combination of two bases: a*SE + b*NE,
where a,b are integers.

Since the there is a unique (a,b) for every hex, we can use (a,b) as a key
in a python dictionary to store properties of the hex indexed by (a,b)


Key Rules:
- must be written 'a,b' without quotes
- no spaces
- a and b can be negative, so it is okay if the key is written as
  '-a,b' or 'a,-b' or '-a,-b'
"""


class HexExistsError(Exception):
    def __init__(self, message, errors):
        super(HexExistsError, self).__init__(message)


class IncorrectCoordinatesError(Exception):
    def __init__(self, message, errors):
        super(IncorrectCoordinatesError, self).__init__(message)


class HexMap(dict):
    def __init__(self):
        super(HexMap, self).__init__()

    def __setitem__(self, coordinate, hex_object):
        key = self.make_key_from_coordinate(coordinate)
        if key in dict.keys():
            raise HexExistsError("key " + key + " already exists.")

        self[key] = hex_object

    def make_key_from_coordinate(self, coordinate):
        if len(coordinate) != 2:
            raise IncorrectCoordinatesError(str(coordinate) + " has incorrect length.")

        return str(coordinate[0]) + ',' + str(coordinate[1])

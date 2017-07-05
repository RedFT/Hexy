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
import numpy as np
from util import DIR, cube_to_axial

# The bases of the axial coordinate system
__bases_mat = np.array([cube_to_axial(DIR.SE), cube_to_axial(DIR.E)],
                       dtype=int)


class HexExistsError(Exception):
    def __init__(self, message, errors):
        super(HexExistsError, self).__init__(message)


class IncorrectCoordinatesError(Exception):
    def __init__(self, message, errors):
        super(IncorrectCoordinatesError, self).__init__(message)


class MismatchError(Exception):
    def __init__(self, message, errors):
        super(MismatchError, self).__init__(message)

def make_key_from_indexes(indexes):
    """
    Converts indexes to string for hashing
    :param indexes: the indexes of a hex. nx2, n=number of index pairs
    :return: key for hashing based on index.
    """
    return [str(index[0]) + ',' + str(index[1]) for index in indexes]


def solve_for_indexes(hexes):
    """
    We want to solve for the coefficients in the linear combos.
    :param hexes: The hexes whose indexes we want to solve for.
                  nx2, n=number of hexes
    :return: indexes of `hexes`
    """
    return np.linalg.solve(__bases_mat, hexes.T).T


class HexMap(dict):
    def __init__(self):
        super(HexMap, self).__init__()

    def __setitem__(self, coordinates, hex_objects):
        if len(coordinates) != len(hex_objects):
            raise MismatchError("Number of coordinates does not match number of hex objects.")
        indexes=solve_for_indexes(coordinates)
        keys = make_key_from_indexes(indexes)
        for key, hex in zip(keys, hex_objects):
            if key in dict.keys():
                raise HexExistsError("key " + key + " already exists.")

            self[key] = hex

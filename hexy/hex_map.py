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

from errors import IncorrectCoordinatesError, HexExistsError, MismatchError
from hexy import DIR, cube_to_axial

# The bases of the axial coordinate system
__bases_mat = cube_to_axial(np.array([DIR.SE, DIR.E], dtype=int))


def make_key_from_indexes(indexes):
    """
    Converts indexes to string for hashing
    :param indexes: the indexes of a hex. nx2, n=number of index pairs
    :return: key for hashing based on index.
    """
    return [str(int(index[0])) + ',' + str(int(index[1])) for index in indexes]


def solve_for_indexes(hexes):
    """
    We want to solve for the coefficients in the linear combos.
    :param hexes: The hexes whose indexes we want to solve for.
                  nx2, n=number of hexes
    :return: indexes of `hexes`
    """
    if hexes.shape[1] != 2:
        raise IncorrectCoordinatesError("Must be axial coordinates!")
    return np.linalg.solve(__bases_mat, hexes.T).T


class HexMap(dict):
    def __init__(self):
        super(HexMap, self).__init__()

    def __setitem__(self, coordinates, hex_objects):
        """
        Assigns hex objects as values to coordinates as keys. The number of coordinates and hex objects
        should be equal.
        :param coordinates: Locations of hex objects.
        :param hex_objects: the hex objects themselves.
        :return: None
        """
        if len(coordinates) != len(hex_objects):
            raise MismatchError("Number of coordinates does not match number of hex objects.")

        indexes = solve_for_indexes(coordinates)
        keys = make_key_from_indexes(indexes)
        for key, hex in zip(keys, hex_objects):
            if key in self.keys():
                raise HexExistsError("key " + key + " already exists.")

            super(HexMap, self).__setitem__(key, hex)

    def overwrite_entry(self, coordinate, hex):
        indexes = solve_for_indexes(np.array([coordinate]))
        keys = make_key_from_indexes(indexes)
        super(HexMap, self).__setitem__(keys[0], hex)

    def __getitem__(self, coordinates):
        """
        Retrieves hexes stores at `coordinates`
        :param coordinate: the locations used as keys for hexes. You can pass more than one coordinate
        :return: list of hexes mapped to using `coordinates`
        """
        if len(coordinates.shape) == 1:
            coordinates = np.array([coordinates])
        indexes = solve_for_indexes(coordinates)
        keys = make_key_from_indexes(indexes)
        hexes = []
        for key in keys:
            if key in self.keys():
                hexes.append(super(HexMap, self).__getitem__(key))
        return hexes

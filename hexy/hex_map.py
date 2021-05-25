"""
This file contains routines for storing the properties of hexes

The keys are just the axial coordinates.

Key Rules:
- must be written 'a,b' without quotes
- no spaces
- a and b can be negative, so it is okay if the key is written as
  '-a,b' or 'a,-b' or '-a,-b'
"""
import numpy as np

from .errors import IncorrectCoordinatesError, HexExistsError, MismatchError
from .hexy import cube_to_axial, SE, E

# The bases of the axial coordinate system
bases_mat = cube_to_axial(np.array([SE, E], dtype=int))


def make_key_from_coordinates(indexes):
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
    return np.linalg.solve(bases_mat, hexes.T).T


class HexMap:
    def __init__(self):
        self._map = {}

    def keys(self):
        yield from self._map.keys()

    def values(self):
        yield from self._map.values()

    def items(self):
        yield from self._map.items()

    def __len__(self):
        return self._map.__len__()

    def __iter__(self):
        yield from self._map

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

        keys = make_key_from_coordinates(coordinates)
        for key, hex in zip(keys, hex_objects):
            if key in self._map.keys():
                raise HexExistsError("key " + key + " already exists.")

            self._map[key] = hex

    def setitem_direct(self, key, value):
        if key in self._map.keys():
            raise HexExistsError("key " + key + " already exists.")

        self._map[key] = value

    def overwrite_entries(self, coordinates, hex):
        keys = make_key_from_coordinates(coordinates)
        for key in keys:
            self._map[key] = hex

    def __delitem__(self, coordinates):
        if len(coordinates.shape) == 1:
            coordinates = np.array([coordinates])
        keys = make_key_from_coordinates(coordinates)
        for key in keys:
            if key in self.keys():
                del self._map[key]

    def __getitem__(self, coordinates):
        """
        Retrieves hexes stores at `coordinates`
        :param coordinate: the locations used as keys for hexes. You can pass more than one coordinate
        :return: list of hexes mapped to using `coordinates`
        """
        if len(coordinates.shape) == 1:
            coordinates = np.array([coordinates])
        keys = make_key_from_coordinates(coordinates)
        return [self._map.get(k) for k in keys if k in self._map.keys()]

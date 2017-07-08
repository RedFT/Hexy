import numpy as np
import hexy as hx

class HexTile(object):
    """
    Base Hex class. Doesn't do anything. Ideally, you want to store instances of
    a subclass of this tile in a HexMap object.
    """

    def __init__(self, axial_coordinates, radius, tile_idx):
        super(HexTile, self).__init__()
        self.axial_coordinates = np.array([axial_coordinates])
        self.cube_coordinates = hx.axial_to_cube(self.axial_coordinates)
        self.position = hx.axial_to_pixel(self.axial_coordinates, radius)
        self.radius = radius
        self.tile_idx = tile_idx

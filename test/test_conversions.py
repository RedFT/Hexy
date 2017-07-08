import sys
sys.path.append("..")
import numpy as np
import hexy as hx


hm = hx.HexMap()


def same_mat(A, B):
    if np.unique(A == B) == [True]:
        return True
    return False


radius = 10
coords = hx.get_spiral(np.array((0, 0, 0)), 1, 10)

# check axial <-> cube conversions work
axial_coords = hx.cube_to_axial(coords)
cube_coords = hx.axial_to_cube(axial_coords)

print same_mat(coords, cube_coords)

# check axial <-> pixel conversions work
pixel_coords = hx.axial_to_pixel(axial_coords, radius)
pixel_to_axial_coords = hx.pixel_to_axial(pixel_coords, radius)

print same_mat(axial_coords, pixel_to_axial_coords)

# check cube <-> pixel conversions work
pixel_coords = hx.cube_to_pixel(cube_coords, radius)
pixel_to_cube_coords = hx.pixel_to_cube(pixel_coords, radius)
pixel_to_cube_to_axial_coords = hx.cube_to_axial(pixel_to_cube_coords)

print same_mat(cube_coords, pixel_to_cube_coords)

# check that we can correctly retrieve hexes after conversions
hm[axial_coords] = coords
retrieved = hm[pixel_to_cube_to_axial_coords]
print same_mat(retrieved, cube_coords)

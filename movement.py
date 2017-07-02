import numpy as np


class DIR:
    # <r, g, b>
    SE=np.array((1, 0, -1))
    SW=np.array((0, 1, -1))
    W =np.array((-1, 1, 0))
    NW=np.array((-1, 0, 1))
    NE=np.array((0, -1, 1))
    E =np.array((1, -1, 0))


def cube_to_axial(direction):
    q = direction[0]
    r = direction[2]
    return np.array((q, r))


def axial_to_cube(direction):
    x = direction[0]
    z = direction[1]
    y = -x-z
    return np.array((x, y, z))


hex_to_pixel_mat = np.array([[np.sqrt(3), np.sqrt(3)/2],[0 , 3/2.]])
pixel_to_hex_mat = np.array([[np.sqrt(3)/3, -1./3],[0 , 2/3.]])
def hex_to_pixel(direction, radius):
    pos = radius * hex_to_pixel_mat.dot(cube_to_axial(direction))
    return pos


def pixel_to_hex(coords, radius):
    pos = pixel_to_hex_mat.dot(coords) / radius
    return cube_round(axial_to_cube(pos))


def cube_round(cube):
    rounded = (rx, ry, rz) = map(round, cube)
    xdiff, ydiff, zdiff = map(abs, rounded - cube)
    if xdiff > ydiff and xdiff > zdiff:
        rx = -ry-rz
    elif ydiff > zdiff:
        ry = -rx-rz
    else:
        rz = -rx-ry
    return np.array((rx, ry, rz))

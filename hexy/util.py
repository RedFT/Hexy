import numpy as np

# Matrix for converting cube coordinates to pixel coordinates
__hex_to_pixel_mat = np.array([[np.sqrt(3), np.sqrt(3) / 2], [0, 3 / 2.]])

# Matrix for converting pixel coordinates to cube coordinates
__pixel_to_hex_mat = np.array([[np.sqrt(3) / 3, -1. / 3], [0, 2 / 3.]])


class DIR:
    """
    This class contains the vectors for moving from any hex to one of its
    neighbors.
    """
    SE = np.array((1, 0, -1))
    SW = np.array((0, 1, -1))
    W = np.array((-1, 1, 0))
    NW = np.array((-1, 0, 1))
    NE = np.array((0, -1, 1))
    E = np.array((1, -1, 0))
    ALL=np.array([NW,NE,E,SE,SW,W,])


def get_neighbor(hex, direction):
    """
    Simply returns the neighbor, in the direction specified, of the hexagon.
    :param hex: Cube coordinates of the hexagon.
    :param direction: A direction from the DIR class.
    :return: The location of the neighbor in cube coordinates.
    """
    return hex + direction


def get_ring(center, radius):
    """
    Retrieves the locations of all the hexes exactly a certain distance from a hexagon.
    :param center: The location of the hexagon to get the ring of.
    :param radius: The distance from `center` of the hexes we want.
    :return: An array of locations of the hexes that are exactly `radius` units away from `center`.
    """
    if radius < 0:
        return []
    if radius == 0:
        return [center]

    rad_hex = np.zeros((6*radius, 3))
    count = 0
    for i in range(0, 6):
        for k in range(0, radius):
            rad_hex[count] = DIR.ALL[i-1] * (radius-k) + DIR.ALL[i] * (k)
            count += 1

    return np.squeeze(rad_hex) + center.astype(int)


def get_area(center, radius):
    """
    Retrieves all hexes that are `radius` hexes away from the `center`.
    :param center: The location of the center hex.
    :param radius: The distance from center. We want all hexes within this distance from `center`.
    :return: An array of locations of the hexes that are within `radius` hexes away from `center`.
    """
    hex_area = get_ring(center, 0)
    for i in range(1, radius + 1):
        hex_area=np.append(hex_area, get_ring(center, i), axis=0)
    return hex_area


def cube_to_axial(cube):
    """
    Convert cube to axial coordinates.
    :param cube: A coordinate in cube form.
    :return: `cube` in axial form.
    """
    q = cube[0]
    r = cube[2]
    return np.array((q, r))


def axial_to_cube(axial):
    """
    Convert axial to cube coordinates.
    :param axial: A coordinate in axial form.
    :return: `axial` in cube form.
    """
    x = axial[0]
    z = axial[1]
    y = -x - z
    return np.array((x, y, z))


def hex_to_pixel(cube, radius):
    """
    Converts the location of a hex in cube form to pixel coordinates.
    :param cube: The location of a hex in cube form.
    :param radius: Radius of all hexagons.
    :return: `cube` in pixel coordinates.
    """
    pos = radius * __hex_to_pixel_mat.dot(cube_to_axial(cube))
    return pos


def pixel_to_hex(pixel, radius):
    """
    Converts the location of a hex in pixel coordinates to cube form.
    :param pixel: The location of a hex in pixel coordinates.
    :param radius: Radius of all hexagons.
    :return: `pixel` in cube coordinates.
    """
    pos = __pixel_to_hex_mat.dot(pixel) / radius
    return cube_round(axial_to_cube(pos))


def cube_round(cube):
    """
    Rounds a location in cube coordinates to the center of the nearest hex.
    :param cube: A location in cube form.
    :return: The location of the center of the nearest hex in cube coordinates.
    """
    rounded = (rx, ry, rz) = map(round, cube)
    xdiff, ydiff, zdiff = map(abs, rounded - cube)
    if xdiff > ydiff and xdiff > zdiff:
        rx = -ry - rz
    elif ydiff > zdiff:
        ry = -rx - rz
    else:
        rz = -rx - ry
    return np.array((rx, ry, rz))


def axial_round(axial):
    """
    Rounds a location in axial coordinates to the center of the nearest hex.
    :param axial: A location in axial form.
    :return: The location of the center of the nearest hex in axial coordinates.
    """
    return cube_to_axial(cube_round(axial_to_cube(axial)))

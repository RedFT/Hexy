import numpy as np
import pygame as pg


def draw_hex(surf, color, pos, r):
    """
    Draws a hexagon with gray borders on a pygame surface.
    :param surf: pygame surface to draw on.
    :param color: The fill color of the hexagon.
    :param pos: Where to draw the center of the hexagon.
    :param r: The radius (from center to any corner) of the hexagon.
    :return: None
    """
    points = []
    for i in range(6):
        angle = np.deg2rad(30 * (2 * i + 1))
        x = r * np.cos(angle)
        y = r * np.sin(angle)
        points.append((x, y))

    points = np.array(points)

    sorted_x = sorted(points[:, 0])
    sorted_y = sorted(points[:, 1])
    minx = sorted_x[0]
    maxx = sorted_x[-1]
    miny = sorted_y[0]
    maxy = sorted_y[-1]

    center = ((maxx - minx + 10) / 2, (maxy - miny + 10) / 2)
    surface = pg.Surface(map(int, (maxx - minx + 10, maxy - miny + 10)))
    surface.set_colorkey((0, 0, 0))
    surface.set_alpha(color[-1])
    pg.draw.polygon(surface, color, points + center, 0)

    pg.draw.polygon(surface, (100, 100, 100), points + center, 4)

    surf.blit(surface, pos - np.array(center))

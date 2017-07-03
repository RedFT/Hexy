import numpy as np
import pygame as pg
import hexy as hx


def draw_hex(surf, color, pos, r):
    points = []
    for i in range(6):
        angle = hx.deg_to_rad(30 * (2 * i + 1))
        x = r * np.cos(angle)
        y = r * np.sin(angle)
        # points.append((pos[0]+x, pos[1]+y))
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

    top_points = np.array([points[i] for i in range(-1, -4, -1)])
    pg.draw.polygon(surface, (100, 100, 100), points + center, 4)
    '''
    for i in range(-1, 20):
        #pg.draw.lines(surface, (100, 100, 100), False, top_points + center + (0, i), 2)
        pg.draw.line(surface, (100, 100, 100),
                     top_points[0] + center + (0, i),
                     top_points[1] + center + (0, i), 2)
        pg.draw.line(surface, (50, 50, 50),
                     top_points[1] + center + (0, i),
                     top_points[2] + center + (0, i), 2)

    '''
    surf.blit(surface, pos - np.array(center))

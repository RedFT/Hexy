import numpy as np
import pygame as pg
from util import deg_to_rad


def draw_hex(surf, color, pos, r):
    points=[]
    for i in range(6):
        angle=deg_to_rad(30*(2*i + 1))
        x=r*np.cos(angle)
        y=r*np.sin(angle)
        points.append((pos[0]+x, pos[1]+y))

    pg.draw.polygon(surf, color, points, 0)
    pg.draw.polygon(surf, (100, 100, 100), points, 4)


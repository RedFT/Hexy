import numpy as np
import pygame as pg
from itertools import product

from movement import DIR, hex_to_pixel, pixel_to_hex
from draw import draw_hex
from util import deg_to_rad

SIZE=np.array((640, 480))
WIDTH,HEIGHT=SIZE
HEX_RADIUS=40.
HEX_APOTHEM=HEX_RADIUS*np.cos(deg_to_rad(30))
CENTER=SIZE/2
HEX_POS=np.array((0, 0, 0))


pg.init()
main_surf = pg.display.set_mode(SIZE)
pg.display.set_caption("HEX")

pg.font.init()
font = pg.font.SysFont("monospace", 12)


dims = [-3, -2, -1, 0, 1, 2, 3]
_coords = list(product(dims, dims, dims))
coords = []
for coord in _coords:
    if (coord[0] + coord[1] + coord[2]) == 0:
        coords.append(coord)


running = True
while running:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False

  for coord in coords:
      pos = hex_to_pixel(coord, HEX_RADIUS) + CENTER
      draw_hex(main_surf, (0, 255, 0), pos, HEX_RADIUS)

  pos = np.array(pg.mouse.get_pos()) - CENTER
  coord=pixel_to_hex(pos, HEX_RADIUS)
  abs_coord=map(abs,coord)
  if abs_coord[0] <= 3 and abs_coord[1] <= 3 and abs_coord[2] <= 3:
      pos = hex_to_pixel(coord, HEX_RADIUS) + CENTER
      draw_hex(main_surf, (0, 0, 255), pos, HEX_RADIUS)

  pg.display.flip()
  main_surf.fill((0, 0, 0))


pg.quit()

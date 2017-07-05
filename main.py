import numpy as np
import pygame as pg
from itertools import product

import hexy as hx

SIZE = np.array((800, 600))
WIDTH, HEIGHT = SIZE
HEX_RADIUS = 20.
HEX_APOTHEM = HEX_RADIUS * np.cos(np.deg2rad(30))
CENTER = SIZE / 2
HEX_POS = np.array((0, 0, 0))

colors = np.array([
    [244,98,105], # red
    [251,149,80], # orange
    [141,207,104], # green
    [53,111,163], # water blue
    [85,163,193], # sky blue
    ])

col_idx=np.random.randint(0, 4, (7**3))


def init(caption="App"):
    pg.init()
    pg.font.init()
    main_surf = pg.display.set_mode(SIZE)
    pg.display.set_caption(caption)
    return main_surf


def get_coords(low_bound=-4, upper_bound=4):
    dims = range(low_bound, upper_bound + 1)
    _coords = list(product(dims, dims, dims))
    return [coord for coord in _coords if sum(coord) == 0]


def main(main_surf):
    font = pg.font.SysFont("monospace", 14, True)
    max_coord = 7
    # coords = get_coords(-max_coord, max_coord)
    coords = hx.get_area(np.array((0, 0, 0)), max_coord)
    running = True

    rad=3
    circle=False
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 3:
                    circle = False if circle == True else True
                if event.button == 4:
                    rad+=1
                if event.button == 5:
                    rad -= 1

            if event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    rad+=1
                elif event.key == pg.K_DOWN:
                    rad -= 1
        if rad > 5:
            rad = 5
        elif rad < 0:
            rad = 0


        # show all hexes
        for i, coord in enumerate(coords):
            pos = hx.hex_to_pixel(coord, HEX_RADIUS) + CENTER
            colo = list(colors[col_idx[i]]) + [255]
            hx.draw_hex(main_surf, colo, pos, HEX_RADIUS)

            text = font.render(str(i), False, (0, 0, 0))
            text.set_alpha(160)
            text_pos = pos
            text_pos -= (text.get_width() / 2, text.get_width() / 2)
            main_surf.blit(text, text_pos)

        # show highlighted hex
        pos = np.array(pg.mouse.get_pos()) - CENTER
        coord = hx.pixel_to_hex(pos, HEX_RADIUS)
        abs_coord = map(abs, coord)
        if abs_coord[0] <= max_coord and abs_coord[1] <= max_coord and abs_coord[2] <= max_coord:
            pos = hx.hex_to_pixel(coord, HEX_RADIUS) + CENTER
            hx.draw_hex(main_surf, (75, 75, 75, 128), pos, HEX_RADIUS)


        if circle:
            rad_hex = hx.get_area(coord, rad)
        else:
            rad_hex = hx.get_ring(coord, rad)
        # show ring hexes
        for point in rad_hex:
            pos = hx.hex_to_pixel(point, HEX_RADIUS) + CENTER
            hx.draw_hex(main_surf, (0, 0, 128, 128), pos, HEX_RADIUS)



        pg.display.flip()
        main_surf.fill(colors[-1])

    pg.quit()


if __name__ == '__main__':
    main_surf = init()
    main(main_surf)

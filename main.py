import numpy as np
import pygame as pg
import hexy as hx


COL_IDX = np.random.randint(0, 4, (7 ** 3))
COLORS = np.array([
    [244,  98, 105],  # red
    [251, 149,  80],  # orange
    [141, 207, 104],  # green
    [53,  111, 163],  # water blue
    [85,  163, 193],  # sky blue
])


class ExampleHexMap():
    def __init__(self, size=(800, 600), hex_radius=20, caption="ExampleHexMap"):
        self.size = np.array(size)
        self.width, self.height = self.size

        self.hex_radius = hex_radius
        self.hex_apothem = hex_radius * np.sqrt(3) / 2

        self.center = self.size / 2

        pg.init()
        pg.font.init()
        self.main_surf = pg.display.set_mode(self.size)
        pg.display.set_caption(caption)

    def main_loop(self):
        font = pg.font.SysFont("monospace", 14, True)
        max_coord = 7
        coords = hx.get_area(np.array((0, 0, 0)), max_coord)
        running = True

        rad = 3
        circle = False
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        circle = False if circle == True else True
                    if event.button == 4:
                        rad += 1
                    if event.button == 5:
                        rad -= 1

                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        rad += 1
                    elif event.key == pg.K_DOWN:
                        rad -= 1

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        running = False

            if rad > 5:
                rad = 5
            elif rad < 0:
                rad = 0

            # show all hexes
            for i, coord in enumerate(coords):
                pos = hx.hex_to_pixel(coord, self.hex_radius) + self.center
                colo = list(COLORS[COL_IDX[i]]) + [255]
                hx.draw_hex(self.main_surf, colo, pos, self.hex_radius)

                text = font.render(str(i), False, (0, 0, 0))
                text.set_alpha(160)
                text_pos = pos
                text_pos -= (text.get_width() / 2, text.get_width() / 2)
                self.main_surf.blit(text, text_pos)

            # show highlighted hex
            pos = np.array(pg.mouse.get_pos()) - self.center
            coord = hx.pixel_to_hex(pos, self.hex_radius)
            abs_coord = map(abs, coord)
            if abs_coord[0] <= max_coord and abs_coord[1] <= max_coord and abs_coord[2] <= max_coord:
                pos = hx.hex_to_pixel(coord, self.hex_radius) + self.center
                hx.draw_hex(self.main_surf, (75, 75, 75, 128), pos, self.hex_radius)

            if circle:
                rad_hex = hx.get_area(coord, rad)
            else:
                rad_hex = hx.get_ring(coord, rad)
            # show ring hexes
            for point in rad_hex:
                pos = hx.hex_to_pixel(point, self.hex_radius) + self.center
                hx.draw_hex(self.main_surf, (0, 0, 128, 128), pos, self.hex_radius)

            pg.display.flip()
            self.main_surf.fill(COLORS[-1])

        pg.quit()


if __name__ == '__main__':
    ehm = ExampleHexMap()
    ehm.main_loop()

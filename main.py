import numpy as np
import pygame as pg
import hexy as hx


def make_hex_surface(color, radius, border_color=(100, 100, 100), border=True, hollow=False):
    """
    Draws a hexagon with gray borders on a pygame surface.
    :param color: The fill color of the hexagon.
    :param radius: The radius (from center to any corner) of the hexagon.
    :return: A pygame surface with a hexagon drawn on it
    """
    points = []
    for i in range(6):
        angle = np.deg2rad(30 * (2 * i + 1))
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
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
    if len(color) >= 4:
        surface.set_alpha(color[-1])
    if not hollow:
        pg.draw.polygon(surface, color, points + center, 0)

    if border or (not hollow):
        pg.draw.polygon(surface, border_color, points + center, 4)
    return surface


class MyHex(hx.HexTile):
    def __init__(self, axial_coordinates=(0, 0, 0), color=(128, 0, 0), radius=20):
        self.axial_coordinates = axial_coordinates
        self.position = hx.hex_to_pixel(hx.axial_to_cube(axial_coordinates), radius)
        self.color = color
        self.radius = radius
        self.image = make_hex_surface(color, radius)
        self.value = None

    def set_value(self, value):
        self.value = value

    def get_draw_position(self):
        return self.position - [self.image.get_width() / 2, self.image.get_height() / 2]


COL_IDX = np.random.randint(0, 4, (7 ** 3))
COLORS = np.array([
    [244, 98, 105],  # red
    [251, 149, 80],  # orange
    [141, 207, 104],  # green
    [53, 111, 163],  # water blue
    [85, 163, 193],  # sky blue
])


class ExampleHexMap():
    def __init__(self, size=(600, 600), hex_radius=22, caption="ExampleHexMap"):
        self.size = np.array(size)
        self.width, self.height = self.size
        self.center = self.size / 2

        self.hex_radius = hex_radius
        self.hex_apothem = hex_radius * np.sqrt(3) / 2
        self.hex_offset = np.array([self.hex_radius * np.sqrt(3) / 2, self.hex_radius])

        self.hex_map = hx.HexMap()
        self.max_coord = 7

        self.circle = False
        self.rad = 3

        self.selected_hex_image = make_hex_surface((128, 128, 128, 160), self.hex_radius, (255, 255, 255), hollow=True)
        coords = hx.get_area(np.array((0, 0, 0)), self.max_coord)
        axial_coords = []
        for coord in coords:
            axial_coords.append(hx.cube_to_axial(coord))

        hexes = []
        for i, coord in enumerate(axial_coords):
            colo = list(COLORS[COL_IDX[i]])
            colo.append(255)
            hexes.append(MyHex(coord, colo, hex_radius))
            hexes[-1].set_value(i)

        self.hex_map[np.array(axial_coords)] = hexes

        pg.init()
        self.main_surf = pg.display.set_mode(self.size)
        pg.display.set_caption(caption)

        pg.font.init()
        self.font = pg.font.SysFont("monospace", 14, True)

    def main_loop(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        self.circle = False if self.circle == True else True
                    if event.button == 4:
                        self.rad += 1
                    if event.button == 5:
                        self.rad -= 1

                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        self.rad += 1
                    elif event.key == pg.K_DOWN:
                        self.rad -= 1

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        running = False

            if self.rad > 5:
                self.rad = 5
            elif self.rad < 0:
                self.rad = 0

            # show all hexes
            for hex in self.hex_map.values():
                self.main_surf.blit(hex.image, hex.get_draw_position() + self.center)

            for hex in self.hex_map.values():
                text = self.font.render(str(hex.value), False, (0, 0, 0))
                text.set_alpha(160)
                text_pos = hex.position + self.center
                text_pos -= (text.get_width() / 2, text.get_height() / 2)
                self.main_surf.blit(text, text_pos)

            # show highlighted hex
            pos = np.array(pg.mouse.get_pos()) - self.center
            coord = hx.pixel_to_hex(pos, self.hex_radius)
            hexes = self.hex_map[hx.cube_to_axial(coord)]
            if len(hexes) > 0:
                hex = hexes[0]
                self.main_surf.blit(self.selected_hex_image, hex.get_draw_position() + self.center)

            if self.circle:
                rad_hex = hx.get_area(coord, self.rad)
            else:
                rad_hex = hx.get_ring(coord, self.rad)
            # show ring hexes
            for point in rad_hex:
                hexes = self.hex_map[hx.cube_to_axial(point)]
                if len(hexes) > 0:
                    hex = hexes[0]
                    self.main_surf.blit(self.selected_hex_image, hex.get_draw_position() + self.center)

            pg.display.update()
            self.main_surf.fill(COLORS[-1])

        pg.quit()


if __name__ == '__main__':
    ehm = ExampleHexMap()
    ehm.main_loop()

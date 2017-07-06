from test_hex import *

COL_IDX = np.random.randint(0, 4, (7 ** 3))
COLORS = np.array([
    [244, 98, 105],  # red
    [251, 149, 80],  # orange
    [141, 207, 104],  # green
    [53, 111, 163],  # water blue
    [85, 163, 193],  # sky blue
])


class SelectionType:
    POINT = 0
    RING = 1
    DISK = 2
    LINE = 3


class ExampleHexMap():
    def __init__(self, size=(600, 600), hex_radius=22, caption="ExampleHexMap"):
        self.caption = caption
        self.size = np.array(size)
        self.width, self.height = self.size
        self.center = self.size / 2

        self.hex_radius = hex_radius
        self.hex_apothem = hex_radius * np.sqrt(3) / 2
        self.hex_offset = np.array([self.hex_radius * np.sqrt(3) / 2, self.hex_radius])

        self.hex_map = hx.HexMap()
        self.max_coord = 7

        self.rad = 3

        self.selected_hex_image = make_hex_surface((128, 128, 128, 160), self.hex_radius, (255, 255, 255), hollow=True)
        self.selection_type = 0

        # Get all possible coordinates within `self.max_coord` as radius.
        coords = hx.get_disk(np.array((0, 0, 0)), self.max_coord)

        # Convert coords to axial coordinates, create hexes and randomly filter out some hexes.
        axial_coords = []
        hexes = []
        num_hexes = np.random.binomial(len(coords), 1.0)
        for i in np.random.choice(len(coords), num_hexes, replace=False):  # enumerate(coords):
            axial_coord = hx.cube_to_axial(coords[i])
            axial_coords.append(axial_coord)

            colo = list(COLORS[COL_IDX[i]])
            colo.append(255)
            hexes.append(MyHex(axial_coord, colo, hex_radius))
            hexes[-1].set_value(i)  # the number at the center of the hex

        self.hex_map[np.array(axial_coords)] = hexes

        self.main_surf = None
        self.font = None
        self.init_pg()

    def init_pg(self):
        pg.init()
        self.main_surf = pg.display.set_mode(self.size)
        pg.display.set_caption(self.caption)

        pg.font.init()
        self.font = pg.font.SysFont("monospace", 14, True)

    def handle_events(self):
        running = True
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 3:
                    self.selection_type += 1
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
        return running

    def main_loop(self):
        running = self.handle_events()
        if self.rad > 5:
            self.rad = 5
        elif self.rad < 0:
            self.rad = 0

        if self.selection_type > 3:
            self.selection_type = 0

        return running

    def draw(self):
        # show all hexes
        for hexagon in self.hex_map.values():
            self.main_surf.blit(hexagon.image, hexagon.get_draw_position() + self.center)

        # draw values of hexes
        for hexagon in self.hex_map.values():
            text = self.font.render(str(hexagon.value), False, (0, 0, 0))
            text.set_alpha(160)
            text_pos = hexagon.position + self.center
            text_pos -= (text.get_width() / 2, text.get_height() / 2)
            self.main_surf.blit(text, text_pos)

        # show highlighted hex
        pos = np.array(pg.mouse.get_pos()) - self.center
        coord = hx.pixel_to_hex(pos, self.hex_radius)

        # choose either ring or disk
        if self.selection_type == SelectionType.DISK:
            rad_hex = hx.get_disk(coord, self.rad)
        elif self.selection_type == SelectionType.RING:
            rad_hex = hx.get_ring(coord, self.rad)
        elif self.selection_type == SelectionType.LINE:
            rad_hex = hx.get_hex_line(np.zeros((3,)), coord)
        elif self.selection_type == SelectionType.POINT:
            rad_hex = [coord.copy()]

        # show ring hexes
        for point in rad_hex:
            hexes = self.hex_map[hx.cube_to_axial(point)]
            if len(hexes) > 0:
                hexagon = hexes[0]
                self.main_surf.blit(self.selected_hex_image, hexagon.get_draw_position() + self.center)

        # draw hud
        if self.selection_type == SelectionType.DISK:
            select_type = "Disk"
        elif self.selection_type == SelectionType.RING:
            select_type = "Ring"
        elif self.selection_type == SelectionType.LINE:
            select_type = "Line"
        else:
            select_type = "Point"
        selection_type_text = self.font.render("(Right Click To Change) Selection Type: " + select_type, True,
                                               (50, 50, 50))
        self.main_surf.blit(selection_type_text, (0, 0))
        radius_text = self.font.render("(Scroll Mouse Wheel To Change) Radius: " + str(self.rad), True, (50, 50, 50))
        self.main_surf.blit(radius_text, (0, 15))

        # Update screen
        pg.display.update()
        self.main_surf.fill(COLORS[-1])

    def quit_app(self):
        pg.quit()


if __name__ == '__main__':
    ehm = ExampleHexMap()
    while ehm.main_loop():
        ehm.draw()
    ehm.quit_app()

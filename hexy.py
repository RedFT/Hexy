from util import *


class HexTile(object):
    def __init__(self, axial_pos):
        super(HexTile, self).__init__()
        self.axial_pos = np.array(axial_pos)

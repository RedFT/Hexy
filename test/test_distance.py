import numpy as np
import hexy as hx

def test_get_cube_distance():
    start = np.array([0, 2, -2])
    end = np.array([-2, -1, 3])
    assert(hx.get_cube_distance(start, end) == 5)
    assert(hx.get_cube_distance(start, start) == 0)

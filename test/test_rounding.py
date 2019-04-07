import numpy as np
import hexy as hx

def test_cube_round():
    test_coords = np.array([
        [1.1, -1.4, 0.3],
        [3.3, 2.3, -5.4],
        ]);

    expected_coords = np.array([
        [1, -1, 0],
        [3, 2, -5],
        ]);

    assert(np.array_equal(hx.cube_round(test_coords), expected_coords))

def test_axial_round():
    test_coords = np.array([
        [1.1, -1.4],
        [3.3, 2.3],
        ]);

    expected_coords = np.array([
        [1, -1],
        [3, 2],
        ]);

    assert(np.array_equal(hx.axial_round(test_coords), expected_coords))

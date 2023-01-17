import numpy as np
import hexy as hx
import pprint


# The way get_ring works is:
#   For a radius r, grab two adjacent "directions" d1, d2 and find all linear
#   combinations a * d1 + b * d2 such that a and b are positive integers and
#   a + b = r.
#
# In the implementation, we omit a * d1 + r * d2 because if this is included, we'll
# get duplicates coordinates.
def test_get_ring_with_positive_radius():
    r=3
    expected = _get_linear_combinations(hx.W, hx.NW, r) + \
               _get_linear_combinations(hx.NW, hx.NE, r) + \
               _get_linear_combinations(hx.NE, hx.E, r) + \
               _get_linear_combinations(hx.E, hx.SE, r) + \
               _get_linear_combinations(hx.SE, hx.SW, r) + \
               _get_linear_combinations(hx.SW, hx.W, r)

    _assert_np_array_equal(hx.get_ring([0, 0, 0], r), expected)


def test_get_ring_with_negative_radius():
    _assert_np_array_equal(hx.get_ring([0, 0, 0], -1), [])


def test_get_ring_with_zero_radius():
    _assert_np_array_equal(hx.get_ring([0, 0, 0], 0), [[0, 0, 0]])


def test_get_spiral():
    start_radius = 2
    end_radius = 4
    expected = []
    for r in range(start_radius, end_radius + 1):
        expected += _get_linear_combinations(hx.W, hx.NW, r) + \
                    _get_linear_combinations(hx.NW, hx.NE, r) + \
                    _get_linear_combinations(hx.NE, hx.E, r) + \
                    _get_linear_combinations(hx.E, hx.SE, r) + \
                    _get_linear_combinations(hx.SE, hx.SW, r) + \
                    _get_linear_combinations(hx.SW, hx.W, r)

    actual_array = hx.get_spiral([0, 0, 0], start_radius, end_radius)
    expected_array = np.array(expected)
    _assert_np_array_equal(actual_array, expected_array)



def test_get_disk():
    expected = [[0, 0, 0]]
    radius=3
    for r in range(radius+1):
        expected += _get_linear_combinations(hx.W, hx.NW, r) + \
                    _get_linear_combinations(hx.NW, hx.NE, r) + \
                    _get_linear_combinations(hx.NE, hx.E, r) + \
                    _get_linear_combinations(hx.E, hx.SE, r) + \
                    _get_linear_combinations(hx.SE, hx.SW, r) + \
                    _get_linear_combinations(hx.SW, hx.W, r)

    actual_array = hx.get_disk([0, 0, 0], radius)
    expected_array = np.array(expected)
    _assert_np_array_equal(actual_array, expected_array)


def test_get_disk_not_at_origin():
    center = hx.SE
    expected = [center]
    radius=3
    for r in range(radius+1):
        expected += _get_linear_combinations(hx.W, hx.NW, r, center) + \
                    _get_linear_combinations(hx.NW, hx.NE, r, center) + \
                    _get_linear_combinations(hx.NE, hx.E, r, center) + \
                    _get_linear_combinations(hx.E, hx.SE, r, center) + \
                    _get_linear_combinations(hx.SE, hx.SW, r, center) + \
                    _get_linear_combinations(hx.SW, hx.W, r, center)

    actual_array = hx.get_disk(center, radius)
    expected_array = np.array(expected)
    _assert_np_array_equal(actual_array, expected_array)


def _assert_np_array_equal(actual, expected):
    if not np.array_equal(actual, expected):
        msg = (
                f"Expected with length {len(expected)}: \n"
                f"{pprint.pformat(expected)}\n"
                f"But got with length {len(actual)}: \n"
                f"{pprint.pformat(actual)}\n"
        )
        raise AssertionError(msg)


def _get_linear_combinations(d1, d2, r, center = np.array([0, 0, 0])):
    return [(r - i) * d1 + i * d2 + center for i in range(r)]


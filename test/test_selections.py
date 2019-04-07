import numpy as np
import hexy as hx

from pprint import pprint

def test_get_ring():
    # The way get_ring works is for a radius r,
    # Grab two adjacent "directions" d1, d2 and find all linear combos a * d1 + b * d2
    # such that a and b are positive integers and a + b = r, 
    # in the implementatin we omit a * d1 + r * d2 because if this is included, we'll 
    # get duplicates coordinates.

    # For radius of 3
    r = 3
    expected = []
    expected.append((r - 0) * hx.W + 0 * hx.NW)
    expected.append((r - 1) * hx.W + 1 * hx.NW)
    expected.append((r - 2) * hx.W + 2 * hx.NW)

    expected.append((r - 0) * hx.NW + 0 * hx.NE)
    expected.append((r - 1) * hx.NW + 1 * hx.NE)
    expected.append((r - 2) * hx.NW + 2 * hx.NE)

    expected.append((r - 0) * hx.NE + 0 * hx.E)
    expected.append((r - 1) * hx.NE + 1 * hx.E)
    expected.append((r - 2) * hx.NE + 2 * hx.E)

    expected.append((r - 0) * hx.E + 0 * hx.SE)
    expected.append((r - 1) * hx.E + 1 * hx.SE)
    expected.append((r - 2) * hx.E + 2 * hx.SE)

    expected.append((r - 0) * hx.SE + 0 * hx.SW)
    expected.append((r - 1) * hx.SE + 1 * hx.SW)
    expected.append((r - 2) * hx.SE + 2 * hx.SW)

    expected.append((r - 0) * hx.SW + 0 * hx.W)
    expected.append((r - 1) * hx.SW + 1 * hx.W)
    expected.append((r - 2) * hx.SW + 2 * hx.W)

    assert(np.array_equal(
        hx.get_ring([0, 0, 0], r),
        expected))

    assert(np.array_equal(
        hx.get_ring([0, 0, 0], -1),
        []))

    assert(np.array_equal(
        hx.get_ring([0, 0, 0], 0),
        [[0, 0, 0]]))

def test_get_spiral():
    # For radius of 3
    expected = []

    r = 2
    expected.append((r - 0) * hx.W + 0 * hx.NW)
    expected.append((r - 1) * hx.W + 1 * hx.NW)

    expected.append((r - 0) * hx.NW + 0 * hx.NE)
    expected.append((r - 1) * hx.NW + 1 * hx.NE)

    expected.append((r - 0) * hx.NE + 0 * hx.E)
    expected.append((r - 1) * hx.NE + 1 * hx.E)

    expected.append((r - 0) * hx.E + 0 * hx.SE)
    expected.append((r - 1) * hx.E + 1 * hx.SE)

    expected.append((r - 0) * hx.SE + 0 * hx.SW)
    expected.append((r - 1) * hx.SE + 1 * hx.SW)

    expected.append((r - 0) * hx.SW + 0 * hx.W)
    expected.append((r - 1) * hx.SW + 1 * hx.W)

    r += 1
    expected.append((r - 0) * hx.W + 0 * hx.NW)
    expected.append((r - 1) * hx.W + 1 * hx.NW)
    expected.append((r - 2) * hx.W + 2 * hx.NW)

    expected.append((r - 0) * hx.NW + 0 * hx.NE)
    expected.append((r - 1) * hx.NW + 1 * hx.NE)
    expected.append((r - 2) * hx.NW + 2 * hx.NE)

    expected.append((r - 0) * hx.NE + 0 * hx.E)
    expected.append((r - 1) * hx.NE + 1 * hx.E)
    expected.append((r - 2) * hx.NE + 2 * hx.E)

    expected.append((r - 0) * hx.E + 0 * hx.SE)
    expected.append((r - 1) * hx.E + 1 * hx.SE)
    expected.append((r - 2) * hx.E + 2 * hx.SE)

    expected.append((r - 0) * hx.SE + 0 * hx.SW)
    expected.append((r - 1) * hx.SE + 1 * hx.SW)
    expected.append((r - 2) * hx.SE + 2 * hx.SW)

    expected.append((r - 0) * hx.SW + 0 * hx.W)
    expected.append((r - 1) * hx.SW + 1 * hx.W)
    expected.append((r - 2) * hx.SW + 2 * hx.W)

    assert(np.array_equal(
        hx.get_spiral([0, 0, 0], 2, 3),
        np.array(expected)))

def test_get_disk():
    # For radius of 3
    expected = []

    r = 0
    expected.append(hx.W * r)

    r += 1
    expected.append((r - 0) * hx.W + 0 * hx.NW)
    expected.append((r - 0) * hx.NW + 0 * hx.NE)
    expected.append((r - 0) * hx.NE + 0 * hx.E)
    expected.append((r - 0) * hx.E + 0 * hx.SE)
    expected.append((r - 0) * hx.SE + 0 * hx.SW)
    expected.append((r - 0) * hx.SW + 0 * hx.W)

    r += 1
    expected.append((r - 0) * hx.W + 0 * hx.NW)
    expected.append((r - 1) * hx.W + 1 * hx.NW)

    expected.append((r - 0) * hx.NW + 0 * hx.NE)
    expected.append((r - 1) * hx.NW + 1 * hx.NE)

    expected.append((r - 0) * hx.NE + 0 * hx.E)
    expected.append((r - 1) * hx.NE + 1 * hx.E)

    expected.append((r - 0) * hx.E + 0 * hx.SE)
    expected.append((r - 1) * hx.E + 1 * hx.SE)

    expected.append((r - 0) * hx.SE + 0 * hx.SW)
    expected.append((r - 1) * hx.SE + 1 * hx.SW)

    expected.append((r - 0) * hx.SW + 0 * hx.W)
    expected.append((r - 1) * hx.SW + 1 * hx.W)

    r += 1
    expected.append((r - 0) * hx.W + 0 * hx.NW)
    expected.append((r - 1) * hx.W + 1 * hx.NW)
    expected.append((r - 2) * hx.W + 2 * hx.NW)

    expected.append((r - 0) * hx.NW + 0 * hx.NE)
    expected.append((r - 1) * hx.NW + 1 * hx.NE)
    expected.append((r - 2) * hx.NW + 2 * hx.NE)

    expected.append((r - 0) * hx.NE + 0 * hx.E)
    expected.append((r - 1) * hx.NE + 1 * hx.E)
    expected.append((r - 2) * hx.NE + 2 * hx.E)

    expected.append((r - 0) * hx.E + 0 * hx.SE)
    expected.append((r - 1) * hx.E + 1 * hx.SE)
    expected.append((r - 2) * hx.E + 2 * hx.SE)

    expected.append((r - 0) * hx.SE + 0 * hx.SW)
    expected.append((r - 1) * hx.SE + 1 * hx.SW)
    expected.append((r - 2) * hx.SE + 2 * hx.SW)

    expected.append((r - 0) * hx.SW + 0 * hx.W)
    expected.append((r - 1) * hx.SW + 1 * hx.W)
    expected.append((r - 2) * hx.SW + 2 * hx.W)

    assert(np.array_equal(
        hx.get_disk([0, 0, 0], r),
        np.array(expected)))

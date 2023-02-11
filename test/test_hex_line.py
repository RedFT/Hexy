import numpy as np
import hexy as hx

def test_get_hex_line():
    expected = [
            [-3, 3, 0],
            [-2, 2, 0],
            [-1, 2, -1],
            [0, 2, -2],
            [1, 1, -2],
            ]
    start = np.array([-3, 3, 0])
    end = np.array([1, 1, -2])
    print(hx.get_hex_line(start, end))
    print(expected)
    assert(np.array_equal(
        hx.get_hex_line(start, end),
        expected))
    # testing one hex line special case
    one_hex_line = hx.get_hex_line(start, start)
    assert len(one_hex_line) == 1
    assert(np.array_equal(one_hex_line[0], start))
    assert id(start) != id(one_hex_line)


if __name__ == "__main__":
    test_get_hex_line()

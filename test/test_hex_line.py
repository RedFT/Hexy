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
    print(expected);
    assert(np.array_equal(
        hx.get_hex_line(start, end),
        expected));

if __name__ == "__main__":
    test_get_hex_line()

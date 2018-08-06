import numpy as np
import hexy as hx


hm = hx.HexMap()
radius = 10
coords = hx.get_spiral(np.array((0, 0, 0)), 1, 10)


def test_axial_to_cube_conversion():
    axial_coords = hx.cube_to_axial(coords)
    cube_coords = hx.axial_to_cube(axial_coords)

    assert np.array_equal(coords, cube_coords)


def test_axial_to_pixel_conversion():
    axial_coords = hx.cube_to_axial(coords)
    pixel_coords = hx.axial_to_pixel(axial_coords, radius)
    pixel_to_axial_coords = hx.pixel_to_axial(pixel_coords, radius)

    assert np.array_equal(axial_coords, pixel_to_axial_coords)


def test_cube_to_pixel_conversion():
    axial_coords = hx.cube_to_axial(coords)
    cube_coords = hx.axial_to_cube(axial_coords)
    pixel_coords = hx.cube_to_pixel(cube_coords, radius)
    pixel_to_cube_coords = hx.pixel_to_cube(pixel_coords, radius)
    pixel_to_cube_to_axial_coords = hx.cube_to_axial(pixel_to_cube_coords)

    assert np.array_equal(cube_coords, pixel_to_cube_coords)


def test_the_converted_coords_and_dataset_coords_retrieve_the_same_data():
    axial_coords = hx.cube_to_axial(coords)
    cube_coords = hx.axial_to_cube(axial_coords)
    pixel_coords = hx.cube_to_pixel(cube_coords, radius)
    pixel_to_cube_coords = hx.pixel_to_cube(pixel_coords, radius)
    pixel_to_cube_to_axial_coords = hx.cube_to_axial(pixel_to_cube_coords)

    # check that we can correctly retrieve hexes after conversions
    hm[axial_coords] = coords
    retrieved = hm[pixel_to_cube_to_axial_coords]

    assert np.array_equal(retrieved, coords)


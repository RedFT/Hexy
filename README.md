# Hexy, A library for dealing with hexagonal coordinate systems.

A library that makes working with a hexagonal lattice easier. Some of the inspiration for this library comes from [http://www.redblobgames.com/grids/hexagons/](http://www.redblobgames.com/grids/hexagons/).

![Alt text](/test/Hexy.gif?raw=true "Short Demo")

## Getting Started

### Prerequisites

The base library only requires `python2.7` and `numpy`.

If you want to run the tests, you should have `pygame` installed.


```
sudo apt install python2.7 python-numpy python-pygame
```

### Installing

Just clone this repository into your project's root.


## Running the example

Go the project root directory and run the following:

```
python2 -m test.test
```

The test app just shows off some features of the library. To play around you can:

```
- right click to change the hex selection type. 
- scroll up and down to change the radius of selection when selection type is ring or disk.
- left click to change the starting point of the line when selection type is a line.
```

## Authors

* **Norbu Tsering** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


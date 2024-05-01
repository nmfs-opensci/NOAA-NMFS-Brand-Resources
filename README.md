# nmfspalettepy

`nmfspalettepy` is a Python library designed to facilitate the use of National Marine Fisheries Service (NMFS) color palettes for data visualization. It provides easy access to a series of NMFS color schemes.

## Source:
- view on Github: https://github.com/MichaelAkridge-NOAA/NOAA-NMFS-Brand-Resources/tree/nmfspalettepy

## Features

- Provides a set of predefined color palettes using the NMFS color palettes.
- Functions to display and utilize these palettes in visualizations.
- Easy integration with matplotlib for creating custom color maps.

## Installation

### Install

To install `nmfspalettepy`, you can use pip. Simply run the following command:

```
pip install nmfspalettepy
```

#### To Install From Source
```
git clone -b nmfspalettepy https://github.com/MichaelAkridge-NOAA/NOAA-NMFS-Brand-Resources.git
cd NOAA-NMFS-Brand-Resources
python setup.py install
```

## To Use

## Listing Available Color Palettes

To see a list of all available color palettes you can use with `nmfspalettepy`, simply call the `list_nmfs_palettes` function:

```
import nmfspalettepy
print(nmfspalettepy.list_nmfs_palettes())
```

## Usage Examples

### Display a Color Gradient

To display a color gradient using one of the available NMFS color palettes, you can use the `display_color_gradient` function. Here's an example using the "oceans" palette:

```
from nmfspalettepy import display_color_gradient, get_palette_colors

# Display the 'oceans' palette gradient
display_color_gradient(get_palette_colors("oceans"))
```

### Creating a Custom Color Map
```
import matplotlib.pyplot as plt
from nmfspalettepy import create_nmfs_colormap

# Create a custom colormap
cmap = create_nmfs_colormap("coral")

# Use the colormap in a plot
plt.imshow([[1,2],[2,3]], cmap=cmap)
plt.colorbar()
plt.show()
```
### Getting Hex Codes for a Palette

```
from nmfspalettepy import get_palette_colors

# Get hex codes for the 'waves' palette
colors_hex = get_palette_colors("waves")
print("Hex codes for 'waves':", colors_hex)

```
----------
#### Disclaimer
This repository is a scientific product and is not official communication of the National Oceanic and Atmospheric Administration, or the United States Department of Commerce. All NOAA GitHub project content is provided on an ‘as is’ basis and the user assumes responsibility for its use. Any claims against the Department of Commerce or Department of Commerce bureaus stemming from the use of this GitHub project will be governed by all applicable Federal law. Any reference to specific commercial products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply their endorsement, recommendation or favoring by the Department of Commerce. The Department of Commerce seal and logo, or the seal and logo of a DOC bureau, shall not be used in any manner to imply endorsement of any commercial product or activity by DOC or the United States Government.

##### License
See the [LICENSE.md](https://github.com/MichaelAkridge-NOAA/NOAA-NMFS-Brand-Resources/tree/nmfspalettepy/LICENSE.md) for details

##### Credits
- Inspired by the work of (https://github.com/ChristineStawitz-NOAA) and other devs of: 
   - R Package: https://github.com/nmfs-fish-tools/nmfspalette/
   - R App/plot Tutorial: https://connect.fisheries.noaa.gov/colors/

# nmfspalettepy
<a href="https://pypi.org/project/nmfspalettepy">
    <img src="./docs/nmfspalettepy_250.png" align="right" alt="logo"/>
</a>
`nmfspalettepy` is a Python library designed to facilitate the use of National Marine Fisheries Service (NMFS) color palettes for data visualization. It provides easy access to a series of NMFS color schemes.

- [View 'nmfspalettepy' Python Package on PyPi](https://pypi.org/project/nmfspalettepy)


### Features
- Provides a set of predefined color palettes using the NMFS color palettes.
- Functions to display and utilize these palettes in visualizations.
- Easy integration with matplotlib for creating custom color maps.
# Table of Contents

- [Installation](#installation)
  - [To Install via pip](#installation)
  - [To Install From Source](#to-install-from-source)
- [Usage](#usage)
  - [Listing Available Color Palettes](#listing-available-color-palettes)
  - [Display a Color Gradient](#display-a-color-gradient)
  - [Creating a Custom Color Map](#creating-a-custom-color-map)
  - [Getting Hex Codes for a Palette](#getting-hex-codes-for-a-palette)
- [Examples](#examples)
  - [Plot](#plot)
  - [Boxplot](#boxplot)
  - [LinePlot](#lineplot)
## Installation
#### To Install via pip
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

## Usage

## Listing Available Color Palettes

To see a list of all available color palettes you can use with `nmfspalettepy`, simply call the `list_nmfs_palettes` function:

```
import nmfspalettepy
print(nmfspalettepy.list_nmfs_palettes())
```
### output
```
['oceans', 'waves', 'seagrass', 'urchin', 'crustacean', 'coral']
```

### Display a Color Gradient

To display a color gradient using one of the available NMFS color palettes, you can use the `display_color_gradient` function. Here's an example using the "oceans" palette:

```
from nmfspalettepy import display_color_gradient, get_palette_colors

# Display the 'oceans' palette gradient
display_color_gradient(get_palette_colors("oceans"))
```
![](./docs/waves_palette.png)
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
![](./docs/waves_plot_square.png)
### Getting Hex Codes for a Palette

```
from nmfspalettepy import get_palette_colors

# Get hex codes for the 'waves' palette
colors_hex = get_palette_colors("waves")
print("Hex codes for 'waves':", colors_hex)

```
### output
```
Hex codes for 'waves': ['#005E5E', '#00797F', '#1EBEC7', '#90DFE3']
```

## Examples
### Plot
![](./docs/waves_plot.png)
```
# example data| import seaborn as sns
from plotnine.data import penguins
p = (
    ggplot(penguins_clean, aes(x='flipper_length_mm', y='body_mass_g', color='species')) +
    geom_point(size=4) +
    labs(y="Body Mass (g)", x="Flipper Length (mm)") +
    theme_bw() +
    scale_color_manual(values=nmfs_palettes["urchin"])  # Use 'urchin' palette
)

# Show the plot
p.show()
```

### Boxplot
![](./docs/waves_boxplot.png)
```
def show_boxplot(data, x_var, y_var, hue_var, palette_name):
    palette = nmfs_palettes.get(palette_name, ["#555555"])  # Default grey if not found
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=x_var, y=y_var, hue=hue_var, palette=palette, data=data)
    sns.despine(offset=10, trim=True)
    plt.show()
```
### LinePlot
![](./docs/waves_lineplot.png)
```
def show_lineplot(data, x_var, y_var, hue_var, palette_name):
    palette = nmfs_palettes.get(palette_name, ["#555555"])  # Default grey if not found
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=x_var, y=y_var, hue=hue_var, palette=palette, data=data)
    plt.title(f"{y_var.capitalize()} over {x_var.capitalize()} by {hue_var.capitalize()}")
    plt.grid(True)
    sns.despine(offset=10, trim=True)
    plt.show()
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

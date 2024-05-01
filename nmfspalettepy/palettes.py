import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Define the NMFS color palettes
nmfs_color_palettes = {
    "oceans": ["#001743", "#002364", "#003087", "#0085CA", "#5EB6D9", "#C6E6F0"],
    "waves": ["#005E5E", "#00797F", "#1EBEC7", "#90DFE3"],
    "seagrass": ["#365E17", "#4B8320", "#76BC21", "#B1DC6B"],
    "urchin": ["#3B469A", "#5761C0", "#737BE6", "#A8B8FF"],
    "crustacean": ["#853B00", "#DB6015", "#FF8400", "#ffab38"],
    "coral": ["#901200", "#b71300", "#db2207", "#ff6c57"],
}

def display_color_gradient(colors, n=100):
    """Generates and displays a gradient based on a list of colors."""
    cmap = LinearSegmentedColormap.from_list("Custom", colors, N=n)
    gradient = np.linspace(0, 1, n)
    gradient = np.vstack((gradient, gradient))
    fig, ax = plt.subplots(figsize=(6, 2))
    ax.imshow(gradient, aspect='auto', cmap=cmap)
    ax.set_axis_off()
    plt.show()

def get_interpolated_palette_values(name, n=100):
    """Returns interpolated values and colors from the specified NMFS color palette."""
    if name in nmfs_color_palettes:
        return np.linspace(0, 1, n), nmfs_color_palettes[name]
    else:
        raise ValueError("Invalid palette name. Available options are: {}".format(list_nmfs_palettes()))

def get_palette_colors(name, n=100):
    """Returns a list of interpolated colors as hex codes from the specified NMFS palette."""
    _, colors = get_interpolated_palette_values(name, n)
    return colors

def create_nmfs_colormap(name, n=100):
    """Creates a matplotlib colormap object from the specified NMFS palette."""
    _, colors = get_interpolated_palette_values(name, n)
    return LinearSegmentedColormap.from_list(name, colors, N=n)

def list_nmfs_palettes():
    """Returns a list of available NMFS color palettes."""
    return list(nmfs_color_palettes.keys())


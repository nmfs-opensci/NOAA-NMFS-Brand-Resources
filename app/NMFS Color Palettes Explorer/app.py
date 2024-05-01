import streamlit as st
from plotnine import ggplot, aes, geom_point, theme_bw, scale_color_manual, labs
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
# Define the nmfs color palettes
nmfs_palettes = {
    "oceans": ["#001743", "#002364", "#003087", "#0085CA", "#5EB6D9", "#C6E6F0"],
    "waves": ["#005E5E", "#00797F", "#1EBEC7", "#90DFE3"],
    "seagrass": ["#365E17", "#4B8320", "#76BC21", "#B1DC6B"],
    "urchin": ["#3B469A", "#5761C0", "#737BE6", "#A8B8FF"],
    "crustacean": ["#853B00", "#DB6015", "#FF8400", "#ffab38"],
    "coral": ["#901200", "#b71300", "#db2207", "#ff6c57"],
}

def display_palette(colors, n=100):
    """Generates and displays a gradient based on a list of colors."""
    # Create a color map
    cmap = LinearSegmentedColormap.from_list("Custom", colors, N=n)
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    
    # Plotting
    fig, ax = plt.subplots(figsize=(6, 2))
    ax.imshow(gradient, aspect='auto', cmap=cmap)
    ax.set_axis_off()
    st.pyplot(fig)

def nmfs_palette(name, n=100):
    """Returns a list of interpolated colors from the specified nmfs palette."""
    if name in nmfs_palettes:
        return np.linspace(0, 1, n), nmfs_palettes[name]
    else:
        raise ValueError("Invalid nmfs palette name. Available options are: {}".format(list(nmfs_palettes.keys())))

def show_palette_and_plot(palette_name):
    """Displays the named palette with 10 interpolations and plot."""
    display_palette(nmfs_palettes[palette_name], n=10)
    
    p = (
        ggplot(penguins_clean, aes(x='flipper_length_mm', y='body_mass_g', color='species')) +
        geom_point(size=4) +
        labs(y="Body Mass (g)", x="Flipper Length (mm)") +
        theme_bw() +
        scale_color_manual(name=palette_name, values=nmfs_palettes[palette_name])  # Use selected palette
    )
    # Convert ggplot object to Matplotlib figure
    fig = p.draw()
    # Display the Matplotlib figure
    st.pyplot(fig)

penguins = sns.load_dataset("penguins")
# Remove rows with missing values
penguins_clean = penguins.dropna()

# Streamlit app
st.title("NMFS Color Palettes Explorer")
st.write("""
A Python color palette and palette explorer using NOAA Fisheries branding colors.
""")

# Sidebar for user inputs
with st.sidebar:
    st.title("NMFS Color Palettes Explorer")
    #st.subheader("Select Palette:")
    #palette_name = st.selectbox("Select Palette",list(nmfs_palettes.keys()), index=0)
    st.write("""
    For a collection of color palettes, logos, and icons and more information
    - Visit the GitHub repository: [NOAA NMFS Brand Resources](https://github.com/MichaelAkridge-NOAA/NOAA-NMFS-Brand-Resources)
    - For R user, view: [nmfspalette](https://github.com/nmfs-fish-tools/nmfspalette)
    """)
    st.subheader("View Color Palettes")
    for name in nmfs_palettes:
        st.subheader(name)
        display_palette(nmfs_palettes[name])

# Show the selected palette and plot
st.subheader("Select Palette:")
palette_name = st.selectbox("Select Palette",list(nmfs_palettes.keys()), index=0)
st.subheader(palette_name)
show_palette_and_plot(palette_name)


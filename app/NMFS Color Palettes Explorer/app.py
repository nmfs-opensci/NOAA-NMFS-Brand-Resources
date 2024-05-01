import streamlit as st
from plotnine import ggplot, aes, geom_point, theme_bw, scale_color_manual, labs
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
st.set_page_config(page_title="NMFS Color Palettes Explorer")
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
    if palette_name not in nmfs_palettes:
        st.error("Invalid palette name selected.")
        return

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

def show_boxplot(data, x_var, y_var, hue_var, palette_name):
    """Displays a boxplot for the given dataset themed by the selected palette."""
    palette = nmfs_palettes.get(palette_name, ["#555555"])  # Default grey if not found
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=x_var, y=y_var, hue=hue_var, palette=palette, data=data)
    sns.despine(offset=10, trim=True)
    st.pyplot(plt.gcf())

def show_lineplot(data, x_var, y_var, hue_var, palette_name):
    """Displays a line plot for the given dataset themed by the selected palette."""
    palette = nmfs_palettes.get(palette_name, ["#555555"])  # Default grey if not found
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=x_var, y=y_var, hue=hue_var, palette=palette, data=data)
    plt.title(f"{y_var.capitalize()} over {x_var.capitalize()} by {hue_var.capitalize()}")
    plt.grid(True)
    sns.despine(offset=10, trim=True)
    st.pyplot(plt.gcf())

with st.sidebar:
    st.title("NMFS Color Palettes Explorer")
    st.write("""
    For a collection of color palettes, logos, and icons and more information
    - Visit the GitHub repository: [NOAA NMFS Brand Resources](https://github.com/MichaelAkridge-NOAA/NOAA-NMFS-Brand-Resources)
    - For R user, view: [nmfspalette](https://github.com/nmfs-fish-tools/nmfspalette)
    """)
    st.subheader("View Color Palettes")
    for name in nmfs_palettes:
        st.subheader(name)
        display_palette(nmfs_palettes[name])

# Load the penguins dataset
penguins = sns.load_dataset("penguins")
penguins_clean = penguins.dropna()

# Streamlit app setup
st.title("NMFS Color Palettes Explorer")
st.write("A Python color palette and palette explorer using NOAA Fisheries branding colors.")

# Main page setup for plot selection
plot_type = st.selectbox("Choose Plot Type", ["Palette Plot", "Boxplot", "Line Plot"], index=0)
if plot_type == "Palette Plot":
    palette_name = st.selectbox("Select Palette", list(nmfs_palettes.keys()), index=0)
    show_palette_and_plot(palette_name)
elif plot_type == "Boxplot":
    palette_name = st.selectbox("Select Palette for Boxplot", list(nmfs_palettes.keys()), index=0)
    x_var = st.selectbox("Select X-axis Variable", ['species', 'island', 'sex'], index=0)
    y_var = st.selectbox("Select Y-axis Variable", ['body_mass_g', 'flipper_length_mm', 'bill_length_mm', 'bill_depth_mm'], index=0)
    hue_var = st.selectbox("Select Hue Variable (optional)", ['None', 'species', 'island', 'sex'], index=0)
    hue_var = None if hue_var == 'None' else hue_var
    show_boxplot(penguins_clean, x_var, y_var, hue_var, palette_name)
elif plot_type == "Line Plot":
    palette_name = st.selectbox("Select Palette for Line Plot", list(nmfs_palettes.keys()), index=0)
    x_var = st.selectbox("Select X-axis Variable for Line Plot", ['body_mass_g', 'flipper_length_mm', 'bill_length_mm', 'bill_depth_mm'], index=0)
    y_var = st.selectbox("Select Y-axis Variable for Line Plot", ['flipper_length_mm', 'body_mass_g', 'bill_length_mm', 'bill_depth_mm'], index=0)
    hue_var = st.selectbox("Select Hue Variable for Line Plot", ['species', 'island', 'sex'], index=0)
    show_lineplot(penguins_clean, x_var, y_var, hue_var, palette_name)


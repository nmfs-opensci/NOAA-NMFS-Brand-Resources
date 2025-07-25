---
editor_options: 
  markdown: 
    wrap: 95
---

Notes on \_brand.yml for Shiny in R

Resources:

-   [Slides from presentation at Posit Shiny Conference
    2025](https://slides.garrickadenbuie.com/brand-yml-shiny/#/title-slide)

-   [Bslib and Shiny
    Overview](https://shiny.posit.co/blog/posts/bslib-0.9.0/?_gl=1*1punm69*_ga*MTg2NTYwNDY0MC4xNzQ4OTg3NDk1*_ga_2C0WZ1JHG0*czE3NDg5ODc0OTUkbzEkZzEkdDE3NDg5ODg2NzQkajYwJGwwJGgw)

-   [HTML Theming -
    Quarto](https://quarto.org/docs/output-formats/html-themes.html#sass-variables): useful for
    syntax for defaults

    -   Defaults are derived from Sass variables
    -   Found Gemini helpful in identifying the specific defaults needed

-   \_brand.yml [repository](https://github.com/posit-dev/brand-yml?tab=readme-ov-file)

-   Demo from Posit team: [video](https://www.youtube.com/watch?v=U48y0_yzEPY)

Notes:

-   Need to check {bslib} version

    -   Check which versions you are running -\> needs to be 0.9

-   Google fonts

    -   To install new ones

    ```{r}
    sysfonts::font_add_google(“font name goes here”)
    # check loading
    Sysfonts::font_families() 
    ```

-   Logo functionality seemingly not yet designed for RShiny so current workaround at top of
    ui.R

    ```{r}
    tagList(
    # Custom header with logo
      div(
        class = "container-fluid",
        style = "margin: 10px 0; display: flex; justify-content: space-between; align-items: center;",

    # Left side blank with a placeholder
      div(style = "visibility: hidden;", "Placeholder"),

    # Right side will have NOAA logo
      div(
    # note do not include www folder in file path or link will appear broken
        img(src = "logos/NOAA_FISHERIES_logoH_web.png", height = "60px", alt = "NOAA Fisheries Logo")
      )
    ),

    #rest of ui.R follows here
      
    ```

-   \_brand.yml should live in the base of the repository your app is built in, either in the
    ui.R or the global.R dependent on how your app is set-up

    -   ui.R

    ```{r}
    ui <- page_sidebar(title = "Dashboard Name", theme = bs_theme(brand = "titled_brand.yml"),
    ... the rest of your app ... ) 
    ```

    -   global.R

    ```{r}
    # if file is titled _brand.yml and in main directory the file will automatically be found
    library(bslib)
    theme <- bslib::bs_theme()
    ```

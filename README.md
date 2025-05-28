# Hirst Dot Painting

This project is a Python recreation of artist Damien Hirst's iconic dot paintings using the `turtle` graphics library and color extraction with `colorgram`. It creates a colorful grid of randomly selected dots using colors extracted from a real image.

## Project Overview
* Extracts a palette of colors from an image (`image.jpg`) using the `colorgram` library.
* Uses the `turtle` module to draw a 10x10 grid of colored dots.
* Each dot is drawn using a random color from the extracted palette to mimic Hirst’s style.

## Requirements
* Python 3.x
* `turtle`
* `cologram.py`

## How It Works
1. Extracts 30 dominant colors from a reference image.
2. Stores the RGB values in a list.
3. Uses the turtle graphics module to draw dots on the screen in a grid layout.
4. Each dot color is chosen randomly from the extracted color list.

## Files
* `image.jpg`: The source image used for color extraction.
* `hirst_painting.py`: The main script that generates the painting.

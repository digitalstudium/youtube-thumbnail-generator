# YouTube Thumbnail Generator
This python script can create YouTube video thumbnails with a text on them.
Image for thumbnail will be downloaded from https://source.unsplash.com/

This script works on Ubuntu operating system out of the box.
In order to make it work on other operating systems, you should change a path to font in 
`main.py` script from `/usr/share/fonts/truetype/ubuntu/Ubuntu-BI.ttf` to something else. 
## Installation
```bash
pip install -r requirements.txt
```
## Usage
```bash
python3 main.py <theme> <text on image>
```
## Configurable parameters inside `main.py` script:
```
background_width = 1280
background_height = 720
background_color = "green"
background_opacity = 128  # number from 0 to 255, where 0 is transparent and 255 is opaque
background_margin = 70

font_path = '/usr/share/fonts/truetype/ubuntu/Ubuntu-BI.ttf'
font_size = 135
font_colors = ["orange", "yellow", "purple", "white"]

text_width = 10  # in symbols

destination_folder = "./"
```
## Example
### Command
```bash
python3 main.py yoga "Asanas for beginners"
```
### Results
As a result you will get 4 images in a folder containing the script:
```
blue_yoga_thumbnail.png
lime_yoga_thumbnail.png
white_yoga_thumbnail.png
yellow_yoga_thumbnail.png
```
![Result image 1](example_images/blue_yoga_thumbnail.png?raw=true "Blue")
![Result image 2](example_images/lime_yoga_thumbnail.png?raw=true "Lime")
![Result image 3](example_images/yellow_yoga_thumbnail.png?raw=true "Yellow")
![Result image 4](example_images/white_yoga_thumbnail.png?raw=true "White")
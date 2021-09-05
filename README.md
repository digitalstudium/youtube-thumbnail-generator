# YouTube Thumbnail Generator
## Description
This program is a python script which can create YouTube video thumbnails with a text covering them.
The result of this script looks like this:

![Result image 2](example_images/lime_yoga.png?raw=true "Lime")

Image for thumbnail will be downloaded from https://source.unsplash.com/

This script works on Ubuntu operating system out of the box.
In order to make it work on other operating systems, you should change a path to font in 
`[font]` section of `config.ini` from `/usr/share/fonts/truetype/ubuntu/Ubuntu-BI.ttf` to correct value. 
## Installation
```bash
pip install -r requirements.txt
```
## Configurable parameters inside `config.ini` file:
```ini
[background]
width = 1280
height = 720
color = green
# opacity - number from 0 to 255, where 0 is transparent and 255 is opaque
opacity = 128
margin = 70

[font]
path = /usr/share/fonts/truetype/ubuntu/Ubuntu-BI.ttf
size = 135
colors = blue,yellow,white,lime

[other]
# max characters in one line of text
text_width = 10
# where to save images
destination_folder = ./
```
## Usage
```bash
python3 main.py <theme> <text on image>
```
## Example
### Command
```bash
python3 main.py yoga "Asanas for beginners"
```
### Results
As a result you will get 4 images in a folder containing the script:
```
blue_yoga.png
lime_yoga.png
white_yoga.png
yellow_yoga.png
```
![Result image 1](example_images/blue_yoga.png?raw=true "Blue")
![Result image 2](example_images/lime_yoga.png?raw=true "Lime")
![Result image 3](example_images/yellow_yoga.png?raw=true "Yellow")
![Result image 4](example_images/white_yoga.png?raw=true "White")
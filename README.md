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
## Example
### Command
```bash
python3 main.py yoga "Asanas for beginners"
```
### Results
As a result you will get 4 images in a folder containing the script:
```
orange_yoga_thumbnail.png
purple_yoga_thumbnail.png
white_yoga_thumbnail.png
yellow_yoga_thumbnail.png
```
![Result image 1](example_images/orange_yoga_thumbnail.png?raw=true "Orange")
![Result image 2](example_images/purple_yoga_thumbnail.png "Purple")
![Result image 3](example_images/yellow_yoga_thumbnail.png "Yellow")
![Result image 4](example_images/white_yoga_thumbnail.png "White")
#!/usr/bin/env python3

import sys
import textwrap
from io import BytesIO
from urllib.request import urlopen
import configparser

from PIL import Image, ImageDraw, ImageFont, ImageColor

# read config
config = configparser.ConfigParser()
config.read('config.ini')

# handle user input
theme = sys.argv[1]
text = sys.argv[2].upper()

# split text into lines
wrapper = textwrap.TextWrapper(width=config.getint('other', 'text_width'), break_long_words=False)
text_on_image = wrapper.fill(text=text)

# download image and create corresponding object
background_image_url = f"https://source.unsplash.com/" \
                       f"{config.getint('background', 'width')}x{config.getint('background', 'height')}/?{theme}"
image_data = BytesIO(urlopen(background_image_url).read())
image = Image.open(image_data).convert("RGBA")

# create background object
background_shape = [(config.getint('background', 'margin'), config.getint('background', 'margin')),
                         (config.getint('background', 'width') - config.getint('background', 'margin'),
                          config.getint('background', 'height') - config.getint('background', 'margin'))]
background = Image.new('RGBA', image.size, (0, 0, 0, 0))

# create font object
font = ImageFont.truetype(config['font']['path'], config.getint('font', 'size'))

# draw and save images
for font_color in config['font']['colors'].split(","):
    draw = ImageDraw.Draw(background)
    draw.rectangle(background_shape,
                   fill=ImageColor.getrgb(config['background']['color']) + (config.getint('background', 'opacity'),))
    font_width, font_height = draw.textsize(text_on_image, font=font)
    draw.multiline_text(((config.getint('background', 'width') - font_width) / 2,
                         (config.getint('background', 'height') - font_height) / 2), text_on_image,
                        font=font, fill=ImageColor.getrgb(font_color), align="center")

    final_image = Image.alpha_composite(image, background)
    final_image.save(f"{config['other']['destination_folder']}{font_color}_" + theme + ".png", 'PNG')

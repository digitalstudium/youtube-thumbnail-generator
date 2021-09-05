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

# initialize vars
theme = sys.argv[1]
background_image_url = f"https://source.unsplash.com/" \
                       f"{config.getint('background', 'width')}x{config.getint('background', 'height')}/?{theme}"
image_data = BytesIO(urlopen(background_image_url).read())
text_background_shape = [(config.getint('background', 'margin'), config.getint('background', 'margin')),
                         (config.getint('background', 'width') - config.getint('background', 'margin'),
                          config.getint('background', 'height') - config.getint('background', 'margin'))]

# text parameters
font = ImageFont.truetype(config['font']['path'], config.getint('font', 'size'))
text = sys.argv[2].upper()
wrapper = textwrap.TextWrapper(width=config.getint('other', 'text_width'))
word_list = wrapper.wrap(text=text)
text_on_image = '\n'.join(word_list)
result_file_name = f"{theme}_thumbnail.png"

# draw images
for font_color in config['font']['colors'].split(","):
    image = Image.open(image_data)
    image = image.convert("RGBA")
    overlay = Image.new('RGBA', image.size, (0, 0, 0) + (0,))
    draw = ImageDraw.Draw(overlay)
    draw.rectangle(text_background_shape,
                   fill=ImageColor.getrgb(config['background']['color']) + (config.getint('background', 'opacity'),))
    font_width, font_height = draw.textsize(text_on_image, font=font)
    draw.multiline_text(((config.getint('background', 'width') - font_width) / 2,
                         (config.getint('background', 'height') - font_height) / 2), text_on_image,
                        font=font, fill=ImageColor.getrgb(font_color), align="center")

    image = Image.alpha_composite(image, overlay)
    img = image.convert("RGB")
    # save image
    image.save(f"{config['other']['destination_folder']}{font_color}_" + result_file_name, 'PNG')

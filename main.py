#!/usr/bin/env python3

import sys
import textwrap
from io import BytesIO
from urllib.request import urlopen

from PIL import Image, ImageDraw, ImageFont, ImageColor

# configurable parameters
background_width = 1280
background_height = 720
background_color = "green"
background_opacity = 128  # number from 0 to 255, where 0 is transparent and 255 is opaque
background_margin = 70

font_path = '/usr/share/fonts/truetype/ubuntu/Ubuntu-BI.ttf'
font_size = 135
font_colors = ["blue", "yellow", "white", "lime"]

text_width = 10  # in symbols

destination_folder = "./"

# other parameters
# background parameters
theme = sys.argv[1]
background_image_url = f"https://source.unsplash.com/{background_width}x{background_height}/?{theme}"
image_data = BytesIO(urlopen(background_image_url).read())
text_background_shape = [(background_margin, background_margin),
                         (background_width - background_margin, background_height - background_margin)]

# text parameters
font = ImageFont.truetype(font_path, font_size)
text = sys.argv[2].upper()
wrapper = textwrap.TextWrapper(width=text_width)
word_list = wrapper.wrap(text=text)
text_on_image = '\n'.join(word_list)
result_file_name = f"{theme}_thumbnail.png"

# draw images
for font_color in font_colors:
    image = Image.open(image_data)
    image = image.convert("RGBA")
    overlay = Image.new('RGBA', image.size, (0, 0, 0) + (0,))
    draw = ImageDraw.Draw(overlay)
    draw.rectangle(text_background_shape, fill=ImageColor.getrgb(background_color) + (background_opacity,))
    font_width, font_height = draw.textsize(text_on_image, font=font)
    draw.multiline_text(((background_width - font_width) / 2, (background_height - font_height) / 2), text_on_image,
                        font=font, fill=ImageColor.getrgb(font_color), align="center")

    image = Image.alpha_composite(image, overlay)
    img = image.convert("RGB")
    # save image
    image.save(f"{destination_folder}{font_color}_" + result_file_name)

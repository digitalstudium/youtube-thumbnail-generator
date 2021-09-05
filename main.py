#!/usr/bin/env python3

import sys
import time
import textwrap
import io

from PIL import Image, ImageDraw, ImageFont, ImageColor
import requests

# background parameters
width = 1280
height = 720
theme = "code"
background_image_url = f"https://source.unsplash.com/{width}x{height}/?{theme}"
image_data = io.BytesIO(requests.get(background_image_url, stream=True).content)
text_background_color = "green"
margin = 70
text_background_shape = [(margin, margin), (width - margin, height - margin)]

# text parameters
font_path = '/usr/share/fonts/truetype/ubuntu/Ubuntu-BI.ttf'
font_size = 135
font_colors = ["orange", "yellow", "purple", "white"]
text = sys.argv[1].upper()
wrapper = textwrap.TextWrapper(width=10)
word_list = wrapper.wrap(text=text)
text_on_image = '\n'.join(word_list)
result_file_name = f"thumbnail-{round(time.time())}.png"

# draw images
for font_color in font_colors:
    image = Image.open(image_data)
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(image)
    draw.rectangle(text_background_shape, fill=ImageColor.getrgb(text_background_color))
    font_width, font_height = draw.textsize(text_on_image, font=font)
    draw.multiline_text(((width - font_width) / 2, (height - font_height) / 2), text_on_image, font=font,
                        fill=ImageColor.getrgb(font_color), align="center")

    # save image
    image.save(f"{font_color}_" + result_file_name, 'PNG')

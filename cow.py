import os
import warnings
import argparse

from PIL import (
    Image,
    ImageDraw,
    ImageFont,
)

name = 'Vera'
age = '22'

BIRTHDAY_GREETINGS = r"""
  ________________________________
/    Happy Birthday,   {0}  ! \
\    You are now {1} years old! /
  ================================
                \
                 \
                   ^__^
                   (oo)\_______
                   (__)\       )\/\
                       ||----w |
                       ||     ||
"""

FONT_FILE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'fonts', 'mono', 'Roboto-Mono', 'Roboto-Mono-700.ttf'
)

FONT_SIZE = 30


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type = str, required = False)
    parser.add_argument('--age', type = str, required = False)
    parser.add_argument ('--save-path', type = str, required = False)

    args = parser.parse_args()

    if args.name:
        name = args.name
    if args.age:
        age = args.age

    image = Image.new(
        mode='RGB',
        size=(650, 500),
        color=(255, 255, 255),
    )

    draw = ImageDraw.Draw(image)

    if os.path.isfile(FONT_FILE_PATH):
        font = ImageFont.truetype(FONT_FILE_PATH, FONT_SIZE)
    else:
        font = None

        warnings.warn(f'No font file "{FONT_FILE_PATH}" found!')

    draw.text(
        xy=(0, 0),
        text=BIRTHDAY_GREETINGS.format(name, age),
        font=font,
        fill=(0, 0, 0),
    )
    if args.save_path:
        image.save(args.save_path)
    else:
        image.save('happy_birthday_from_the_cow.png')
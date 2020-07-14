import os
from os import path
import sys
from PIL import Image

'''
JPG to PNG converter. Supply absolute or relative path as command line arguments
in format jpg_path png_path to program. If png_path does not exist, new directory
will be created.
'''

try:
    jpg_path = sys.argv[1]
    png_path = sys.argv[2]
except IndexError as err:
    print("Two command line arguments, jpg path and png path, needed")
    raise err

jpgs = os.listdir(jpg_path)

# print(path.isdir(jpg_path))

for convert_me in jpgs:
    img_path = jpg_path + '/' + convert_me
    print(img_path)
    img = Image.open(img_path)
    convert_me = convert_me[:convert_me.find('.')]
    convert_me += '.png'
    print(convert_me)
    img_path = png_path + '/' + convert_me
    if not path.isdir(png_path):
        os.mkdir(png_path)
    img.save(img_path, "png")

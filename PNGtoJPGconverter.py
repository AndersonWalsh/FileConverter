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
except IndexError:
    print("Two command line arguments, jpg path and png path, needed")
    raise

jpgs = os.listdir(jpg_path)

if not path.isdir(png_path):
    os.mkdir(png_path)

for convert_me in jpgs:
    img_path = jpg_path + '/' + convert_me
    img = Image.open(img_path)
    convert_me = convert_me[:convert_me.find('.')]
    convert_me += '.png'
    img_path = png_path + '/' + convert_me
    img.save(img_path, "png")

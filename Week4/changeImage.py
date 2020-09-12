#!/usr/bin/env python3
from PIL import Image
import os

path = os.path.expanduser('~')+"/supplier-data/images/"

for infile in os.listdir(path):
  if '.tiff' in infile:
    im = Image.open(path+infile)
    imgname = os.path.splitext(infile)[0]
    im.resize((600,400)).convert("RGB").save(path+infile+ ".jpeg")
    im.close()


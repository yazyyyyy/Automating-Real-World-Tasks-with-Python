
#!/usr/bin/env python3
from PIL import Image
import os

old_path = os.path.expanduser('~')+"/images/"
new_path = "/opt/icons/"

for infile in os.listdir(old_path):
  if '.' not in infile:
    im = Image.open(infile)
    im.rotate(-90).resize((128,128)).convert("RGB").save(new_path+infile,"jpeg")
    im.close()


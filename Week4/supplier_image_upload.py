#!/usr/bin/env python3
import requests
import os

url = "http://35.239.218.10/upload/"
path = os.path.expanduser('~')+"/supplier-data/images/"

for infile in os.listdir(path):
  with open(path+infile, 'rb') as opened:
      r = requests.post(url, files={'file': opened})

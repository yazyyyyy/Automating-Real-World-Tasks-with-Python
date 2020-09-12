#! /usr/bin/env python3

import os
import requests
import json

txtpath = os.path.expanduser('~')+"/supplier-data/descriptions/"
imgpath = os.path.expanduser('~')+"/supplier-data/images"

infos = []
infolist = ['name', 'weight', 'description']

response = requests.get("http://35.239.218.10/fruits/")
print(response.status_code)

for txtfile in os.listdir(txtpath):
  if '.txt' in txtfile:
    infodict = {}
    with open(txtpath+txtfile, 'r') as file:
      for key in infolist:
        if key == 'weight':
          weight = file.readline().split()[0]
          infodict[key] = int(weight)
        else:
          infodict[key] = file.readline()
      imgfile = os.path.splitext(txtfile)[0]+'.jpeg'
      infodict['image_name'] = imgfile
      infos+=[infodict]
      response = requests.post("http://35.239.218.10/fruits/", data=infodict)
      print(response.status_code)
      print(response.request.url)

with open('infos.json', 'w') as info_json:
    json.dump(infos,info_json)


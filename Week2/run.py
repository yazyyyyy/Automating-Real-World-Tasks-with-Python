#! /usr/bin/env python3

import os
import requests
import json

path = "/data/feedback/"
feedbacks = []
reviewlist = ['title', 'name', 'date', 'feedback']

response = requests.get("http://34.68.46.37/feedback/")
print(response.ok)

for txtfile in os.listdir(path):
  if '.txt' in txtfile:
    reviewdict = {}
    with open(path+txtfile, 'r') as file:
      for key in reviewlist:
        reviewdict[key] = file.readline()
      feedbacks+=[reviewdict]
      response = requests.post("http://34.68.46.37/feedback/", data=reviewdict)
      print(response.status_code)
      print(response.request.url)

with open('feedbacks.json', 'w') as feedback_json:
    json.dump(feedbacks,feedback_json)



        

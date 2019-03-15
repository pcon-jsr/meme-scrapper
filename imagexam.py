# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 16:15:00 2019

@author: ADARSH ANURAG
"""
import pandas as pd
import requests
df = pd.read_csv("memedroid.csv")
for x in df['image']:
    overlay=True
    url=x
    payload = {'url': url,
           'isOverlayRequired':overlay,
           'apikey': '9ec509657e88957',
           'language': 'eng',
          }
    r = requests.post('https://api.ocr.space/parse/image',data=payload,)
    print(r.status_code, r.reason)
    result = r.json()
    print(['ParsedResults'][0]['ParsedText'])
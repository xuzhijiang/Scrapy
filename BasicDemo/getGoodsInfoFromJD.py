#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import requests

url = 'https://item.jd.com/2967929.html'
try:
    r = requests.get(url)
    r.raise_for_status()
    print(type(r))
    print(type(r.headers))
    print(r.headers)
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print('Get Goods Info failed!')
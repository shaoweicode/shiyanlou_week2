#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:23:54 2018

@author: python
"""

#zidian={1:'hello','2':"nihao"}
#for key ,value in zidian.items():
#    print(key,value)

import os
import json
file_dir='/home/python/shiyanlou_week2/files'
l=[]
title_list=[]
for root ,dirs,files in os.walk(file_dir):
    for file in files:
        if os.path.splitext(file)[1]=='.json':
            l.append(os.path.join(root,file))
for page in l:        
    with open(page) as file:
        article = json.load(file)
        title_list.append(article['title'])



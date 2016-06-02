#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-02 20:37:16
# @Author  : Libra (69066656@qq.com)
# @Link    : https://github.com/Libra28
import json,pickle

count = 0

with open('items.txt','rb') as file:
    for i in range(1,9):
        r = pickle.load(file)
        for key in r:
            if key['itemid'] == '1865348296':
                print key['item_desc'].encode('gb2312')
        break


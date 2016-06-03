#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-02 20:37:16
# @Author  : Libra (69066656@qq.com)
# @Link    : https://github.com/Libra28
"""
设置折扣价格
"""
import requests
import json
import time
from get_token import get_file_token
from cate_items import cate_items


cate_id = 81018763
discount = 0.38
access_token = get_file_token()
items = cate_items(str(cate_id))


for item in items:
    item_id = item[0]
    price = round(float(item[1]) * discount)
    url = 'https://api.vdian.com/api?param={"itemid":"%s","price":"%d","quantity":"999999","start_time":"2016-06-2 15:23:00","end_time":"2016-06-27 14:58:00"}&public={"method":"vdian.seckill.item.set","access_token":"%s","version":"1.0","format":"json"}' % (
        item_id, price, access_token)
    r = requests.post(url).text
    if r == '{"status":{"status_code":0,"status_reason":""},"result":true}':
        pass
    else:
        print item_id
        print r.encode('gb2312')

#itemid = 1865348296

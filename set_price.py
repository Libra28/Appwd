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
from mem_token import mem_token
from manage_url import manage_url
from find_cate_items import find_cate_items


cate_id = 81018763
discount = 0.38
access_token = mem_token()
items = find_cate_items(str(cate_id))


for item in items:
    item_id = item[0]
    price = round(float(item[1]) * discount)
    param = '{"itemid":"%s","price":"%d","quantity":"999999","start_time":"2016-06-2 15:23:00","end_time":"2016-06-27 14:58:00"}' % (
        item_id, price)
    public = '{"method":"vdian.seckill.item.set","access_token":"%s","version":"1.0","format":"json"}' % access_token
    r = menage_url('post', param, public).text
    if r == '{"status":{"status_code":0,"status_reason":""},"result":true}':
        pass
    else:
        print item_id
        print r.encode('gb2312')

#itemid = 1865348296

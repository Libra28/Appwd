#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-02 20:37:16
# @Author  : Libra (69066656@qq.com)
# @Link    : https://github.com/Libra28
"""
获取全部商品
"""
import requests
import json
import pickle
from mem_token import mem_token
access_token = mem_token()


def get_items():
    page_num = 1
    item_num = 1
    with open('items.txt', 'wb') as file:
        while True:
            url = 'https://api.vdian.com/api?param={"page_num":%d,"page_size":200}&public={"method":"vdian.item.list.get","access_token":"%s","version":"1.0","format":"json"}' % (
                page_num, access_token)

            r = json.loads(requests.get(url).text)
            item_num = r['result']['item_num']
            items = r['result']['items']
            if item_num == 0:
                break
            pickle.dump(items, file)
            page_num += 1


if __name__ == '__main__':
    get_items()

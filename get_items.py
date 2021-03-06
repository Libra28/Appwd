#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-02 20:37:16
# @Author  : Libra (69066656@qq.com)
# @Link    : https://github.com/Libra28
"""
获取指定商品并写入items.txt(Demo)
"""
import requests
import json
import pickle
from mem_token import mem_token


def get_items(key=[]):
    access_token = mem_token()
    page_num = 1
    item_num = 1
    items = []

    with open('items.txt', 'wb') as file:
        while True:
            url = 'https://api.vdian.com/api?param={"page_num":%d,"page_size":200}&public={"method":"vdian.item.list.get","access_token":"%s","version":"1.0","format":"json"}' % (
                page_num, access_token)
            t = json.loads(requests.get(url).text, encoding='gbk')
            item_num = t['result']['item_num']
            if item_num == 0:
                break
            if key == []:
                items.extend(t['result']['items'])
                break
            elif key[0] == 'cate_name':
                for item in items:
                    if item['cates'][0]['cate_name'] == key[1]:
                        print item
            elif key[0] == 'cate_id':
                for item in items:
                    if item['cates'][0]['cate_id'] == key[1]:
                        print item
            else key[0] == 'keyword':
                for item in items:
                    if key[1] in item['item_name']:
                        print item
            page_num += 1
        #pickle.dump(item, file)


if __name__ == '__main__':
    get_items(['cate_id', '81018763'])

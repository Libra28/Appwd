#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-02 20:37:16
# @Author  : Libra (69066656@qq.com)
# @Link    : https://github.com/Libra28
"""
获取指定分类所有商品，根据传入的keys返回商品列表items
"""
import json
import pickle


def find_cate_items(cate_id, *args):
    global count
    count = 0
    items = []
    with open('items.txt', 'rb') as file:
        r = pickle.load(file)
        for key in r:
            item = []
            if key['cates'][0]['cate_id'] == cate_id:
                for name in args:
                    item.append(key[name])
                items.append(item)
                count += 1
    return items


if __name__ == '__main__':
    items = find_cate_items('81018763', 'itemid', 'price')
    print items[0], count

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-02 20:37:16
# @Author  : Libra (69066656@qq.com)
# @Link    : https://github.com/Libra28
"""
获取分类商品
"""
import json
import pickle


def cate_items(cate_id):
    global count
    count = 0
    items = []
    with open('items.txt', 'rb') as file:
        for i in range(1, 9):
            r = pickle.load(file)
            for key in r:
                if key['cates'][0]['cate_id'] == cate_id:
                    item = key['item_name'].encode('gb2312')
                    items.append(item)
                    count += 1
    return items

if __name__ == '__main__':
    items = cate_items('81018763')
    line = '15X2C011'
    with open('items2.txt', 'rb') as file:
        line = file.readline()
        for item in items:
            if line.rstrip() in item:
                line = file.readline()
            print line, 'not found'


"""
    with open('items2.txt', 'rb') as file:
        for line in file:
                for item in items:
                    if line in item:
                        break
                print line.rstrip()
"""
# print count,items

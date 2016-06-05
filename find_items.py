#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-02 20:37:16
# @Author  : Libra (69066656@qq.com)
# @Link    : https://github.com/Libra28
"""
根据关键字组搜索商品（Demo）
"""
import json
import pickle


def find_items():
    items = []
    with open('items3.txt', 'rb') as file2:
        for line in file2:
            if find_current_item(line):
                items.append(line)
    return items


def find_current_item(keyword):
    global count
    count = 0
    with open('items.txt', 'rb') as file:
        r = pickle.load(file)
        for item in r:
            if keyword in item['item_name\r'].encode('UTF-8'):
                count += 1
                return True

if __name__ == '__main__':
    i = find_items()
    #r = find_current_item('15X2C011')
    print count, i

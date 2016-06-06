#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-05 01:53:04
# @Author  : Libra (69066656@qq.com)
# @Link    : https://github.com/Libra28
"""
处理API的URL请求
"""
import json
import requests


def manage_url(func, url='https://api.vdian.com/api', **params):
    r = eval('requests.' + func + '(url, params=params)')
    return r


if __name__ == '__main__':
    from mem_token import mem_token
    access_token = mem_token()
    func = 'get'
    param = '{"page_num": 1, "page_size": 200}'
    public = '{"method": "vdian.item.list.get","access_token":"%s","version": "1.0", "format": "json"}' % access_token
    print json.loads(manage_url(func, param=param, public=public).text)

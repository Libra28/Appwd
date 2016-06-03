#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-02 20:37:16
# @Author  : Libra (69066656@qq.com)
# @Link    : https://github.com/Libra28
"""
获取access_token并写入memcached
"""
import requests
import json


def _create_memcache_client():
    try:
        import pylibmc
        return pylibmc.Client()
    except ImportError:
        import memcache
        return memcache.Client(['127.0.0.1:11211'], debug=0)


def get_token():
    grant_type = 'client_credential'
    appkey = '658077'
    secret = '9a8f69ba222e7e0afc97d27e7c78ec26'
    url = 'https://api.vdian.com/token?grant_type=%s&appkey=%s&secret=%s' % (
        grant_type, appkey, secret)
    r = json.loads(requests.get(url).text)
    return r


def mem_token():
    cache = _create_memcache_client()
    token = cache.get('token')
    if token is None:
        r = get_token()
        token = r['result']['access_token']
        expire_in = r['result']['expire_in']
        cache.set('token', token, expire_in - 500)
    return token

if __name__ == '__main__':
    print mem_token()

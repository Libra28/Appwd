#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-02 20:37:16
# @Author  : Libra (69066656@qq.com)
# @Link    : https://github.com/Libra28
import sae
#sae.add_vendor_dir('vendor')
from mem_token import mem_token


def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    mem = mem_token()
    return [bytes(mem)]

application = sae.create_wsgi_app(app)

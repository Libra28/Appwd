#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-02 20:37:16
# @Author  : Libra (69066656@qq.com)
# @Link    : https://github.com/Libra28

import os
from get_token import get_file_token

response = {"status":{"status_code":10013,"status_reason":"access_token无效(access_token:c160743ab35d7f57d441fcca8142cb3100048975ec 无效) "}}

def catch_error(response):
    status_code = response["status"]["status_code"]
    if status_code == 10013:



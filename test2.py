#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-05 22:10:35
# @Author  : Libra (69066656@qq.com)
# @Link    : https://github.com/Libra28


class screen(object):

    @property
    def f(self):
        return self.w, self.h

    @f.setter
    def f(self, weight, height):
        self.w = weight
        self.h = height

    @property
    def resolution(self):
        return self.w*self.h

s = screen()
s.w = 1024

print s.w
print(s.resolution)

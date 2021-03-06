#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/5/16 13:45
# Author: zhourudong

from __future__ import print_function
import functools


class lazy_property:
    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __get__(self, obj, type_):
        if obj is None:
            return self
        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val


class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    @lazy_property
    def relatives(self):
        # Get all relatives, let's assume that it costs much time.
        relatives = "Many relatives."
        return relatives


def main():
    Jhon = Person('Jhon', "Coder")
    print("name:{0}     Occupation:{1}".format(Jhon.name, Jhon.occupation))
    print(u"Before we access `relatives`:")
    print(Jhon.__dict__)
    print(u"Jhon's relatives: {0}".format(Jhon.relatives))
    print(u"After we've accessed `relatives`:")
    print(Jhon.__dict__)


if __name__ == '__main__':
    main()
	
	
# 返回
'''
name:Jhon     Occupation:Coder
Before we access `relatives`:
{'occupation': 'Coder', 'name': 'Jhon'}
Jhon's relatives: Many relatives.
After we've accessed `relatives`:
{'occupation': 'Coder', 'relatives': 'Many relatives.', 'name': 'Jhon'}
'''

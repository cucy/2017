#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/5/16 12:06
# Author: zhourudong

'''
    delegate a specialized function/method to create instances
    委派一个专门的函数/方法来创建实例
'''


class GreekGetter(object):
    """A simple localizer a la gettext"""

    def __init__(self):
        self.trans = dict(dog="狗", cat="猫")

    def get(self, msgid):
        """We'll punt if we don't have a translation"""
        return self.trans.get(msgid, str(msgid))


class EnglishGetter(object):
    """Simply echoes the msg ids"""

    def get(self, msgid):
        return str(msgid)
    def __repr__(self):
        return 'EnglishGetter 类'


def get_localizer(language="English"):
    """The factory method"""
    languages = dict(English=EnglishGetter, Greek=GreekGetter)
    return languages[language]()


# Create our localizers
e, g = get_localizer(language="English"), get_localizer(language="Greek")
# Localize some text
for msgid in "dog parrot cat bear".split():
    print(e.get(msgid), g.get(msgid))

"""
dog 狗
parrot parrot
cat 猫
bear bear
"""

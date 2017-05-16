#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/5/16 11:18
# Author: zhourudong

"""
实例中具有共享状态的单例
"""

class Borg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state


class YourBorg(Borg):
    pass


if __name__ == '__main__':
    rm1 = Borg()
    rm2 = Borg()

    rm1.state = 'Idle'
    rm2.state = 'Running'   #

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    rm2.state = 'Zombie'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    print('rm1 id: {0}'.format(id(rm1)))
    print('rm2 id: {0}'.format(id(rm2)))

    rm3 = YourBorg()

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))
    print('rm3: {0}'.format(rm3))

# return
"""
rm1: Running
rm2: Running
rm1: Zombie
rm2: Zombie
rm1 id: 139890728880112
rm2 id: 139890728880224
rm1: Init
rm2: Init
rm3: Init
"""

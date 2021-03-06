#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/5/16 14:11
# Author: zhourudong

"""
http://stackoverflow.com/questions/1514120/python-implementation-of-the-object-pool-design-pattern
"""


class ObjectPool:
    def __init__(self, queue, auto_get=False):
        self._queue = queue
        self.item = self._queue.get() if auto_get else None

    def __enter__(self):
        if self.item is None:
            self.item = self._queue.get()
        return self.item

    def __exit__(self, Type, Value, traceback):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None

    def __del__(self):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None


def main():
    try:
        import queue
    except ImportError:
        import Queue as queue

    def test_object(queue):
        pool = ObjectPool(queue, True)
        print("Inside func: {}".format(pool.item))

    sample_queue = queue.Queue()

    sample_queue.put('yam')
    with ObjectPool(sample_queue) as obj:
        print("Inside with: {}".format(obj))
    print("Outside with: {}".format(sample_queue.get()))

    sample_queue.put('sam')
    test_object(sample_queue)
    print("Outside func: {}".format(sample_queue.get()))

    if not sample_queue.empty():
        print(sample_queue.get())


if __name__ == '__main__':
    main()



# result
'''
Inside with: yam
Outside with: yam
Inside func: sam
Outside func: sam
'''
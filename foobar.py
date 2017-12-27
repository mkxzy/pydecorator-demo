#!/usr/bin/env python

import logging
from functools import wraps

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filemode='w')


def use_logging(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.warn("%s is running" % func.__name__)
        return func(*args, **kwargs)
    return wrapper


def foo():
    '''哈哈哈'''
    print('i am foo')


@use_logging
def bar():
    print('i am bar')


foo = use_logging(foo)
print(foo.__name__)
print(foo.__doc__)
foo()
bar()

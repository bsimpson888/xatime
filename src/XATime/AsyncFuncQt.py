#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading
from functools import wraps

from PyQt4.QtCore import QCoreApplication, QEventLoop

__author__ = 'Marco Bartel'


class AsyncFuncQt(object):
    def __init__(self, await=False):
        self.await = await
        self.callFunc = None

    def __call__(self, func):
        self.callFunc = func

        def _return_inner(obj, *args, **kwargs):
            self.ret = self.callFunc(obj, *args, **kwargs)

        def _inner(obj, *args, **kwargs):
            newargs = (obj,) + args
            t = threading.Thread(target=_return_inner, args=newargs, kwargs=kwargs)
            t.start()
            if self.await:
                while t.is_alive():
                    QCoreApplication.processEvents(QEventLoop.AllEvents, 100)
                return self.ret
            else:
                return



        wraps(_inner, func)
        return _inner
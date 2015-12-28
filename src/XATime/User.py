#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Marco Bartel'

class User(object):
    def __init__(self, core=None, USER_ID=None):
        super(User, self).__init__()
        self.core = core
        self.USER_ID = USER_ID
        self.load()

    def load(self):
        sql = """
        SELECT
          USER_ID,
          USERNAME,
          NAME,
          EMAIL
        FROM xatime_user
        where USER_ID='{USER_ID}'
        """.format(USER_ID=self.USER_ID)
        r = self.core.dbQueryDict(sql)
        if len(r) != 0:
            for key, value in r[0].items():
                setattr(self, key, value)

    def save(self):
        sql = """
        update xatime_user
        set USERNAME='{USERNAME}',
        NAME='{NAME}',
        EMAIL='{EMAIL}'
        WHERE USER_ID={USER_ID}
        """.format(
            USERNAME=self.USERNAME,
            NAME=self.NAME,
            EMAIL=self.EMAIL,
            USER_ID=self.USER_ID,
        )
        self.core.dbQueryDict(sql)

#!/usr/bin/python
# -*- coding: utf-8 -*-

import XATime

__author__ = 'Marco Bartel'

class Badge(object):
    def __init__(self, core=None, BADGE_ID=None):
        super(Badge, self).__init__()
        self.core = core
        self.BADGE_ID = BADGE_ID
        self.load()

    def load(self):
        sql = """
        SELECT
          BADGE_ID,
          BADGE_NR,
          USER_ID
        FROM xatime_badges
        where BADGE_ID='{BADGE_ID}'
        """.format(BADGE_ID=self.BADGE_ID)
        r = self.core.dbQueryDict(sql)
        if len(r) != 0:
            for key, value in r[0].items():
                setattr(self, key, value)

    def save(self):
        sql = """
        update xatime_badges
        set BADGE_NR='{BADGE_NR}',
        USER_ID='{USER_ID}'
        WHERE BADGE_ID={BADGE_ID}
        """.format(
            BADGE_NR=self.BADGE_NR,
            USER_ID=self.USER_ID,
            BADGE_ID=self.BADGE_ID
        )
        self.core.dbQueryDict(sql)

    def getUser(self):
        user = XATime.User(core=self.core, USER_ID=self.USER_ID)
        return user



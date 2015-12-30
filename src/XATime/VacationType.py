#!/usr/bin/python
# -*- coding: utf-8 -*-

import XATime

__author__ = 'Marco Bartel'


class VacationType(object):
    def __init__(self, core=None, VACATION_TYPE_ID=None):
        super(VacationType, self).__init__()
        self.core = core
        self.VACATION_TYPE_ID = VACATION_TYPE_ID
        self.load()

    def load(self):
        sql = """
        SELECT
          VACATION_TYPE_ID,
          VACATION_TYPE_GROUP_ID,
          NAME,
          DESCRIPTION,
          MINUTES,
          VOID_DATE
        FROM xatime_vacation_type
        where VACATION_TYPE_ID='{VACATION_TYPE_ID}'
        """.format(VACATION_TYPE_ID=self.VACATION_TYPE_ID)
        r = self.core.dbQueryDict(sql)
        if len(r) != 0:
            for key, value in r[0].items():
                setattr(self, key, value)

    def save(self):
        sql = """update xatime_badges
        set
          VACATION_TYPE_GROUP_ID={VACATION_TYPE_GROUP_ID},
          NAME={NAME},
          DESCRIPTION={DESCRIPTION},
          MINUTES={MINUTES},
          VOID_DATE={VOID_DATE}
        WHERE VACATION_TYPE_ID = {VACATION_TYPE_ID}
        """.format(
            VACATION_TYPE_GROUP_ID=self.VACATION_TYPE_GROUP_ID,
            NAME=self.NAME,
            DESCRIPTION=self.DESCRIPTION,
            MINUTES=self.MINUTES,
            VOID_DATE=self.VOID_DATE,
            VACATION_TYPE_ID=self.VACATION_TYPE_ID,
        )
        self.core.dbQueryDict(sql)
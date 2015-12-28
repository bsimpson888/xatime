#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import datetime
import pymysql
import yaml

import XATime

__author__ = 'Marco Bartel'


class Core(object):
    configPath = "."

    MODUS_KOMMEN, MODUS_GEHEN, MODUS_PAUSE, MODUS_STATUS = range(1, 5, 1)

    @classmethod
    def now(self):
        return datetime.datetime.now().replace(second=0, microsecond=0)

    def __init__(self):
        self.loadConfig()

    def dbQueryDict(self, sql):
        con = pymysql.connect(
                host=self.config["host"],
                user=self.config["user"],
                passwd=self.config["passwd"],
                db=self.config["db"],
        )
        cur = con.cursor(pymysql.cursors.DictCursor)
        cur.execute(sql)

        ret = cur.fetchall()
        con.close()
        return ret

    def loadConfig(self):
        path = os.path.join(self.configPath, "xatime.yaml")
        self.config = yaml.load(open(path))["database"]

    def getBadgeByBadgeNumber(self, BADGE_NR=None):
        sql = """
        select
          BADGE_ID
        from xatime_badges
        where BADGE_NR='{BADGE_NR}'
        """.format(BADGE_NR=BADGE_NR)
        r = self.dbQueryDict(sql)
        if len(r) != 0:
            return XATime.Badge(self, r[0]["BADGE_ID"])
        return None


    def mysqlDateTime(self, dt):
        if dt:
            return "'{dt:%Y-%m-%d  %H:%M:%S}'".format(dt=dt)
        else:
            return "null"
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

    MODUS_KOMMEN = 1
    MODUS_GEHEN = 2
    MODUS_PAUSE = 3
    MODUS_STATUS = 4

    @classmethod
    def now(self):
        return datetime.datetime.now().replace(second=0, microsecond=0)

    @classmethod
    def minutesToHourString(cls, minutes):
        print minutes
        if minutes < 0:
            sign = "-"
            minutes = minutes * -1
        else:
            sign = "+"

        print minutes, sign

        return "{sign}{hours}:{minutes:02}".format(
                sign=sign,
                hours=int(minutes / 60),
                minutes=minutes % 60
        )

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
        print self.config

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

    def mysqlDate(self, d):
        if d:
            return "'{d:%Y-%m-%d}'".format(d=d)
        else:
            return "null"

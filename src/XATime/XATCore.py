#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import pymysql
import yaml

from XATime.Badge import Badge
from XATime.User import User
__author__ = 'Marco Bartel'


class XATCore(object):
    configPath = "."
    Badge = Badge
    User = User

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

    def getBadgeByBadgeNumber(self, badge=None):
        sql = "select ID from xatime_badges where BADGE_NR='{badge}'".format(badge=badge)
        r = self.dbQueryDict(sql)
        if len(r) != 0:
            return XATCore.Badge(self, r[0]["ID"])
        return None

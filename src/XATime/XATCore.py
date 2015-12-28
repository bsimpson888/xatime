#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import pymysql
import yaml

__author__ = 'Marco Bartel'


class XATCore(object):
    configPath = "."
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

    class Badge(object):
        def __init__(self, core=None, ID=None):
            super(XATCore.Badge, self).__init__()
            self.core = core
            self.ID = ID
            self.load()

        def load(self):
            sql = """
            SELECT
              ID,
              BADGE_NR,
              NAME,
              USERNAME,
              EMAIL
            FROM xatime_badges
            where ID='{ID}'
            """.format(ID=self.ID)
            r = self.core.dbQueryDict(sql)
            if len(r) != 0:
                for key, value in r[0].items():
                    setattr(self, key, value)

        def save(self):
            sql = """
            update xatime_badges
            set BADGE_NR='{BADGE_NR}',
            NAME='{NAME}',
            USERNAME='{USERNAME}',
            EMAIL='{EMAIL}'
            WHERE ID={ID}
            """.format(
                BADGE_NR=self.BADGE_NR,
                NAME=self.NAME,
                USERNAME=self.USERNAME,
                EMAIL=self.EMAIL,
                ID=self.ID
            )
            self.core.dbQueryDict(sql)
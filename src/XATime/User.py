#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime

import XATime

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
          EMAIL,
          WORKTIME_GROUP_ID
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
        EMAIL='{EMAIL}',
        WORKTIME_GROUP_ID={WORKTIME_GROUP_ID}
        WHERE USER_ID={USER_ID}
        """.format(
                USERNAME=self.USERNAME,
                NAME=self.NAME,
                EMAIL=self.EMAIL,
                WORKTIME_GROUP_ID=self.WORKTIME_GROUP_ID,
                USER_ID=self.USER_ID,
        )
        self.core.dbQueryDict(sql)

    def getBadge(self):
        sql = """
        select BADGE_ID from xatime_badges where USER_ID = {USER_ID}
        """.format(USER_ID=self.USER_ID)
        r = self.core.dbQueryDict(sql)
        if len(r) != 0:
            badge = XATime.Badge(core=self.core, BADGE_ID=r[0]["BADGE_ID"])
            return badge
        return None

    def newTimeLog(self, mode=None, logTime=None, correction=0, correctionUser=None, correctionDate=None):
        correctionUser = "'{CORRECTION_USER_ID'".format(correctionUser) if correctionUser else "null"
        sql = """
        replace into xatime_time_logs(
        USER_ID,
        LOG_TIME,
        MODE,
        CORRECTION,
        CORRECTION_USER_ID,
        CORRECTION_DATE
        ) values (
        {USER_ID},
        {LOG_TIME},
        {MODE},
        {CORRECTION},
        {CORRECTION_USER_ID},
        {CORRECTION_DATE}
        )
        """.format(
                USER_ID=self.USER_ID,
                LOG_TIME=self.core.mysqlDateTime(logTime),
                MODE=mode,
                CORRECTION=correction,
                CORRECTION_USER_ID=correctionUser,
                CORRECTION_DATE=self.core.mysqlDateTime(correctionDate)
        )
        r = self.core.dbQueryDict(sql)

    def getCurrentMode(self):
        sql = """
        SELECT MODE FROM xatime_time_logs
        WHERE USER_ID = {USER_ID}
        ORDER BY LOG_TIME DESC
        LIMIT 1
        """.format(USER_ID=self.USER_ID)
        r = self.core.dbQueryDict(sql)
        if len(r) == 0:
            return XATime.Core.MODUS_GEHEN
        else:
            return r[0]["MODE"]

    def getSaldoForAccount(self, ACCOUNT_ID):
        sql = """
        SELECT
          ACC1_MINUTES,
          ACC2_MINUTES
        FROM xatime_account_changes
        WHERE USER_ID={USER_ID}
        order by CHANGE_TIME desc
        limit 1
        """.format(
                USER_ID=self.USER_ID
        )
        r = self.core.dbQueryDict(sql)
        if len(r) != 0:
            if ACCOUNT_ID == 1:
                return r[0]["ACC1_MINUTES"]
            elif ACCOUNT_ID == 2:
                return r[0]["ACC2_MINUTES"]
            else:
                return 0
        else:
            return 0

    def assignVacation(self, VACATION_TYPE_ID, AMOUNT, YEAR=None):

        if YEAR is None:
            YEAR = datetime.date.today().year

        vacationType = XATime.VacationType(core=self.core, VACATION_TYPE_ID=VACATION_TYPE_ID)

        VALID_UNTIL = vacationType.VOID_DATE.replace(year=YEAR)

        MINUTES = int(vacationType.MINUTES * AMOUNT)
        while 1:
            if MINUTES >= 480:
                newMinutes = 480
            else:
                newMinutes = MINUTES

            sql = """
            insert into xatime_user_has_vacation(
              USER_ID,
              VACATION_TYPE_ID,
              MINUTES,
              MINUTES_TAKEN,
              VALID_UNTIL,
              CREATED
            ) VALUES (
              {USER_ID},
              {VACATION_TYPE_ID},
              {MINUTES},
              0,
              {VALID_UNTIL},
              now()
            )
            """.format(
                    USER_ID=self.USER_ID,
                    VACATION_TYPE_ID=VACATION_TYPE_ID,
                    MINUTES=newMinutes,
                    VALID_UNTIL=self.core.mysqlDate(VALID_UNTIL)
            )
            self.core.dbQueryDict(sql)

            MINUTES -= newMinutes
            if MINUTES == 0:
                break

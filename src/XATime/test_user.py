#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase

import XATime

__author__ = 'Marco Bartel'


class TestUser(TestCase):
    def setUp(self):
        XATime.Core.configPath = ".."
        self.core = XATime.Core()

    def test_load(self):
        user = XATime.User(core=self.core, USER_ID=1)
        self.assertIsInstance(user, XATime.User)
        self.assertTrue(hasattr(user, "USERNAME"))

    def test_save(self):
        user = XATime.User(core=self.core, USER_ID=1)
        self.assertIsInstance(user, XATime.User)
        oldUSERNAME = user.USERNAME
        user.USERNAME = "hautz"
        user.save()
        user.load()
        self.assertEqual(user.USERNAME, "hautz")
        user.USERNAME = oldUSERNAME
        user.save()
        user.load()
        self.assertEqual(user.USERNAME, oldUSERNAME)

    def test_getCurrentMode(self):
        user = XATime.User(core=self.core, USER_ID=1)
        self.assertIsInstance(user, XATime.User)
        print user.getCurrentMode()

    def test_newLog(self):
        user = XATime.User(core=self.core, USER_ID=1)
        self.assertIsInstance(user, XATime.User)
        user.newTimeLog(mode=XATime.Core.MODUS_KOMMEN, logTime=XATime.Core.now())

    def test_getCurrentSaldo(self):
        user = XATime.User(core=self.core, USER_ID=1)
        self.assertIsInstance(user, XATime.User)
        self.assertIsInstance(user.getSaldoForAccount(2), int)

    def test_assignVacation(self):
        user = XATime.User(core=self.core, USER_ID=1)
        self.assertIsInstance(user, XATime.User)
        user.assignVacation(VACATION_TYPE_ID=1, AMOUNT=22, YEAR=2015)
        user.assignVacation(VACATION_TYPE_ID=17, AMOUNT=3, YEAR=2016)
        user.assignVacation(VACATION_TYPE_ID=5, AMOUNT=1, YEAR=2016)



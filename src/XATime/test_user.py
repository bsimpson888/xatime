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
        user.newLog(mode=XATime.Core.MODUS_KOMMEN, logTime=XATime.Core.now())

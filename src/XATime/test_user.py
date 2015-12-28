#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase

from XATime.XATCore import XATCore

__author__ = 'Marco Bartel'


class TestUser(TestCase):
    def setUp(self):
        XATCore.configPath = ".."
        self.core = XATCore()

    def test_load(self):
        user = XATCore.User(core=self.core, USER_ID=1)
        self.assertIsInstance(user, XATCore.User)
        self.assertTrue(hasattr(user, "USERNAME"))

    def test_save(self):
        user = XATCore.User(core=self.core, USER_ID=1)
        self.assertIsInstance(user, XATCore.User)
        oldUSERNAME = user.USERNAME
        user.USERNAME = "hautz"
        user.save()
        user.load()
        self.assertEqual(user.USERNAME, "hautz")
        user.USERNAME = oldUSERNAME
        user.save()
        user.load()
        self.assertEqual(user.USERNAME, oldUSERNAME)


#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase

from XATime import Core, Badge, User

__author__ = 'Marco Bartel'


class TestBadge(TestCase):
    def setUp(self):
        Core.configPath = ".."
        self.core = Core()

    def test_load(self):
        badge = Core.Badge(core=self.core, BADGE_ID=1)
        self.assertIsInstance(badge, Core.Badge)
        self.assertTrue(hasattr(badge, "BADGE_NR"))

    def test_save(self):
        badge = Core.Badge(core=self.core, BADGE_ID=1)
        self.assertIsInstance(badge, Core.Badge)
        oldUSERNAME = badge.USERNAME
        badge.USERNAME = "tralala"
        badge.save()
        badge.load()
        self.assertEqual(badge.USERNAME, "tralala")
        badge.USERNAME = oldUSERNAME
        badge.save()
        badge.load()
        self.assertEqual(badge.USERNAME, oldUSERNAME)

    def test_getUser(self):
        badge = Badge(core=self.core, BADGE_ID=1)
        self.assertIsInstance(badge, Badge)
        user = badge.getUser()
        self.assertIsInstance(user, User)

        badge2 = user.getBadge()
        self.assertIsInstance(badge2, Badge)
        self.assertEqual(badge.BADGE_ID, badge2.BADGE_ID)



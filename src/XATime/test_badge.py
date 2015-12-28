#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase

from XATime.XATCore import XATCore

__author__ = 'Marco Bartel'


class TestBadge(TestCase):
    def setUp(self):
        XATCore.configPath = ".."
        self.core = XATCore()

    def test_load(self):
        badge = XATCore.Badge(core=self.core, BADGE_ID=1)
        self.assertIsInstance(badge, XATCore.Badge)
        self.assertTrue(hasattr(badge, "BADGE_NR"))

    def test_save(self):
        badge = XATCore.Badge(core=self.core, BADGE_ID=1)
        self.assertIsInstance(badge, XATCore.Badge)
        oldUSERNAME = badge.USERNAME
        badge.USERNAME = "tralala"
        badge.save()
        badge.load()
        self.assertEqual(badge.USERNAME, "tralala")
        badge.USERNAME = oldUSERNAME
        badge.save()
        badge.load()
        self.assertEqual(badge.USERNAME, oldUSERNAME)


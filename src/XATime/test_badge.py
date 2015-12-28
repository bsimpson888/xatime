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
        badge = XATCore.Badge(core=self.core, ID=1)
        self.assertIsInstance(badge, XATCore.Badge)
        self.assertTrue(hasattr(badge, "BADGE_NR"))

    def test_save(self):
        badge = XATCore.Badge(core=self.core, ID=1)
        self.assertIsInstance(badge, XATCore.Badge)
        oldEmail = badge.EMAIL
        badge.EMAIL = "tralala"
        badge.save()
        badge.load()
        self.assertEqual(badge.EMAIL, "tralala")
        badge.EMAIL = oldEmail
        badge.save()
        badge.load()
        self.assertEqual(badge.EMAIL, oldEmail)

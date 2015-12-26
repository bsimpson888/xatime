#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase

from XATime.XATCore import XATCore

__author__ = 'Marco Bartel'


class TestBadge(TestCase):
    def setUp(self):
        self.core = XATCore()

    def test_load(self):
        badge = XATCore.Badge(1)


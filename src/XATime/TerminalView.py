#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4.QtGui import QDialog

from XATime.ui.Ui_TerminalView import Ui_TerminalView

__author__ = 'Marco Bartel'


class TerminalView(QDialog, Ui_TerminalView):
    def __init__(self, parent=None):
        super(TerminalView, self).__init__(parent)
        self.setupUi(self)

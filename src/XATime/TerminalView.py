#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import sys
import time

import pymysql
import yaml
from PyQt4.QtCore import QTimer, Qt, QSize, QCoreApplication
from PyQt4.QtGui import QDialog, QIcon, QKeyEvent, QColor, QPalette

from XATime.AsyncFuncQt import AsyncFuncQt
import XATime
from XATime.ui.Ui_TerminalView import Ui_TerminalView

__author__ = 'Marco Bartel'


class TerminalView(XATime.Core, QDialog, Ui_TerminalView):
    modeTexts = {
        XATime.Core.MODUS_KOMMEN: "Kommen",
        XATime.Core.MODUS_GEHEN: "Gehen",
        XATime.Core.MODUS_PAUSE: "Pause",
        XATime.Core.MODUS_STATUS: "Status"
    }

    modeIcons = {
        XATime.Core.MODUS_KOMMEN: ":/icons/kommen.svg",
        XATime.Core.MODUS_GEHEN: ":/icons/gehen.svg",
        XATime.Core.MODUS_PAUSE: ":/icons/pause.svg",
        XATime.Core.MODUS_STATUS: ":/icons/status.svg"
    }

    COLOR_ALERT = "#A00"
    COLOR_OK = "#080"

    def __init__(self, parent=None):
        XATime.Core.__init__(self)
        QDialog.__init__(self, parent)
        self.inputString = ""
        self.setupUi(self)
        self.setupWidgets()
        self.setupTimer()
        self.setMode(self.MODUS_KOMMEN)

    def setupWidgets(self):
        self.pbKommen.setIconSize(QSize(100, 100))
        self.pbKommen.setIcon(QIcon(self.modeIcons[self.MODUS_KOMMEN]))

        self.pbGehen.setIconSize(QSize(100, 100))
        self.pbGehen.setIcon(QIcon(self.modeIcons[self.MODUS_GEHEN]))

        self.pbPause.setIconSize(QSize(50, 50))
        self.pbPause.setIcon(QIcon(self.modeIcons[self.MODUS_PAUSE]))

        self.pbStatus.setIconSize(QSize(50, 50))
        self.pbStatus.setIcon(QIcon(self.modeIcons[self.MODUS_STATUS]))

        self.pbKommen.pressed.connect(self.slotButtonPressed)
        self.pbGehen.pressed.connect(self.slotButtonPressed)
        self.pbPause.pressed.connect(self.slotButtonPressed)
        self.pbStatus.pressed.connect(self.slotButtonPressed)

        self.labelDaten.hide()

        if sys.platform in ("posix", "linux2"):
            self.showFullScreen()
            self.setCursor(Qt.BlankCursor)
        else:
            self.resize(800, 480)

    def setupTimer(self):
        self.clockTimer = QTimer()
        self.clockTimer.setInterval(1000)
        self.clockTimer.timeout.connect(self.slotClockTimerTimeOut)
        self.clockTimer.start()

    def slotClockTimerTimeOut(self):
        self.labelClock.setText("{dt:%a.  %d.%m.%Y  %H:%M}".format(dt=self.now()))

    def slotButtonPressed(self):
        sender = self.sender()
        if sender == self.pbKommen:
            mode = self.MODUS_KOMMEN
        elif sender == self.pbGehen:
            mode = self.MODUS_GEHEN
        elif sender == self.pbStatus:
            mode = self.MODUS_STATUS
        elif sender == self.pbPause:
            mode = self.MODUS_PAUSE

        self.setMode(mode)

    def setMode(self, mode):
        self.mode = mode
        self.pbMode.setText(self.modeTexts[mode])
        self.pbMode.setIconSize(QSize(200, 200))
        self.pbMode.setIcon(QIcon(self.modeIcons[mode]))

    def keyPressEvent(self, event):
        if type(event) == QKeyEvent:
            if event.key() == Qt.Key_Return:
                badge = self.inputString
                self.inputString = ""
                self.slotNewBadgeString(badge)

            if event.key() < 127:
                self.inputString += chr(int(event.key()))
            event.accept()
        else:
            event.ignore()

    @AsyncFuncQt(await=True)
    def qtsleep(self, s):
        time.sleep(s)

    def message(self, message, sec, color=None):
        wdgs = [
            self.pbGehen,
            self.pbKommen,
            self.pbPause,
            self.pbStatus,
            self.pbMode
        ]
        if color:
            self.setStyleSheet("""
                TerminalView {{background: {color};}}
                # QToolButton {{background: {color}; border: {color};}}
            """.format(color=color))

        self.labelDaten.setText(message)
        for wdg in wdgs:
            wdg.hide()

        self.labelDaten.show()
        self.qtsleep(sec)
        self.labelDaten.hide()
        for wdg in wdgs:
            wdg.show()

        if color:
            self.setStyleSheet("")

    def setAllButtonsEnabled(self, state):
        wdgs = [
            self.pbGehen,
            self.pbKommen,
            self.pbPause,
            self.pbStatus
        ]
        for wdg in wdgs:
            wdg.setEnabled(state)

    def slotNewBadgeString(self, BADGE_NR):
        ok = False
        self.setAllButtonsEnabled(False)

        BADGE_NR = BADGE_NR.strip()
        badge = self.getBadgeByBadgeNumber(BADGE_NR)
        if badge:
            user = badge.getUser()
            if user:
                ok = True
                if self.mode in (XATime.Core.MODUS_KOMMEN, XATime.Core.MODUS_GEHEN, XATime.Core.MODUS_PAUSE):
                    now = self.now()
                    user.newTimeLog(mode=self.mode, logTime=now)
                    self.message(
                        "{NAME}\n\n{MODE_NAME} registriert.\n\nZeit: {dt:%H:%M}".format(
                            NAME=user.NAME,
                            MODE_NAME=self.modeTexts[self.mode],
                            dt=now,
                        ),
                        2,
                        color=self.COLOR_OK
                    )

                elif self.mode == XATime.Core.MODUS_STATUS:
                    self.message(
                        """{name}\n\n(1)  {acc1}     (2)  {acc2}""".format(
                            name=user.NAME,
                            acc1=self.minutesToHourString(user.getSaldoForAccount(1)),
                            acc2=self.minutesToHourString(user.getSaldoForAccount(2)),
                        ),
                        10,
                        color=self.COLOR_OK
                    )




        if not ok:
            self.message("Badge {BADGE_NR}\n\nnicht erkannt.".format(BADGE_NR=BADGE_NR), 2, color=self.COLOR_ALERT)

        self.setAllButtonsEnabled(True)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import time

import sys

import pymysql
import yaml
from PyQt4.QtCore import QTimer, Qt, QSize, QCoreApplication, QEventLoop
from PyQt4.QtGui import QDialog, QPicture, QIcon, QKeyEvent

from XATime.AsyncFuncQt import AsyncFuncQt
from XATime.ui.Ui_TerminalView import Ui_TerminalView

__author__ = 'Marco Bartel'


class TerminalView(QDialog, Ui_TerminalView):
    MODUS_KOMMEN, MODUS_GEHEN, MODUS_PAUSE, MODUS_STATUS = range(4)

    modeTexts = {
        MODUS_KOMMEN: "Kommen",
        MODUS_GEHEN: "Gehen",
        MODUS_PAUSE: "Pause",
        MODUS_STATUS: "Status"
    }

    modeIcons = {
        MODUS_KOMMEN: ":/icons/kommen.svg",
        MODUS_GEHEN: ":/icons/gehen.svg",
        MODUS_PAUSE: ":/icons/pause.svg",
        MODUS_STATUS: ":/icons/status.svg"
    }


    def __init__(self, parent=None):
        super(TerminalView, self).__init__(parent)
        self.modeSlots = {
            self.MODUS_KOMMEN: self.slotKommen,
            self.MODUS_GEHEN: self.slotGehen,
            self.MODUS_PAUSE: self.slotPause,
            self.MODUS_STATUS: self.slotStatus,
        }


        self.loadConfig()


        self.inputString = ""
        self.setupUi(self)
        self.setupWidgets()
        self.setupTimer()
        self.setMode(self.MODUS_KOMMEN)

    def dbQueryDict(self, sql):
        con = pymysql.connect(
            host=self.config["host"],
            user=self.config["user"],
            passwd=self.config["passwd"],
            db=self.config["db"],
        )
        cur = con.cursor(pymysql.cursors.DictCursor)
        cur.execute(sql)

        ret = cur.fetchall()
        con.close()

        return ret

    def loadConfig(self):
        self.config = yaml.load(open("xatime.yaml"))["database"]


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
        self.labelClock.setText("{dt:%a.  %d.%m.%Y  %H:%M}".format(dt=datetime.datetime.now()))

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

    def message(self, message, sec):
        self.labelDaten.setText(message)
        self.pbMode.hide()
        self.labelDaten.show()
        self.qtsleep(2)
        self.labelDaten.hide()
        self.pbMode.show()

    def setAllButtonsEnabled(self, state):
        self.pbKommen.setEnabled(state)
        self.pbGehen.setEnabled(state)
        self.pbPause.setEnabled(state)
        self.pbStatus.setEnabled(state)

    def slotNewBadgeString(self, badge):
        self.setAllButtonsEnabled(False)
        self.modeSlots[self.mode](badge.strip())
        self.setAllButtonsEnabled(True)

    def slotKommen(self, badge):
        sql = "select ID, NAME from xatime_badges where BADGE_NR='{badge}'".format(badge=badge)
        r = self.dbQueryDict(sql)
        if len(r) != 0:
            d = r[0]
            self.message("{name}\n\nKommen registriert.".format(name=d["NAME"]), 2)
        else:
            self.message("Badge {badge}\n\nnicht erkannt.".format(badge=badge), 2)

    def slotGehen(self, badge):
        pass

    def slotStatus(self, badge):
        pass

    def slotPause(self, badge):
        pass


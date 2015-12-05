#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from PyQt4.QtCore import QTimer, Qt, QSize
from PyQt4.QtGui import QDialog, QPicture, QIcon
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

        self.teDaten.hide()
        # self.showFullScreen()
        # self.setCursor(Qt.BlankCursor)
        self.resize(800, 480)



    def setupTimer(self):
        self.clockTimer = QTimer()
        self.clockTimer.setInterval(1000)
        self.clockTimer.timeout.connect(self.slotClockTimerTimeOut)
        self.clockTimer.start()

    def slotClockTimerTimeOut(self):
        self.labelClock.setText("{dt:%d.%m.%Y   %H:%M}".format(dt=datetime.datetime.now()))

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
        self.pbMode.setIconSize(QSize(200,200))
        self.pbMode.setIcon(QIcon(self.modeIcons[mode]))
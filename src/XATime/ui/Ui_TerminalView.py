# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TerminalView.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TerminalView(object):
    def setupUi(self, TerminalView):
        TerminalView.setObjectName(_fromUtf8("TerminalView"))
        TerminalView.resize(400, 231)
        self.gridLayout = QtGui.QGridLayout(TerminalView)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelClock = QtGui.QLabel(TerminalView)
        self.labelClock.setAlignment(QtCore.Qt.AlignCenter)
        self.labelClock.setObjectName(_fromUtf8("labelClock"))
        self.gridLayout.addWidget(self.labelClock, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pbKommen = QtGui.QToolButton(TerminalView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbKommen.sizePolicy().hasHeightForWidth())
        self.pbKommen.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/kommen.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbKommen.setIcon(icon)
        self.pbKommen.setIconSize(QtCore.QSize(50, 50))
        self.pbKommen.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.pbKommen.setAutoRaise(False)
        self.pbKommen.setObjectName(_fromUtf8("pbKommen"))
        self.verticalLayout.addWidget(self.pbKommen)
        self.pbStatus = QtGui.QToolButton(TerminalView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbStatus.sizePolicy().hasHeightForWidth())
        self.pbStatus.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/status.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbStatus.setIcon(icon1)
        self.pbStatus.setIconSize(QtCore.QSize(50, 50))
        self.pbStatus.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.pbStatus.setObjectName(_fromUtf8("pbStatus"))
        self.verticalLayout.addWidget(self.pbStatus)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.labelMiddleUpper = QtGui.QLabel(TerminalView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMiddleUpper.sizePolicy().hasHeightForWidth())
        self.labelMiddleUpper.setSizePolicy(sizePolicy)
        self.labelMiddleUpper.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMiddleUpper.setObjectName(_fromUtf8("labelMiddleUpper"))
        self.verticalLayout_3.addWidget(self.labelMiddleUpper)
        self.labelMiddleLower = QtGui.QLabel(TerminalView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMiddleLower.sizePolicy().hasHeightForWidth())
        self.labelMiddleLower.setSizePolicy(sizePolicy)
        self.labelMiddleLower.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMiddleLower.setObjectName(_fromUtf8("labelMiddleLower"))
        self.verticalLayout_3.addWidget(self.labelMiddleLower)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pbGehen = QtGui.QToolButton(TerminalView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbGehen.sizePolicy().hasHeightForWidth())
        self.pbGehen.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/gehen.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbGehen.setIcon(icon2)
        self.pbGehen.setIconSize(QtCore.QSize(50, 50))
        self.pbGehen.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.pbGehen.setObjectName(_fromUtf8("pbGehen"))
        self.verticalLayout_2.addWidget(self.pbGehen)
        self.pbPause = QtGui.QToolButton(TerminalView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbPause.sizePolicy().hasHeightForWidth())
        self.pbPause.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/pause.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbPause.setIcon(icon3)
        self.pbPause.setIconSize(QtCore.QSize(50, 50))
        self.pbPause.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.pbPause.setObjectName(_fromUtf8("pbPause"))
        self.verticalLayout_2.addWidget(self.pbPause)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.labelStatus = QtGui.QLabel(TerminalView)
        self.labelStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStatus.setObjectName(_fromUtf8("labelStatus"))
        self.gridLayout.addWidget(self.labelStatus, 2, 0, 1, 1)

        self.retranslateUi(TerminalView)
        QtCore.QMetaObject.connectSlotsByName(TerminalView)

    def retranslateUi(self, TerminalView):
        TerminalView.setWindowTitle(_translate("TerminalView", "XATime", None))
        self.labelClock.setText(_translate("TerminalView", "N/A", None))
        self.pbKommen.setText(_translate("TerminalView", "Kommen", None))
        self.pbStatus.setText(_translate("TerminalView", "Status", None))
        self.labelMiddleUpper.setText(_translate("TerminalView", "N/A", None))
        self.labelMiddleLower.setText(_translate("TerminalView", "N/A", None))
        self.pbGehen.setText(_translate("TerminalView", "Gehen", None))
        self.pbPause.setText(_translate("TerminalView", "Pause", None))
        self.labelStatus.setText(_translate("TerminalView", "N/A", None))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TerminalView = QtGui.QWidget()
    ui = Ui_TerminalView()
    ui.setupUi(TerminalView)
    TerminalView.show()
    sys.exit(app.exec_())


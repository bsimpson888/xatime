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
        TerminalView.resize(342, 370)
        self.gridLayout = QtGui.QGridLayout(TerminalView)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelClock = QtGui.QLabel(TerminalView)
        self.labelClock.setAlignment(QtCore.Qt.AlignCenter)
        self.labelClock.setObjectName(_fromUtf8("labelClock"))
        self.gridLayout.addWidget(self.labelClock, 0, 0, 1, 1)
        self.labelMode = QtGui.QLabel(TerminalView)
        self.labelMode.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMode.setObjectName(_fromUtf8("labelMode"))
        self.gridLayout.addWidget(self.labelMode, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pbKommen = QtGui.QPushButton(TerminalView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbKommen.sizePolicy().hasHeightForWidth())
        self.pbKommen.setSizePolicy(sizePolicy)
        self.pbKommen.setObjectName(_fromUtf8("pbKommen"))
        self.horizontalLayout.addWidget(self.pbKommen)
        self.pbGehen = QtGui.QPushButton(TerminalView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbGehen.sizePolicy().hasHeightForWidth())
        self.pbGehen.setSizePolicy(sizePolicy)
        self.pbGehen.setObjectName(_fromUtf8("pbGehen"))
        self.horizontalLayout.addWidget(self.pbGehen)
        self.pbPause = QtGui.QPushButton(TerminalView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbPause.sizePolicy().hasHeightForWidth())
        self.pbPause.setSizePolicy(sizePolicy)
        self.pbPause.setObjectName(_fromUtf8("pbPause"))
        self.horizontalLayout.addWidget(self.pbPause)
        self.pbStatus = QtGui.QPushButton(TerminalView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbStatus.sizePolicy().hasHeightForWidth())
        self.pbStatus.setSizePolicy(sizePolicy)
        self.pbStatus.setObjectName(_fromUtf8("pbStatus"))
        self.horizontalLayout.addWidget(self.pbStatus)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.labelName = QtGui.QLabel(TerminalView)
        self.labelName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelName.setObjectName(_fromUtf8("labelName"))
        self.gridLayout.addWidget(self.labelName, 3, 0, 1, 1)
        self.labelStatus = QtGui.QLabel(TerminalView)
        self.labelStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStatus.setObjectName(_fromUtf8("labelStatus"))
        self.gridLayout.addWidget(self.labelStatus, 4, 0, 1, 1)

        self.retranslateUi(TerminalView)
        QtCore.QMetaObject.connectSlotsByName(TerminalView)

    def retranslateUi(self, TerminalView):
        TerminalView.setWindowTitle(_translate("TerminalView", "XATime", None))
        self.labelClock.setText(_translate("TerminalView", "N/A", None))
        self.labelMode.setText(_translate("TerminalView", "N/A", None))
        self.pbKommen.setText(_translate("TerminalView", "Kommen", None))
        self.pbGehen.setText(_translate("TerminalView", "Gehen", None))
        self.pbPause.setText(_translate("TerminalView", "Pause", None))
        self.pbStatus.setText(_translate("TerminalView", "Status", None))
        self.labelName.setText(_translate("TerminalView", "N/A", None))
        self.labelStatus.setText(_translate("TerminalView", "N/A", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TerminalView = QtGui.QWidget()
    ui = Ui_TerminalView()
    ui.setupUi(TerminalView)
    TerminalView.show()
    sys.exit(app.exec_())


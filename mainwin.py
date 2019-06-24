# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 400)
        MainWindow.setMinimumSize(QtCore.QSize(370, 400))
        MainWindow.setMaximumSize(QtCore.QSize(370, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setEnabled(True)
        self.treeView.setGeometry(QtCore.QRect(10, 40, 351, 291))
        self.treeView.setInputMethodHints(QtCore.Qt.ImhNone)
        self.treeView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.treeView.setObjectName("treeView")
        self.filterEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.filterEdit.setGeometry(QtCore.QRect(10, 10, 351, 20))
        self.filterEdit.setText("")
        self.filterEdit.setMaxLength(256)
        self.filterEdit.setObjectName("filterEdit")
        self.exportBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exportBtn.setGeometry(QtCore.QRect(10, 340, 351, 23))
        self.exportBtn.setObjectName("exportBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 370, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.filterEdit.setPlaceholderText(_translate("MainWindow", "Filter..."))
        self.exportBtn.setText(_translate("MainWindow", "Export to CSV"))



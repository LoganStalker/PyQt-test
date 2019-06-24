# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
from mainwin import Ui_MainWindow
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.path = QtCore.QDir.rootPath()
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath(self.path)
        self.model.setFilter(QtCore.QDir.Dirs | QtCore.QDir.Files | QtCore.QDir.NoDot)
        self.model.setNameFilterDisables(False)

        self.ui.treeView.setSortingEnabled(False)
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.hideColumn(1)
        self.ui.treeView.hideColumn(2)
        self.ui.treeView.hideColumn(3)
        self.ui.treeView.setRootIndex( self.model.index(self.path) )

        self.ui.treeView.clicked.connect(self.updateModel)
        self.ui.exportBtn.clicked.connect(self.exportBtnClick)
        self.ui.filterEdit.textChanged.connect(self.onTextChanged)

    def updateModel(self, index):
        self.path = self.model.fileInfo(index).filePath()
        if index.data() != '..':
            self.ui.treeView.setRootIndex(index)
        else:
            currentRoot = self.ui.treeView.rootIndex()
            self.ui.treeView.setRootIndex(currentRoot.parent())

    def exportBtnClick(self):
        index = self.model.index(self.path)
        rowCount = self.model.rowCount(index)
        file_data = ''
        for i in range(rowCount):
            mi = self.model.index(i, 0, index)
            fileInfo = self.model.fileInfo(mi)
            file_data = ','.join(['%s%s,%s\n' % (file_data, fileInfo.fileName(), fileInfo.absoluteFilePath())])
        fname = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', filter='*.csv')
        if fname:
            file = open(fname[0], 'w')
            file.write(file_data)
            file.close()

    @QtCore.pyqtSlot(str)
    def onTextChanged(self, txt):
        self.model.nameFilters().clear()
        self.model.setNameFilters(['%s*' % txt])
        if txt == "":
            self.model.nameFilters().clear()
            self.model.setNameFilters(['*'])

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()

    sys.exit(app.exec())
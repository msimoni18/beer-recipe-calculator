# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recipe.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fermentableTable = QtWidgets.QTableWidget(self.centralwidget)
        self.fermentableTable.setGeometry(QtCore.QRect(10, 80, 521, 151))
        self.fermentableTable.setColumnCount(5)
        self.fermentableTable.setObjectName("fermentableTable")
        self.fermentableTable.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.fermentableTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fermentableTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fermentableTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.fermentableTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.fermentableTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.fermentableTable.setHorizontalHeaderItem(4, item)
        self.addrowButton = QtWidgets.QPushButton(self.centralwidget)
        self.addrowButton.setGeometry(QtCore.QRect(420, 50, 113, 32))
        self.addrowButton.setObjectName("addrowButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Beer Recipe Calculator"))
        item = self.fermentableTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.fermentableTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.fermentableTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "% of Grain Bill"))
        item = self.fermentableTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Fermentable"))
        item = self.fermentableTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "PPG"))
        item = self.fermentableTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Lovibond"))
        self.addrowButton.setText(_translate("MainWindow", "Add Row"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


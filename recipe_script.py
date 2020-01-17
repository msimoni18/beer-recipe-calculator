#! /usr/bin/python python3

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from recipe import Ui_MainWindow
import pandas as pd


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.addrowButton.clicked.connect(self.addrow)

        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setGeometry(QtCore.QRect(220, 100, 411, 392))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(5)
        self.tableWidget.show()

        attr = ['one', 'two', 'three', 'four', 'five']
        i = 0
        for j in attr:
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(j))
            self.comboBox = QtWidgets.QComboBox()
            self.tableWidget.setCellWidget(i, 1, self.comboBox)
            #self.tableWidget.setCurrentItem(i, 1, ["test1", "test2"])
            self.comboBox.addItems(['Test1', 'Test2'])
            i += 1



    def addrow(self):
        rowPos = self.ui.fermentableTable.rowCount()
        self.ui.fermentableTable.insertRow(rowPos)
        comboBox = QtWidgets.QComboBox()
        self.ui.fermentableTable.setCellWidget(1, 1, comboBox)

    def fermentable_list(self):
        df = pd.read_excel('Grain.xlsx')
        self.ferm_list = df['Fermentable']


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
#! /usr/bin/python python3

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from recipe_gui import Ui_MainWindow
import pandas as pd


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.fermentable_list()

        # Testing this block here - Define combo boxes then use in functions
        comboBox_fermentables = QtWidgets.QComboBox()
        comboBox_fermentables.addItems(self.FERMENTABLE_LIST)

        self.comboBox_hops = QtWidgets.QComboBox() 
        hop_test = ['', 'hop1', 'hop2', 'hop3']
        self.comboBox_hops.addItems(hop_test)
        ######################
        # Uncommenting from here down populates all rows with filled combo boxes
        # Initialize tables with combo box
        self.ui.fermentableTable.setCellWidget(0, 0, comboBox_fermentables)
        #self.comboBox_hops = QtWidgets.QComboBox()
        self.ui.hopsTable.setCellWidget(0, 0, self.comboBox_hops)

        # Connect buttons to functions
        self.ui.addfermentablesButton.clicked.connect(self.addfermentables)
        self.ui.addhopsButton.clicked.connect(self.addhops)

        # Test lists with fermentables and hops
        #ferm_test = ['', 'grain1', 'grain2', 'grain3']
        #hop_test = ['', 'hop1', 'hop2', 'hop3']
        #self.comboBox_fermentables.addItems(ferm_test)
        #self.comboBox_hops.addItems(hop_test)

    def addfermentables(self):
        """Add row and insert combo box in fermentable column"""

        rowPos = self.ui.fermentableTable.rowCount()
        # New instance of a combobox is created
        new_ferm_combobox = QtWidgets.QComboBox()
        new_ferm_combobox.addItems(self.FERMENTABLE_LIST)
        self.ui.fermentableTable.insertRow(rowPos)
        self.ui.fermentableTable.setCellWidget(rowPos, 0, new_ferm_combobox)
    

    def addhops(self):
        """Add row and insert combo box in hops column"""
        rowPos = self.ui.hopsTable.rowCount()
        #self.comboBox_hops = QtWidgets.QComboBox()
        self.ui.hopsTable.insertRow(rowPos)
        #hop_test = ['', 'hop1', 'hop2', 'hop3']
        #self.comboBox_hops.addItems(hop_test)
        self.ui.hopsTable.setCellWidget(rowPos, 0, self.comboBox_hops)


    def fermentable_list(self):
        df = pd.read_excel('Grain.xlsx')
        self.FERMENTABLE_LIST = df['Fermentable'].to_list()
        self.FERMENTABLE_LIST .insert(0, '')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

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

        # Testing this block here - Define combo boxes then use in functions
        # TODO - For some reason when defining first, the combo box moves
        #        and sticks with the last row. Need to figure out why.
        self.comboBox_fermentables = QtWidgets.QComboBox()        
        ferm_test = ['', 'grain1', 'grain2', 'grain3']
        self.comboBox_fermentables.addItems(ferm_test)

        self.comboBox_hops = QtWidgets.QComboBox() 
        hop_test = ['', 'hop1', 'hop2', 'hop3']
        self.comboBox_hops.addItems(hop_test)
        ######################
        # Uncommenting from here down populates all rows with filled combo boxes
        # Initialize tables with combo box
        #self.comboBox_fermentables = QtWidgets.QComboBox()
        self.ui.fermentableTable.setCellWidget(0, 0, self.comboBox_fermentables)
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
        #self.comboBox_fermentables = QtWidgets.QComboBox()
        self.ui.fermentableTable.insertRow(rowPos)
        #ferm_test = ['', 'grain1', 'grain2', 'grain3']
        #self.comboBox_fermentables.addItems(ferm_test)
        self.ui.fermentableTable.setCellWidget(rowPos, 0, self.comboBox_fermentables)
    

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
        self.ferm_list = df['Fermentable']


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

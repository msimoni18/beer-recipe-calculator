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

        # Initialize list of available fermentables
        self.fermentable_list()
 
        hop_test = ['', 'hop1', 'hop2', 'hop3']

        # Initialize first row in hops table with combo boxes
        hops_comboBox = QtWidgets.QComboBox() 
        hops_type_comboBox = QtWidgets.QComboBox()

        hops_comboBox.addItems(hop_test)
        hops_type_comboBox.addItems(['', 'Boil', 'Aroma', 'Dry'])

        self.ui.hopsTable.setCellWidget(0, 1, hops_comboBox)        
        self.ui.hopsTable.setCellWidget(0, 0, hops_type_comboBox)
        
        # Connect add row buttons to functions
        self.ui.addfermentablesButton.clicked.connect(self.add_fermentables)
        self.ui.addhopsButton.clicked.connect(self.add_hops)
        

    def add_fermentables(self):
        """Add row and insert combo boxes in fermentable columns."""
        # Count number of rows in table
        rowPos = self.ui.fermentableTable.rowCount()

        # Create combo boxes
        fermentables_type_comboBox = QtWidgets.QComboBox()
        fermentables_comboBox = QtWidgets.QComboBox()
        fermentables_amount_comboBox = QtWidgets.QComboBox()
       
        # Add items to combo boxes 
        fermentables_type_comboBox.addItems(['', 'Grain', 'Adjunct'])
        fermentables_comboBox.addItems(self.FERMENTABLE_LIST)
        fermentables_amount_comboBox.addItems(['', 'lb', 'oz'])

        # Check when current index changes and print text
        fermentables_comboBox.currentIndexChanged[str].connect(self.print_selected_text)
        
        # Insert new row and add combo boxes
        self.ui.fermentableTable.insertRow(rowPos)
        self.ui.fermentableTable.setCellWidget(rowPos, 0, fermentables_type_comboBox)
        self.ui.fermentableTable.setCellWidget(rowPos, 1, fermentables_comboBox)
        self.ui.fermentableTable.setCellWidget(rowPos, 3, fermentables_amount_comboBox)
    

    def add_hops(self):
        """Add row and insert combo boxes in hops columns."""
        
        rowPos = self.ui.hopsTable.rowCount()
       
        # Create new instance of combo boxes
        new_hop_test = ['', 'hop1', 'hop2', 'hop3']
        new_hops_comboBox = QtWidgets.QComboBox()
        new_hops_type_comboBox = QtWidgets.QComboBox()
        
        new_hops_comboBox.addItems(new_hop_test)
        new_hops_type_comboBox.addItems(['', 'Boil', 'Aroma', 'Dry'])
 
        # Insert new row and add combo boxes
        self.ui.hopsTable.insertRow(rowPos)
        self.ui.hopsTable.setCellWidget(rowPos, 0, new_hops_type_comboBox)
        self.ui.hopsTable.setCellWidget(rowPos, 1, new_hops_comboBox)


    def fermentable_list(self):
        """Read grain list into DataFrame and add to a list."""
        df = pd.read_excel('files/Grain.xlsx')
        self.FERMENTABLE_LIST = df['Fermentable'].to_list()
        self.FERMENTABLE_LIST.insert(0, '')


    def print_selected_text(self, text):
        """Print text from combo box."""
        print(text)


    def remove_fermentables(self):
        """Remove fermentable row."""
        # insert line to remove row


    def remove_hops(self):
        """Remove hops row."""
        # insert line to remove row


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

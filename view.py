"""
Copyright (C) 2018  Heriberto J. Díaz Luis-Ravelo

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QComboBox, QTableWidget
from PyQt5.QtCore import Qt


class View(QWidget):

    def __init__(self, *args, **kwargs):
        super(View, self).__init__(*args, **kwargs)

        self.mainLayout = QGridLayout(self)

        self.lblNameCost = QLabel('Name:')
        self.lblCost = QLabel('Cost:')
        self.lblTypeCost = QLabel('Cost type:')

        self.cmbTypeCost = QComboBox()
        self.cmbTypeCost.addItem('COST TYPE')

        self.edtNameCost = QLineEdit()
        self.edtCost = QLineEdit('€')
        self.edtCost.setAlignment(Qt.AlignRight)

        self.btnAdd = QPushButton('Add')

        self.tblCosts = QTableWidget()
        self.tblCosts.setHorizontalHeaderLabels(['Name', 'Cost'])
        self.tblCosts.verticalHeader().setVisible(True)
        self.tblCosts.setRowCount(15)
        self.tblCosts.setColumnCount(2)

    def createFormGroup(self):
        self.mainLayout.addWidget(self.lblNameCost, 0, 0)
        self.mainLayout.addWidget(self.edtNameCost, 0, 1)
        self.mainLayout.addWidget(self.lblCost, 0, 2)
        self.mainLayout.addWidget(self.edtCost, 0, 3)
        self.mainLayout.addWidget(self.cmbTypeCost, 0, 4)
        self.mainLayout.addWidget(self.btnAdd, 0, 5)

        self.mainLayout.addWidget(self.tblCosts, 1, 0, 1, 3)

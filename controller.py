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

from view import View
from model import Model
from PyQt5.QtWidgets import QApplication
import sys


class Controller:

    def __init__(self):
        self.view = View()
        self.model = Model('database.csv', None)

        if self.model.getLastID() > 0:
            """Poner costes en tabla."""
            allData = self.model.getAll()
            for data in allData:
                self.view.setTblCosts(data[0], data[1])

        self.view.createFormGroup()

        self.view.show()


if __name__ == '__main__':
    app = QApplication([])

    window = Controller()
    sys.exit(app.exec_())

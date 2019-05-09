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

from PyQt5.QtCore import QAbstractItemModel
from tempfile import NamedTemporaryFile
import shutil
import csv


class Model(QAbstractItemModel):
    def __init__(self, fileName, parent=None):
        super(Model, self).__init__(parent)

        self.header = ['ID', 'Name', 'Cost', 'Type']

        self.columnID = 0
        self.columnName = 1
        self.columnCost = 2
        self.columnType = 3

        self.fileName = fileName
        self.lastID = 0
        self.rowCount = 0

        self.mainPersonID = None
        self.husbandID = None
        self.wifeID = None
        self.fatherMainPersonID = None
        self.motherMainPersonID = None
        self.fatherWifeHusbandID = None
        self.motherWifeHusbandID = None

        try:
            with open(fileName) as csvFile:
                results = []
                # spamReader = csv.reader(csvFile, delimiter=',')
                spamReader = csv.DictReader(csvFile, delimiter=';')

                for row in spamReader:
                    self.rowCount += 1

                    results.append(row)

                # print(self.rowCount)

            if self.rowCount == 0:
                with open(self.fileName, 'a') as csvFile:
                    spamWriter = csv.writer(csvFile, delimiter=';')

                    spamWriter.writerow(self.header)

            else:
                # self.lastID = self.rowCount - 1
                self.lastID = self.rowCount

        except FileNotFoundError:
            with open(self.fileName, 'a') as csvFile:
                spamWriter = csv.writer(csvFile, delimiter=';')

                spamWriter.writerow(self.header)

    def addCost(self, data):
        row = []

        for item, value in data.items():
            if value == '':
                row.append('')

            else:
                row.append(value)

        with open(self.fileName, 'a') as csvFile:
            spamWriter = csv.writer(csvFile, delimiter=';')

            spamWriter.writerow(row)

    def updateCost(self, data):
        rowData = []

        for item, value in data.items():
            if value == '':
                rowData.append('')

            else:
                rowData.append(str(value))

        tempFile = NamedTemporaryFile(mode='w', delete=False)

        with open(self.fileName, 'r') as csvFile, tempFile:
            reader = csv.reader(csvFile, delimiter=';')
            writer = csv.writer(tempFile, delimiter=';')

            for row in reader:

                if row[self.columnID] == rowData[self.columnID]:

                    for i in range(1, len(rowData)):
                        row[i] = rowData[i]

                writer.writerow(row)

        shutil.move(tempFile.name, self.fileName)

    def getAll(self):
        allCost = []

        with open(self.fileName) as csvFile:
            # spamReader = csv.reader(csvFile, delimiter=';')
            spamReader = csv.DictReader(csvFile, delimiter=';')

            # count = 0
            #
            # for row in spamReader:
            #     if count > 0:
            #         allPeople.append(row)
            #
            #     count = 1

            for row in spamReader:
                allCost.append(row)

            return allCost

    def getID(self, costDict):
        return costDict[self.header[self.columnID]]

    def getLastID(self):
        return self.lastID

    def addID(self):
        self.lastID += 1

        return self.lastID

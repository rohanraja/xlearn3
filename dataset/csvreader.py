import csv

class CSVReader:

    def __init__(self, csvPath):
        self.csvLines = []
        self.csvHeader = []
        self.loadCSV(csvPath)


    def loadCSV(self, csvPath):
        f = open(csvPath)
        r = csv.reader(f)
        self.csvHeader = r.next()
        for row in r:
            self.csvLines.append(row)
        f.close()
        self.Count = len(self.csvLines)

    def getColumnWithName(self, colName):

        assert colName in self.csvHeader
        colIdx = self.csvHeader.index(colName)
        outP = []

        for line in self.csvLines:
            outP.append(line[colIdx])
        return outP


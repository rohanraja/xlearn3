import json
import csv
import imagePathReader
import categoricalParse

class CSVReader:

    csvLines = []
    csvHeader = []

    def __init__(self, csvPath):
        self.loadCSV(csvPath)


    def loadCSV(self, csvPath):
        f = open(csvPath)
        r = csv.reader(f)
        self.csvHeader = r.next()
        for row in r:
            self.csvLines.append(row)
        f.close()
        self.Count = len(csvLines)

    def getColumnWithName(self, colName):

        assert colName in self.csvHeader
        colIdx = self.csvHeader.index(colName)
        outP = []

        for line in self.csvLines:
            outP.append(line[colIdx])
        return outP


parsersDict = {
        "Image": imagePathReader.ImagePathParser,
        "Categorical": categoricalParse.CategoricalParser
}


class DataSetInfo:


    columnsDict = {}

    def __init__(self, jsonPath):
        self.readJson(jsonPath)

        csvPath = self.jsonData["DataListFile"]
        self.csvReader = CSVReader(csvPath)
        self.Count = self.csvReader.Count

        self.findColumns()

        self.X = self.jsonData["X"]
        self.Y = self.jsonData["Y"]


    def findColumns(self):

        for colInfo in self.jsonData["Data"]:

            colName = colInfo["Name"]
            rowList = self.csvReader.getColumnWithName(colName)
            col = parsersDict[colInfo["Type"]](rowList, colInfo)
            self.columnsDict[colName] = col


    def readJson(self, fPath):
        self.jsonData = json.load(open(fPath))


    def getBatchGen(self, batchSize):
        return None

if __name__ == "__main__":
    dsinfo = DataSetInfo("metaData.json")


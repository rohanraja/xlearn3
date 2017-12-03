import json
import csv
import imagePathReader
import categoricalParse
from csvreader import CSVReader 
import os

parsersDict = {
        "Image": imagePathReader.ImagePathParser,
        "Categorical": categoricalParse.CategoricalParser
}


class DataSetInfo:


    columnsDict = {}

    def __init__(self, datasetPath):
        jsonPath = os.path.join(datasetPath, "metaData.json")
        self.readJson(jsonPath)

        csvPath = self.jsonData["DataListFile"]
        csvPath = os.path.join(datasetPath, csvPath)
        self.csvReader = CSVReader(csvPath)
        self.csvReader.randomize()
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


    def getXY(self, st, end):
        x = []
        y = []
        for label in self.X:
            x.append(self.columnsDict[label].GetSlice(st, end))
        
        for label in self.Y:
            y.append(self.columnsDict[label].GetSlice(st, end))

        return (x,y)


    def getBatchGen(self, batchSize):
        totBatches = self.Count / batchSize
        lastExtra = self.Count % batchSize

        end = 0

        for i in range(totBatches):

            st = i*batchSize
            end = (i+1)*batchSize

            yield self.getXY(st, end)

        if lastExtra > 0:
            yield self.getXY(end,end+lastExtra)


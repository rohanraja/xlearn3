import json
import imp
import sys
import os


def readClassFromPyFile(pyDir, pyFileName, className):
    sys.path.insert(0, os.path.abspath(pyDir))
    mod = __import__(pyFileName)
    cls = getattr(mod, className)
    return cls

class ModelInfo:
    def __init__(self, modelPath):
        modelJsonPath = os.path.join(modelPath, "modelInfo.json")
        self.modelPath = modelPath
        self.jsonData = json.load(open(modelJsonPath))
        self.parseJson()
        self.initializeClassOjbect()

    def parseJson(self):
        self.modelPyFile = self.jsonData["pyFileName"]
        self.modelClassName = self.jsonData["pyClassName"]

    def initializeClassOjbect(self):
        Cls = readClassFromPyFile(self.modelPath, self.modelPyFile, self.modelClassName)
        params = Cls.defaultParams()
        self.model = Cls(params)


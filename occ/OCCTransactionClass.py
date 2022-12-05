# Import necessary modules
from OCCOperationClass import Operation
import copy

# Create a transaction class
class Transaction:
    def __init__(self, name:int):
        self.name = name
        self.Operations = []
        self.readOperations = []
        self.writeOperations = []
        self.startTimestamp = None
        self.validateTimestamp = None
        self.endTimestamp = None
    
    def setOperations(self, operations:Operation):
        self.Operations = operations
    
    def addOperation(self, new_operation:Operation):
        self.Operations.append(new_operation)
    
    def addWriteOperation(self, operation:Operation):
        self.writeOperations.append(operation)
    
    def addReadOperation(self, operation:Operation):
        self.readOperations.append(operation)
    
    def getWriteOperations(self):
        return self.writeOperations
    
    def getReadOperations(self):
        return self.readOperations
    
    def getStartTimestamp(self):
        return self.startTimestamp
    
    def getValidateTimestamp(self):
        return self.validateTimestamp
    
    def getEndTimestamp(self):
        return self.endTimestamp
    
    def setStartTimestamp(self, timestamp:float):
        self.startTimestamp = timestamp
    
    def setValidateTimestamp(self, timestamp:float):
        self.validateTimestamp = timestamp
    
    def setEndTimestamp(self, timestamp:float):
        self.endTimestamp = timestamp
    
    def printAllOperations(self):
        for operation in self.allOperations:
            operation.printOperation()
            print(" ", end="")
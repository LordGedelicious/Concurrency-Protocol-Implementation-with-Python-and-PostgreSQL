# Import necessary modules
from OperationClass import Operation
import copy

# Create a transaction class
class Transaction:
    def __init__(self, name:int):
        self.name = name
        self.allOperations = []
        self.completedOperations = []
    
    def setOperations(self, operations:Operation):
        self.allOperations = operations
    
    def addOperation(self, new_operation:Operation):
        self.allOperations.append(new_operation)
    
    def printAllOperations(self):
        for operation in self.allOperations:
            operation.printOperation()
            print(" ", end="")
    
    def checkAllOperationsComplete(self):
        if len(self.allOperations) == len(self.completedOperations):
            return True
        return False
    
    def resetTransaction(self):
        self.completedOperations = []

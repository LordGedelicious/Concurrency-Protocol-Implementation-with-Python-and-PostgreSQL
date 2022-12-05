# Import necessary modules
from OCCTransactionClass import Transaction
from OCCOperationClass import Operation

# Create a schedule class
class Schedule:
    def __init__(self):
        self.operationSchedule = []
    
    def addOperation(self, new_operation:Operation):
        self.operationSchedule.append(new_operation)
    
    def removeOperation(self, operation:Operation):
        self.operationSchedule.remove(operation)
    
    def getAllOperations(self):
        return self.operationSchedule
    
    def findOperationFromTransactionName(self, transaction_name:int):
        operationList = []
        for operation in self.operationSchedule:
            if operation.getTransactionName() == transaction_name and operation.getType() != "C":
                operationList.append(operation)
        if len(operationList) != 0:
            return operationList
        return []

    def findOperationByObject(self, item_name:str):
        operationList = []
        for operation in self.operationSchedule:
            if operation.object.getName() == item_name:
                operationList.append(operation)
        if len(operationList) != 0:
            return operationList
        return []
    
    def printOperationSchedule(self):
        for operation in self.operationSchedule:
            operation.printOperation()
            print(" ", end="")
        print()
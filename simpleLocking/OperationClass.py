# Import necessary modules
from ItemClass import Item

# Create a operation class
class Operation:
    def __init__(self, type:str, transaction_name:int, item=None):
        self.type = type # Can be either "W" for "WRITE" or "R" for "READ" or "A" for "ABORT" or "C" for "COMMIT" or "XL" for "Granting X-LOCK"
        self.item = item # Tables that are used in the operation, if type is "A" or "C", then item is None
        self.transactionName = transaction_name # Transaction name that the operation belongs to
    
    def setType(self, type:str):
        self.type = type
    
    def setItem(self, item:str):
        self.item = item
    
    def getTransactionName(self):
        return self.transactionName
    
    def getType(self):
        return self.type
    
    def getItem(self):
        return self.item
    
    def getItemName(self):
        return self.transactionName
    
    def printOperation(self):
        if self.type != "C":
            print("{}{}({})".format(self.type, self.transactionName, self.item.getName()), end="")
        else:
            print("{}{}".format(self.type, self.transactionName), end="")
# Import necessary modules
from ItemClass import Item

# Create a operation class
class Operation:
    def __init__(self, type:str, object:Item):
        self.type = type # Can be either "W" for "WRITE" or "R" for "READ" or "A" for "ABORT" or "C" for "COMMIT"
        self.object = object # Tables that are used in the operation, if type is "A" or "C", then object is None
    
    def setType(self, type:str):
        self.type = type
    
    def setObject(self, object:str):
        self.object = object
    
    def checkConflict(self, other_operation):
        if self.type == "WRITE" or other_operation.type == "WRITE":
            if self.object == other_operation.object:
                return True
        return False

    def printOperation(self):
        print("{}({})".format(self.type, self.object.getName()), end="")
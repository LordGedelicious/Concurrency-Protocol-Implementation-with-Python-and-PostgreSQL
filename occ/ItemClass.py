# Import necessary modules


# Create a Item (Data/Table) class
class Item:
    def __init__(self, name:str):
        self.name = name
        self.isLocked = False
        self.lockedBy = None
    
    def getName(self):
        return self.name
    
    def getIsLocked(self) -> bool:
        return self.isLocked
    
    def getLockedBy(self):
        return self.lockedBy
    
    def setLockedBy(self, lockedBy):
        self.lockedBy = lockedBy
    
    def setIsLocked(self, isLocked:bool):
        self.isLocked = isLocked

def getItemFromList(list, item_name:str):
    for item in list:
        if item.name == item_name:
            return item
    return False
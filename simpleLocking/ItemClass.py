# Import necessary modules


# Create a Item (Data/Table) class
class Item:
    def __init__(self, name:str):
        self.name = name
        self.isLocked = False
    
    def getName(self):
        return self.name

def getItemFromList(list, item_name:str):
    for item in list:
        if item.name == item_name:
            return item
    return False
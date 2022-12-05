# Import necessary modules
from TransactionClass import Transaction
from OperationClass import Operation

# Create a schedule class
class Schedule:
    def __init__(self):
        self.operationSchedule = []
        self.transactions = []
    
    def addOperation(self, new_operation:Operation):
        self.operationSchedule.append(new_operation)
    
    def addTransaction(self, new_transaction:Transaction):
        self.transactions.append(new_transaction)
    
    def printTransactions(self):
        idx = 0
        for transaction in self.transactions:
            print("Transaction {}: ".format(idx + 1), end="")
            transaction.printAllOperations()
            print()
    
    def getTransaction(self, transaction_name:int):
        for transaction in self.transactions:
            if transaction.name == transaction_name:
                return transaction
        return False
    
    def printOperationSchedule(self):
        for operation in self.operationSchedule:
            operation.printOperation()
            print(" ", end="")
        print()
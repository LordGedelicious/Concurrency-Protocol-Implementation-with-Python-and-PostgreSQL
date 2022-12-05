# Import Schedule
from ScheduleClass import Schedule
from ItemClass import Item, getItemFromList
from TransactionClass import Transaction
from OperationClass import Operation

import sys

# Ask user for all the available Items
tempItemList = input("Enter all the available Items (separated by comma, ex: 'A,B,C'): ").split(sep=",")

# From the list of items, create a list of Item objects
itemList = []
for item in tempItemList:
    itemList.append(Item(item))

# Ask user for all the available Transactions and then create Schedule object.
# Add all the transactions to the schedule (initially, all the transactions are empty)
countTransactions = int(input("Enter the number of Transactions: "))
schedule = Schedule()

# Ask user for all the operations in the schedule (regardless of the transaction they belong to)
tempOperationsList = input("Enter all the operations (separated by comma, ex: 'W1(A),R2(A),W2(B),R2(B),C1,C2'): ").split(sep=",")
for operation in tempOperationsList:
    if operation[0] != "C":
        operationName = operation[0]
        transactionName = int(operation[1])
        objectName = operation[3:-1]
        newOperation = Operation(operationName, transactionName, getItemFromList(itemList, objectName))
        schedule.addOperation(newOperation)
    else:
        operationName = operation[0]
        transactionName = int(operation[1])
        objectName = operation[2:-1]
        newOperation = Operation("C", transactionName)
        schedule.addOperation(newOperation)

# Print the schedule for debugging purposes
schedule.printOperationSchedule()

# Create a list of transactions and build locks
completedOperationsName = []
while True:
    for operation in schedule.getAllOperations():
        print("Operation: {}".format(operation.getFullName()), end="")
        if  operation.getType() != "C":
            # Uncompleted operation
            # Check if operation's item is locked or not.
            # If locked by the same transaction, then add to completed operations
            # If locked by a different transaction, then skip and wait for commit
            # If not locked yet, gain lock and add to completed operations
            operationItem = operation.getItem()
            if operationItem.getIsLocked() == False:
                operationItem.setIsLocked(True)
                operationItem.setLockedBy(operation.getTransactionName())
                schedule.removeOperation(operation)
                completedOperationsName.append("XL{}({})".format(operation.getTransactionName(),operationItem.getName()))
                completedOperationsName.append("{}{}({})".format(operation.getType(),operation.getTransactionName(),operationItem.getName()))
            elif operationItem.getIsLocked() == True:
                if operationItem.getLockedBy() == operation.getTransactionName():
                    schedule.removeOperation(operation)
                    completedOperationsName.append("{}{}({})".format(operation.getType(),operation.getTransactionName(),operationItem.getName()))
            # If there's no other transactions that are waiting for the lock, then release the lock
            print("Contents of findOperationByTransactionName: {}".format(schedule.findOperationFromTransactionName(operation.getTransactionName())))
            if len(schedule.findOperationFromTransactionName(operation.getTransactionName())) == 0:
                completedOperationsName.append("C{}".format(operation.getTransactionName()))
                for item in itemList:
                    if item.getLockedBy() == operation.getTransactionName():
                        item.setIsLocked(False)
                        item.setLockedBy(None)
        print("Current contents of completed operations: {}".format(completedOperationsName))
    if len(schedule.getAllOperations()) == 0:
        break

print(completedOperationsName)
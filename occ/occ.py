from OCCScheduleClass import Schedule
from OCCTransactionClass import Transaction
from OCCOperationClass import Operation
from ValidateSchedule import validateScheduleFunc

import time

def occFunc():
    countTransactions = int(input("Enter the number of transactions: "))
    transactionList = []
    for i in range(countTransactions):
        tempTransactions = Transaction(i+1)
        transactionList.append(tempTransactions)

    tempOperationsList = input("Enter all the operations (separated by comma, ex: 'W1(A),R2(A),W2(B),R2(B),C1,C2'): ").split(sep=",")
    operationList = []
    # Listing operations
    operationIdx = 0
    for operation in tempOperationsList:
        if operation[0] != "C":
            operationName = operation[0]
            transactionName = int(operation[1])
            objectName = operation[3:-1]
            newOperation = Operation(operationIdx, operationName, transactionName, objectName)
            transactionList[transactionName - 1].addOperation(newOperation)
            operationList.append(newOperation)
        else:
            operationName = operation[0]
            transactionName = int(operation[1])
            objectName = operation[2:-1]
            newOperation = Operation(operationIdx, "C", transactionName)
            transactionList[transactionName - 1].addOperation(newOperation)
            operationList.append(newOperation)
        operationIdx += 1

    # Reading and executing operations
    for idx in range(len(operationList)):
        if (operationList[idx].getType() in ["R", "W"]):
            idx_j = operationList[idx].getTransactionName() - 1
            
            # If the transaction is not active, then use current time for the timestamp
            if (transactionList[idx_j].getStartTimestamp() == None):
                transactionList[idx_j].setStartTimestamp(time.time())
            
            if operationList[idx].getType() == "R":
                transactionList[idx_j].addReadOperation(operationList[idx])
            else:
                transactionList[idx_j].addWriteOperation(operationList[idx])
        
        else: # Is a commit operation
            transactionList[idx_j].setValidateTimestamp(time.time())
            isValid = validateScheduleFunc(idx_j, transactionList)
            if (isValid == True):
                transactionList[idx_j].setEndTimestamp(time.time())
            else:
                print("Transaction {} is invalid".format(idx_j + 1))
                return False

    print("All transactions are valid!")
    return True
        
occFunc()
        
        
        
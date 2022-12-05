def validateScheduleFunc(idx_j, transactionList):
    transaction_j = transactionList[idx_j]
    for idx_i in range(len(transactionList)):
        transaction_i = transactionList[idx_i]
        if idx_i == idx_j:
            continue
        
        if transaction_i.getValidateTimestamp() == None:
            continue
        
        if transaction_i.getValidateTimestamp() < transaction_j.getValidateTimestamp():
            if transaction_i.getFinishTimestamp() < transaction_j.getStartTimestamp():
                pass
            elif transaction_j.getStartTimestamp() < transaction_i.getFinishTimestamp() < transaction_j.getValidateTimestamp():
                for var in transaction_i.getWriteOperations():
                    if var in transaction_j.getReadOperations():
                        return False
            else:
                return False
    return True
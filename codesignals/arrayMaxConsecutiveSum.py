def arrayMaxConsecutiveSum(inputArray, k):
    low = 0
    top = k
    gtotal = sum(inputArray[low:top])
    total = gtotal
    while top != len(inputArray):
        
        total = (total - inputArray[low])  + inputArray[top]
        low = low + 1
        top = top + 1
        if total > gtotal:
            gtotal = total
        
    return gtotal

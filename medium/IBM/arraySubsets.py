def subsetA(arr):
    # Write your code here
    arrSorted = sorted(arr)
    start_i = 0
    end_i = len(arrSorted) - 1
    subsetA = []
    sumA = 0
    sumB = 0
    while start_i <= end_i:
        if sumA <= sumB:
            sumA += arrSorted[end_i]
            subsetA.insert(0, arrSorted[end_i])
            end_i -= 1
        else:
            sumB += arrSorted[start_i]
            start_i += 1
    while sumB >= sumA:
        start_i -= 1
        subsetA.insert(0, arrSorted[start_i])
        sumB -=  arrSorted[start_i]
    return subsetA

subsetA([2,
3,
4,
4,
5,
9,
7,
8,
6,
10,
4,
5,
10,
10,
8,4,6,4,10,1])
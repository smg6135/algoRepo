def getMinimumKValues(arr):
    # Write your code here
    # convert to binary number
    def countOnes(str):
        ct = 0
        for char in str:
            if char == "1":
                ct += 1
        return ct

    res = []
    for num in arr:
        binNum = format(num, "0b")
        if num < 4:
            res.append(1)
        else:
            if binNum[-2:] == "00":
                minimumCt = float("inf")
                opOne = format(num-1, "0b")
                opTwo = format(num-2, "0b")
                opThree = format(num-3, "0b")

                if opOne[-2:] == "00":
                    minimumCt = min(minimumCt, countOnes(opOne))

                if opTwo[-2:] == "00":
                    minimumCt = min(minimumCt, countOnes(opTwo))

                if opThree[-2:] == "00":
                    minimumCt = min(minimumCt, countOnes(opThree))
                
                if minimumCt != float("inf"):
                    res.append(minimumCt + 1)
                else:
                    res.append(-1)
            elif binNum[-2:] == "11":
                res.append(countOnes(binNum) - 1)
            else:
                res.append(countOnes(binNum))

    return res

print(getMinimumKValues([12,
3 ,
7 ,
8 ,
15, 
19]))

x = 1
i = 1
while i <= 128:
    i += i
    if i > 128:
        break
    x += x
print(x)
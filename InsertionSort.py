

#lArray = [11,4,22,10,9,8]
lArray = [10,2,1,199,200,2001,20,30]
print("Before sorting array {}". format(lArray))

for i in range(1, len(lArray)):
    lKeyPos = i # 1
    lValInsert = lArray[lKeyPos] # 4
    while lKeyPos > 0 and lArray[lKeyPos-1] > lValInsert: # 11>4
        lArray[lKeyPos] = lArray[lKeyPos-1]  # 11
        lKeyPos -= 1

    lArray[lKeyPos] = lValInsert

print ("After sorting array {}".format(lArray))



class InsertionSort:
    def __init__(self, lArray):
        self.array = lArray

    def fInsertSort(self, lArray):
        for i in range(1, len(lArray)):
            lKeyPos = i  # 1
            lValInsert = lArray[lKeyPos]  # 4
            while lKeyPos > 0 and lArray[lKeyPos - 1] > lValInsert:  # 11>4
                lArray[lKeyPos] = lArray[lKeyPos - 1]  # 11
                lKeyPos -= 1
            lArray[lKeyPos] = lValInsert
        return(lArray)

sort1 = InsertionSort([10,2,1,199,200,2001,20,30])
print("Printing arrays in class form {}".format(sort1.fInsertSort(sort1.array)))


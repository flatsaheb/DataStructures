
# Swap the array elements and return the array.
def fSwapObjects(l_Array,ldx,lmin):
    l_Array[ldx] = l_Array[ldx] + l_Array[lmin]
    l_Array[lmin] = l_Array[ldx] - l_Array[lmin]
    l_Array[ldx] = l_Array[ldx] - l_Array[lmin]

    return l_Array

lArray = [7,10,11,4,3,190,1]

for i in range(0,len(lArray)-1):
    min = i #7
    for j in range(i+1,len(lArray)):#starting from 10
        if lArray[j] < lArray[min]:
            min = j # 3rd Index, next iteration 4th Index, 6th Index i.e. with value 1.
    if min != i: # min is 6 and i is 0, condition true. Swap l_Array[i] and l_Array[min] correspond to 7 and 1.
        fSwapObjects(lArray,i, min)

print ("Printing after sorting {}".format(lArray))


class SelectionSort:
    def __init__(self, l_Array):
        self.lInputArr = l_Array

        for i in range(0, len(self.lInputArr) - 1):
            min = i
            for j in range(i + 1, len(self.lInputArr)):  # starting from 1
                if self.lInputArr[j] < self.lInputArr[min]:
                    min = j
            if min != i:
                self.fcSwapObjects(self.lInputArr,i,min)

    def fcSwapObjects(self,l_InputArr,ldx,lmin):
        l_InputArr[ldx] = l_InputArr[ldx] + l_InputArr[lmin]
        l_InputArr[lmin] = l_InputArr[ldx] - l_InputArr[lmin]
        l_InputArr[ldx] = l_InputArr[ldx] - l_InputArr[lmin]
        return l_InputArr

sort1 = SelectionSort([7,10,11,4,3,190,1])
print(sort1.lInputArr)
sort2 = SelectionSort([7,8,1,20,30,100])
print(sort2.lInputArr)









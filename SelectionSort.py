
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








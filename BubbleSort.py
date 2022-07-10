class BubbleSort:
    def __init__(self, lArray):
        self.array = lArray
        for outer_i in range(len(self.array) - 1):
            for inner_i in range(len(self.array) - 1):
                if self.array[inner_i] > self.array[inner_i + 1]:
                    self.fSwapCode(self.array, inner_i)

    def fSwapCode(self, lArray, lIndex):
        lArray[lIndex] = lArray[lIndex] + lArray[lIndex + 1]
        lArray[lIndex + 1] = lArray[lIndex] - lArray[lIndex + 1]
        lArray[lIndex] = lArray[lIndex] - lArray[lIndex + 1]
        return lArray

def main():
    sort1 = BubbleSort([10,20,30,1,3])
    print (sort1.array)
    sort2 = BubbleSort([101,201,301,11,31])
    print(sort2.array)

if __name__ == "__main__":
    main()


'''
Without Class 
def fSwapCode(lArray,lIndex):
    lArray[lIndex] = lArray[lIndex]+lArray[lIndex+1]
    lArray[lIndex+1] = lArray[lIndex] - lArray[lIndex+1]
    lArray[lIndex] = lArray[lIndex] - lArray[lIndex+1]
    return lArray

lArray = [10,1,5,6,19]
print ("Printing array before sorting {}".format(lArray))

for outer_i in range(len(lArray)-1):
    for inner_i in range(len(lArray)-1):
        #print ("Inner element {}".format(lArray[inner_i]))
        if  lArray[inner_i] > lArray[inner_i+1]:
            fSwapCode(lArray,inner_i)

print ("Printing array after sorting {}".format(lArray))
'''
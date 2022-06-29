lArray = [11,4,22,10,9,8]

print("Before sorting array {}". format(lArray))

for i in range(1, len(lArray)):
    lKeyPos = i # 1
    lValInsert = lArray[lKeyPos] # 4
    while lKeyPos > 0 and lArray[lKeyPos-1] > lValInsert: # 11>4
        lArray[lKeyPos] = lArray[lKeyPos-1]  # 11
        lKeyPos -= 1

    lArray[lKeyPos] = lValInsert

print ("After sorting array {}".format(lArray))

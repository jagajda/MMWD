import random
def mutation (specimenList, mutType):
    #numberOfElements = len (specimensList [0])
    for i in specimenList:
        intList = i.intList
        numberOfElements = len (intList)
        mutationPoint = random.randint (0, numberOfElements - 1)
        if mutType == 0:
            intList[mutationPoint] = intList[mutationPoint] + random.randint (-1, 1)
        elif mutType == 1:
            intList[mutationPoint] = intList[mutationPoint] + random.randint (-3, 3)
        elif mutType == 2:
            intList[mutationPoint] = intList[mutationPoint] + random.randint (-5, 5)
    return specimenList


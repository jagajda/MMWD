import random
def mutation (specimenList, mutType, Storage):
    numberOfElements = len (Storage.storageElements)
    for i in specimenList:
        intList = i.intList
        #numberOfElements = len (intList)
        mutationPoint = random.randint (0, len(intList) - 1)
        if mutType == 0:
            intList[mutationPoint] = random.randint (0, round((numberOfElements - 1)/2))
        elif mutType == 1:
            intList[mutationPoint] = random.randint (round((numberOfElements - 1)/2), numberOfElements - 1)
        #elif mutType == 2:
          #  intList[mutationPoint] = intList[mutationPoint] + random.randint (-5, 5)
    return specimenList


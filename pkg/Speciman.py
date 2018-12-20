from pkg import Element as Element
from pkg import mutation
from pkg import crossover, Storage, Order
import random
""" definition of Speciman class and methods"""


class Speciman:
    def __init__(self, specimanID, intList):
        self.specimanID = specimanID
        self.intList = intList


#def targetFunction(Speciman, storageList):
#    target = 0
#    tempStorage = checkRemainder(Speciman, storageList)
#    for i in storageList.intList:
#        if i.remainder <= 1:
#            target += 0
#        else:
#            target += i.getvalue(i.remainder)
#    return target


#def newSpeciman(storagelist, orderlist):
#   """Generates random elementsList"""
#    templist = []
#    tempspeciman = orderlist[:]
#    tempstorage = storagelist[:]
#    for i in tempspeciman:
#        for j in tempstorage:
#            if i.elementLength <= j.remainder:
#                templist.append(j)
#            else:
#                break
#            tempelement = random.choice(templist)
#            i.source = tempelement.elementID
#            tempelement.remainder = tempelement.remainder - i.elementLength
#            templist.clear()
#            del tempelement
#    return tempspeciman


def newSpeciman(storage, order):
    """Create new random intList for Speciman, basing on storage and order elements lists"""
    tempStorage = storage.storageElements[:]
    tempOrder = order.orderElements[:]
    tempIntList = []
    tempChoiceList = []
    for i in order.orderElements:
        for j in tempStorage:
            if i.elementLength <= j.elementLength:
                tempChoiceList.append(i)
            else:
                tempIntList.insert(i, -1)
        toAppend = random.choice(tempChoiceList)
        tempIntList.insert(toAppend.elementID, i)
        tempStorage = storage.storageElements[:]
        tempChoiceList.clear()
    #check allocation
    if any(tempIntList) is -1:
        print('Speciman cannot be created (bad allocation)')
        return False
    else:
        pass
    #check remainder
    tempStorage = storage.storageElements[:]
    for i in tempOrder:
        for j in tempIntList:
            if i == j.elementID:
                j.remainder -= i.elementLength
            else:
                pass
    if any(tempStorage.remainder) < 0:
        print('Speciman cannot be created (remainder)')
        return False
    else:
        pass
    return tempIntList


def targetFunction(speciman, order, storage):
    """Calculates targetFunction for Speciman, basing on Speciman's intList, oderElements, storageElements """
    tempStorage = storage.storageElements[:]
    tempOrder = order.orderElements[:]
    tempIntList = Speciman.intList[:]
    target = 0
    for i in tempStorage:
        for j in tempIntList:
            if j == i.elementID:
                i.remainder -= tempOrder[tempIntList.index(j)].elementLength
            else:
                pass
        for k in tempStorage:
            if k.remainder <= 1:
                target += 0
            else:
                target += getValue(k.remainder)


def getValue(length):
    """Calculates element's value basing on it's length"""
    if length < 0:
        return None
    elif 0 <= length < 5:
        return length * 1.5
    elif 5 < length < 10:
        return length * 1.75
    elif 10 < length < 15:
        return length * 2
    elif 15 < length < 20:
        return length * 2.25
    elif length > 20:
        return length * 2.5


# def checkallocation(speciman):
#     """Check if any element of Speciman has no source"""
#     if any(speciman.elementsList.source == -1):
#         return False
#     else:
#         return True


#def checkRemainder (self, Order):
#    """Evaluate remainder for every element in the solution"""
#    for i in range (len (self.elementsList)):
#        self.specimenList[i].remainder -= Order.orderElements[i].length

#def checkRemainder (Speciman, storageList, orderList):
#    for i in range (len (Speciman.intList)):
#        for j in range (len (storageList)):
#            if Speciman.intList[i] == storageList[j].elementID:
#                storageList[j].remainder -= orderList[i].elementLength
#    return storageList

#def checkLimitations (storageList):
#    for i in range (len (storageList)):
#        if storageList[i].remainder < 0:
#            return False
#        else:
#            pass
#    return True

def nextGeneration (Population, Storage, Order, populationSize, elitePercentage, mutationPercentage, crossoverPercentage):
    specimenTargetsDict = {}
    while Population.numberOfSpecimen <= populationSize:
        Population.specimenList.append(newSpeciman (Storage.storageElements, Order.orderElements))
        for i in range (len (Population.specimenList)):
            storageListCopy = Storage.storageElements
            storageListCopy = checkRemainder (Population.specimenList[i], storageListCopy, Order.orderElements)
            if checkLimitations (storageListCopy) is False:
                Population.specimenList[i] = newSpeciman (Storage.storageElements, Order.orderElements)
            else:
                Population.numberOfSpecimen += 1
                specimenTargetsDict[Population.specimenList[i]] = targetFunction (Population.specimenList[i], storageListCopy)
    sortedDict = sorted (specimenTargetsDict.items(), key = lambda k: k[1])
    Population.specimenList.clear()
    for i in range (len (sortedDict)):
        Population.specimenList.append (sortedDict[i][0])
    Population.bestFitVect = Population.specimenList[:3]
    elite = round (elitePercentage * populationSize / 100)
    mutation = round (mutationPercentage * populationSize / 100)
    crossover = round (crossoverPercentage * populationSize / 100)
    die = populationSize - elite - mutation - crossover
    del (Population.specimenList[:(die - 1)])
    Population.specimenList[:(mutation - 1)] = mutation.mutation(Population.specimenList[:(mutation - 1)])
    Population.specimenList[mutation:(crossover - 1)] = crossover.crossover(Population.specimenList[mutation :(crossover - 1)])
    Population.numberOfSpecimen -= die
    Population.deathNum = die
    Population.mutationNum = mutation
    Population.crossoverNum = crossover
    return Population

from pkg import Element as Element
from pkg import Mutation
from pkg import Crossover, Storage, Order
import random, copy
""" definition of Speciman class and methods"""


class Speciman:
    def __init__(self, specimanID, intList):
        self.specimanID = specimanID
        self.intList = intList[:]

    def printTarget(self, storageList, orderList):
        tmp = ''
        for j in storageList:
            for k in self.intList:
                if k == j.elementID:
                    for l in orderList:
                        if k == l.elementID:
                            tmp += str(l.elementLength) + 'm/' + str(j.elementLength) + 'm '
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
        tmp += '# target: '
        tmp += (str(getTarget(self, storageList, orderList)) + ' # intList: ' + str(self.intList))
        return tmp


def targetFunction(Speciman, storageList):
   target = 0
   # tempStorage = checkRemainder(Speciman, storageList)
   for i in storageList:
       if i.remainder <= 1:
           target += 0
       else:
           add = getValue(i.remainder)
           target += add
   return target


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
                tempChoiceList.append(j.elementID)
            else:
                tempIntList.insert(i, -1)
        toAppend = random.choice(tempChoiceList)
        tempIntList.insert(i.elementID, toAppend)
        #tempStorage = storage.storageElements[:]
        tempChoiceList.clear()
    #check allocation
    if any(tempIntList) is -1:
        print('Speciman cannot be created (bad allocation)')
        return False
    else:
        pass
    #check remainder
    # tempStorage = storage.storageElements[:]
    # for i in tempOrder:
    #     for j in tempIntList:
    #         if i == j.elementID:
    #             j.remainder -= i.elementLength
    #         else:
    #             pass
    # if any(tempStorage.remainder) < 0:
    #     print('Speciman cannot be created (remainder)')
    #     return False
    # else:
    #     pass
    return tempIntList


def getTarget(speciman, order, storage):
    """Calculates targetFunction for Speciman, basing on Speciman's intList, oderElements, storageElements """
    tempStorage = copy.deepcopy(storage)
    tempOrder = copy.deepcopy(order)
    tempIntList = copy.deepcopy(speciman.intList)
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
    return target


def getValue(length):
    """Calculates element's value basing on it's length"""
    value = 0
    if length <= 0:
        value = 0
    elif 0 < length <= 5:
        value = length * 1.5
    elif 5 < length <= 10:
        value = length * 1.75
    elif 10 < length <= 15:
        value = length * 2
    elif 15 < length <= 20:
        value = length * 2.25
    elif length > 20:
        value = length * 2.5
    return value


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


def checkRemainder (intList, storageList, orderList):
   for i in range (len (intList)):
       for j in range (len (storageList)):
           if intList[i] == storageList[j].elementID:
               storageList[j].remainder -= orderList[i].elementLength
   return storageList


def checkLimitations (storageList):
   for i in range (len (storageList)):
       if storageList[i].remainder < 0:
           return False
       else:
           pass
   return True


def nextGeneration (Population, Storage, Order, populationSize, elitePercentage, mutationPercentage, crossoverPercentage):
    specimenTargetsDict = {}
    #cnt = 0
    newIntList = []
    for m in Population.specimenList:
        storageListCopy = copy.deepcopy(Storage.storageElements)
        storageListCopy = checkRemainder(m.intList, storageListCopy, Order.orderElements)
        if checkLimitations(storageListCopy) is False:
            pass
        else:
            newIntList.append (m)
            specimenTargetsDict[m] = targetFunction(m, storageListCopy)
    Population.specimenList = copy.deepcopy (newIntList)
    Population.numberOfSpecimen = len (Population.specimenList)
    while Population.numberOfSpecimen < populationSize:
        new = newSpeciman(Storage, Order)
        if new == False:
            return False
        else:
            Population.numberOfSpecimen += 1
        newTempSpecimen = Speciman(Population.numberOfSpecimen, new)
        storageListCopy = copy.deepcopy(Storage.storageElements)
        storageListCopy = checkRemainder (newTempSpecimen.intList, storageListCopy, Order.orderElements)
        if checkLimitations (storageListCopy) is False:
            Population.numberOfSpecimen -= 1
        else:
            Population.specimenList.append (newTempSpecimen)
            specimenTargetsDict[newTempSpecimen] = targetFunction(m, storageListCopy)
    sortedDict = sorted (specimenTargetsDict.items(), key = lambda k: k[1])
    Population.specimenList.clear()
    for i in range (len (sortedDict)):
        Population.specimenList.append (sortedDict[i][0])
    tmpList = [getTarget(a, Storage.storageElements, Order.orderElements) for a in Population.specimenList]
    sortedList = sorted(tmpList, key=float, reverse=True)
    Population.bestFitVect = copy.deepcopy(sortedList[:3])
    elite = round (elitePercentage * populationSize / 100)
    mutation = round (mutationPercentage * populationSize / 100)
    crossover = round (crossoverPercentage * populationSize / 100)
    die = populationSize - elite - mutation - crossover
    mutType = random.randint (0,2)
    crossType = random.randint (0,2)
    if die != 0:
        del (Population.specimenList[:(die - 1)])
    Population.specimenList[:mutation] = Mutation.mutation(Population.specimenList[:mutation], mutType, Storage)
    Population.specimenList[mutation:(crossover - 1)] = Crossover.crossover(Population.specimenList[mutation :(crossover - 1)], crossType)
    Population.numberOfSpecimen -= die
    Population.deathNum = die
    Population.mutationNum = mutation
    Population.crossoverNum = crossover
    return Population


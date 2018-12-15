from pkg import Element as Element
import numpy as np
import random
""" definition of Speciman class and methods"""


class Speciman:
    def __init__(self, specimanID, intList):
        self.specimanID = specimanID
        self.intList = intList


def targetFunction(Speciman, storageList):
    target = 0
    tempStorage = storageList[:]
#    for i in Speciman.intList:
#       for j in storageList:
#            if i == storageList[j].elementID:
#                if storageList[j].remainder <= 1:
#                    target += 0
#                else:
#                    target += storageList[j].getvalue(storageList[j].remainder)
    for i in storageList.elementsList:
        if i.remainder <= 1:
            target += 0
        else:
            target += i.getvalue(i.remainder)
    return target


def newSpeciman(storagelist, orderlist):
    """Generates random elementsList"""
    templist = []
    tempspeciman = orderlist[:]
    tempstorage = storagelist[:]
    for i in tempspeciman:
        for j in tempstorage:
            if i.elementLength <= j.remainder:
                templist.append(j)
            else:
                pass
            tempelement = random.choice(templist)
            i.source = tempelement.elementID
            tempelement.remainder = tempelement.remainder - i.elementLength
            templist.clear()
            tempelement.delete()
    return tempspeciman


def checkallocation(speciman):
    """Check if any element of Speciman has no source"""
    if any(speciman.elementsList.source == -1):
        return True
    else:
        return False


def checkRemainder (self, Order):
    """Evaluate remainder for every element in the solution"""
    for i in range (len (self.elementsList)):
        self.specimenList[i].remainder -= Order.orderElements[i].length

def checkRemainder (Speciman, storageList, orderList):
    for i in range (len (Speciman.elementsList)):
        for j in range (len (storageList)):
            if Speciman.elementsList[i] == storageList[j].elementID:
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
    while Population.numberOfSpecimen <= populationSize:
        Population.specimenList.append (newSpeciman (Storage.storageElements, Order.orderElements))
        for i in range (len (Population.specimenList)):
            storageListCopy = Storage.storageElements
            storageListCopy = checkRemainder (Population.specimenList[i], storageListCopy, Order.orderElements)
            if checkLimitations (storageListCopy) is False:
                Population.specimenList[i] = newSpeciman (Storage.storageElements, Order.orderElements)
            else:
                Population.numberOfSpeciman += 1
                specimenTargetsDict[Population.specimenList[i]] = targetFunction (Population.specimenList[i], storageListCopy)
    sortedDict = sorted (specimenTargetsDict.items(), key = lambda k: k[1])
    Population.specimenList.clear()
    for i in range (len (sortedDict)):
        Population.specimenList.append (sortedDict[i][0])
    Population.bestFitVect = np.asarray(Population.specimenList[:3])
    elite = round (elitePercentage * populationSize / 100)
    mutation = round (mutationPercentage * populationSize / 100)
    crossover = round (crossoverPercentage * populationSize / 100)
    die = populationSize - elite - mutation - crossover
    del (Population.specimenList[:(die - 1)])
    Population.specimenList[:(mutation - 1)] = mutation(Population.specimenList[:(mutation - 1)])
    Population.specimenList[mutation:(crossover - 1)] = crossover(Population.specimenList[mutation :(crossover - 1)])
    Population.numberOfSpecimen -= die
    Population.deathNum = die
    Population.mutationNum = mutation
    Population.crossoverNum = crossover
    return Population

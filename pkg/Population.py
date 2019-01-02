from pkg import Speciman, Element
import matplotlib.pyplot as pyplot
import numpy as np
""" definition of Population class and methods"""


class Population:
    def __init__(self, populationID, specimenList, numberOfSpecimen, crossoverNum = 0, mutationNum = 0, deathNum = 0,
                 bestFitVect = []):
        self.populationID = populationID
        self.specimenList = specimenList[:]
        self.numberOfSpecimen = numberOfSpecimen
        self.crossoverNum = crossoverNum
        self.mutationNum = mutationNum
        self.deathNum = deathNum
        self.bestFitVect = bestFitVect[:]

    def printPopulation(self, storageList, orderList):
        tmp = 'Population ID:%2s\n' % (str(self.populationID))
        tmp += 'Number of Specimen: %s\n' %(str(self.numberOfSpecimen))
        for i in self.specimenList:
            tmp += 'ID:'
            tmp += str(i.specimanID)
            tmp += ' # solution:'
            tmp += i.printTarget(storageList, orderList)
            tmp += '# '
            tmp += 'target: '
        # tmp += 'Best acceptable solutions found: '
        # tmp += str(self.bestFitVect[:3])
        # tmp += '\n'
        return tmp

    def getTarget(self):
        obj = [self.bestFitVect[0], self.bestFitVect[1], self.bestFitVect[2]]
        return obj

    def getAverage(self, storageList, orderList):
        vec = [Speciman.getTarget(i, storageList, orderList) for i in self.specimenList]
        avg = np.average(vec)
        return avg

    def getStdDev(self, storageList, orderList):
        vec = [Speciman.getTarget(i, storageList, orderList) for i in self.specimenList]
        stddev = np.std(vec)
        return stddev

    def checkallocation(self):
        for j in self.specimenList:
            tmpList = [Speciman.checkallocation(j) for j in self.specimenList]
            if any(k for k in tmpList) is True:
                return False
            else:
                pass
        return True


def generatepopulation(numspecimen, storagelist, orderlist):
    tmpspecimenlist = []
    for i in range(0,numspecimen):
        j = Speciman.Speciman(i, Speciman.newSpeciman(storagelist, orderlist))
        tmpspecimenlist.append(j)
    return tmpspecimenlist

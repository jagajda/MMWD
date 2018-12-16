from pkg import Speciman, Element
import matplotlib.pyplot as pyplot
import numpy as np
""" definition of Population class and methods"""


class Population:
    def __init__(self, populationID, specimenList, numberOfSpecimen, crossoverNum = 0, mutationNum = 0, deathNum = 0,
                 bestFitVect = []):
        self.populationID = populationID
        self.specimenList = specimenList
        self.numberOfSpecimen = numberOfSpecimen
        self.crossoverNum = crossoverNum
        self.mutationNum = mutationNum
        self.deathNum = deathNum
        self.bestFitVect = bestFitVect

    def plotTarget(self):
        obj = pyplot.plot(self.populationID, self.bestFitVect[0], self.populationID, self.bestFitVect[1], self.populationID, self.bestFitVect[2])
        return obj

    def plotAverage(self):
        vec = [Element.getvalue(i) for i in self.specimenList]
        avg = np.average(vec)
        obj = pyplot.plot(self.populationID, avg)
        return obj

    def plotStdDev(self):
        vec = [Element.getvalue(i) for i in self.specimenList]
        stddev = np.std(vec)
        obj = pyplot.plot(self.populationID, stddev)
        return obj

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

#testing pyplot
pyplot.figure(1)
x = [1, 2]
y =  [1, 2]
s = pyplot.plot(x, y)
pyplot.show(s)
pyplot.figure(2)
x1 = [4, 4]
y1 = [6, 4]
s1 = pyplot.plot(x1, y1)
pyplot.show(s1)
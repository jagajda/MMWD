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
        pyplot.plot(self.populationID, self.bestFitVect[0], self.populationID, self.bestFitVect[1], self.populationID, self.bestFitVect[2])

    def plotAverage(self):
        vec = [Element.getvalue(i) for i in self.specimenList]
        avg = np.average(vec)
        pyplot.plot(self.populationID, avg)

    def plotStdDev(self):
        vec = [Element.getvalue(i) for i in self.specimenList]
        stddev = np.std(vec)
        pyplot.plot(self.populationID, stddev,)


def generatepopulation(numspecimen, storagelist, orderlist):
    tmpspecimenlist = []
    for i in range(0,numspecimen):
        j = Speciman.Speciman(i, Speciman.newSpeciman(storagelist, orderlist))
        tmpspecimenlist.append(j)
    return tmpspecimenlist


#testing pyplot
x = [1, 2, 3]
y1 = [i * 2 for i in x]
y2 = [j*j for j in x]
s = pyplot.plot(x, y1, x, y2)
pyplot.show(s)
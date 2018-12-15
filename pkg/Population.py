from pkg import Speciman
""" definition of Population class and methods"""


class Population:
    def __init__(self, populationID, specimenList, numberOfSpecimen, crossoverNum = 0, mutationNum = 0, deathNum = 0,
                 bestFitVect = ()):
        self.populationID = populationID
        self.specimenList = specimenList
        self.numberOfSpecimen = numberOfSpecimen
        self.crossoverNum = crossoverNum
        self.mutationNum = mutationNum
        self.deathNum = deathNum
        self.bestFitVect = bestFitVect


def generatepopulation(numspecimen, storagelist, orderlist):
    tmpspecimenlist = []
    for i in range(0,numspecimen):
        j = Speciman.Speciman(i, Speciman.newSpeciman(storagelist, orderlist))
        tmpspecimenlist.append(j)
    return tmpspecimenlist

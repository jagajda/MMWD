from pkg import Speciman
""" definition of Population class and methods"""


class Population:
    def __init__(self, populationID, specimenList, numberOfSpecimen, generationNumber):
        self.populationID = populationID
        self.specimenList = specimenList
        self.numberOfSpecimen = numberOfSpecimen
        self.generationNumber = generationNumber


def generatepopulation(numspecimen, storagelist, orderlist):
    tmpspecimenlist = []
    for i in range (0,numspecimen):
        j = Speciman(i, Speciman.newspeciman(storagelist, orderlist))
        tmpspecimenlist.append(j)

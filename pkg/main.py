from pkg import Element, fileInOut, Mutation, Order, Population, Speciman, Storage
import os, random
import matplotlib.pyplot as pyplot

def main():
    myStorage = Storage.Storage(fileInOut.readfile('storageSample.txt'))
    myOrder = Order.Order(fileInOut.readfile('orderSample.txt'))
    populationCount = 10
    specimanCount = 20
    populationList = []
    populationList.insert(0, Population.Population(0, Population.generatepopulation(specimanCount, myStorage, myOrder), specimanCount))
    print(populationList[0].specimenList[3].intList)
    # avgPlot = populationList[0].plotAverage(myStorage.storageElements)
    # stdPlot = populationList[0].plotStdDev(myStorage.storageElements)
    # targetPlot = populationList[0].plotTarget()
    for i in range(1, populationCount):
        populationList.insert(i, Speciman.nextGeneration(populationList[i-1], myStorage, myOrder, specimanCount, 30, 30, 40))
        # avgPlot = populationList[i].plotAverage(myStorage.storageElements)
        # stdPlot = populationList[i].plotStdDev(myStorage.storageElements)
        # targetPlot = populationList[i].Population.Population.plotTarget()
        print(populationList[i].specimenList[i].intList)
    # pyplot.figure(1)
    # pyplot.show(avgPlot)
    # pyplot.figure(2)
    # pyplot.show(stdPlot)
    # pyplot.figure(3)
    # pyplot.show(targetPlot)

if __name__ == '__main__':
    main()

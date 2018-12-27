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
    # avgObj = pyplot.plot(avgPlot, 'b')
    # stdPlot = populationList[0].plotStdDev(myStorage.storageElements)
    # stdObj = pyplot.plot(stdPlot, 'g')
    # targetPlot = populationList[0].plotTarget()
    # tarObj = pyplot.plot(targetPlot, 'r')
    for i in range(1, populationCount):
        populationList.insert(i, Speciman.nextGeneration(populationList[i-1], myStorage, myOrder, specimanCount, 30, 30, 40))
        avgPlot = populationList[i].plotAverage(myStorage.storageElements)
        avgObj = pyplot.plot(avgPlot, 'b')
        stdPlot = populationList[i].plotStdDev(myStorage.storageElements)
        stdObj = pyplot.plot(stdPlot, 'g')
        targetPlot = populationList[i].plotTarget()
        tarObj = pyplot.plot(targetPlot, 'r')
        print(populationList[i].specimenList[i].intList)
    pyplot.figure(1)
    pyplot.show(avgObj)
    pyplot.figure(2)
    pyplot.show(stdObj)
    pyplot.figure(3)
    pyplot.show(tarObj)

if __name__ == '__main__':
    main()

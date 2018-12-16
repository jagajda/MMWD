from pkg import Element, fileInOut, mutation, Order, Population, Speciman, Storage
import os, random
import matplotlib.pyplot as pyplot

def main():
    myStorage = fileInOut.readfile('orderStorage.txt')
    myOrder = fileInOut.readfile('orderSample.txt')
    populationCount = 10
    specimanCount = 20
    populationList = []
    populationList.insert(0, Population.Population(0, Population.generatepopulation(specimanCount, myStorage, myOrder), specimanCount))
    avgPlot = populationList[0].Population.plotAverage()
    stdPlot = populationList[0].Population.plotStdDev()
    targetPlot = populationList[0].Population.plotTarget()
    for i in range(1, populationCount):
        Speciman.nextGeneration(populationList[i-1], myStorage, myOrder, specimanCount, 30, 30, 40)
        avgPlot = populationList[i].Population.plotAverage()
        stdPlot = populationList[i].Population.plotStdDev()
        targetPlot = populationList[i].Population.plotTarget()
    pyplot.figure(1)
    pyplot.show(avgPlot)
    pyplot.figure(2)
    pyplot.show(stdPlot)
    pyplot.figure(3)
    pyplot.show(targetPlot)

if __name__ == '__main__':
    main()

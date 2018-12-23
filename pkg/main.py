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
    #avgPlot = populationList[0].plotAverage()
    #stdPlot = populationList[0].plotStdDev()
    #targetPlot = populationList[0].plotTarget()
    for i in range(1, populationCount):
        populationList.insert(i, Speciman.nextGeneration(populationList[i-1], myStorage, myOrder, specimanCount, 30, 30, 40))
        #avgPlot = populationList[i].Population.Population.plotAverage()
        #stdPlot = populationList[i].Population.Population.plotStdDev()
        #targetPlot = populationList[i].Population.Population.plotTarget()
        print(populationList[i].specimenList[i].intList)

if __name__ == '__main__':
    main()

from pkg import Element, fileInOut, Mutation, Order, Population, Speciman, Storage
import os, random, copy
import matplotlib.pyplot as pyplot
import numpy as np

def main():
    myStorage = Storage.Storage(fileInOut.readfile('storageSample.txt'))
    myOrder = Order.Order(fileInOut.readfile('orderSample.txt'))
    populationCount = 10
    specimanCount = 20
    populationList = []
    avgList = []
    stdList = []
    populationList.insert(0, Population.Population(0, Population.generatepopulation(specimanCount, myStorage, myOrder), specimanCount))
    avgList.append(populationList[0].getAverage(myStorage.storageElements, myOrder.orderElements))
    stdList.append(populationList[0].getStdDev(myStorage.storageElements, myOrder.orderElements))
    for i in range(1, populationCount):
        newPopulation = copy.deepcopy(populationList[i-1])
        newPopulation.populationID = i
        populationList.insert(i, Speciman.nextGeneration(newPopulation, myStorage, myOrder, specimanCount, 30, 30, 40))
        avgList.append(populationList[i].getAverage(myStorage.storageElements, myOrder.orderElements))
        stdList.append(populationList[i].getStdDev(myStorage.storageElements, myOrder.orderElements))
        # targetPlot = populationList[i].plotTarget()
        # tarObj = pyplot.plot(targetPlot, 'r')
        print(populationList[i].specimenList[i].intList)
    for j in populationList:
        print(j.printPopulation(myStorage.storageElements, myOrder.orderElements))
    pyplot.figure(1)
    x1 = [i.populationID for i in populationList]
    y1 = avgList
    pyplot.plot(x1, y1, label='Przebieg sredniej wartosci funkcji celu')
    pyplot.xlabel('ID populacji')
    pyplot.ylabel('Srednia wartosc funckji celu')
    pyplot.xticks(np.arange(0, len(x1), 1))
    pyplot.show()
    pyplot.figure(2)
    # pyplot.cla()
    x2 = [i.populationID for i in populationList]
    y2 = stdList
    obj2 = pyplot.plot(x2, y2, label='Przebieg wartosci odchylenia standardowego')
    pyplot.xlabel('ID populacji')
    pyplot.ylabel('Odchylenie standardowe')
    pyplot.xticks(np.arange(0, len(x2), 1))
    pyplot.show()
    # pyplot.figure(3)
    # pyplot.show(tarObj)

if __name__ == '__main__':
    main()

from pkg import Element, fileInOut, Mutation, Order, Population, Speciman, Storage
import os, random, copy
import matplotlib.pyplot as pyplot
import numpy as np

def main():
    myStorage = Storage.Storage(fileInOut.readfile('storageSample.txt'))
    myOrder = Order.Order(fileInOut.readfile('orderSample.txt'))
    populationCount = 30
    specimanCount = 20
    populationList = []
    medList = []
    stdList = []
    tarList0 = []
    tarList1 = []
    tarList2 = []
    dictList = []
    tmpString = ''
    populationList.insert(0, Population.Population(0, Population.generatepopulation(specimanCount, myStorage, myOrder), specimanCount))
    # avgList.append(populationList[0].getAverage(myStorage.storageElements, myOrder.orderElements))
    # stdList.append(populationList[0].getStdDev(myStorage.storageElements, myOrder.orderElements))
    for i in range(1, populationCount):
        newPopulation = copy.deepcopy(populationList[i-1])
        newPopulation.populationID = i
        populationList.insert(i, Speciman.nextGeneration(newPopulation, myStorage, myOrder, specimanCount, 30, 30, 40)[0])
        a = Speciman.nextGeneration(newPopulation, myStorage, myOrder, specimanCount, 30, 30, 40)[1]
        dictList.append(a)
        tmpList = [i[1] for i in a]
        medList.append(np.median(tmpList))
        stdList.append(np.std(tmpList))
        tarList0.append(populationList[i].getTarget()[0])
        tarList1.append(populationList[i].getTarget()[1])
        tarList2.append(populationList[i].getTarget()[2])
    for j in populationList:
        print(j.printPopulation(myStorage.storageElements, myOrder.orderElements))
    pyplot.figure(1)
    x1 = range(1, len(populationList))
    y1 = medList
    pyplot.plot(x1, y1, label='Przebieg mediany wartosci funkcji celu')
    pyplot.xlabel('ID populacji')
    pyplot.ylabel('Mediana wartosc funckji celu')
    pyplot.xticks(np.arange(0, len(x1), 1))
    pyplot.show()
    pyplot.figure(2)
    x2 = range(1, len(populationList))
    y2 = stdList
    pyplot.plot(x2, y2, label='Przebieg wartosci odchylenia standardowego')
    pyplot.xlabel('ID populacji')
    pyplot.ylabel('Odchylenie standardowe')
    pyplot.xticks(np.arange(0, len(x2), 1))
    pyplot.show()
    pyplot.figure(3)
    x3 = range(1, len(populationList))
    pyplot.plot(x3, tarList0, 'r', x3, tarList1, 'g', x3, tarList2, 'b', label='Przebieg wartosci funkcji przystosowania najlepszych dopuszczalnych osobnikow')
    pyplot.xlabel('ID populacji')
    pyplot.ylabel('Wartos funkcji celu')
    pyplot.xticks(np.arange(1, len(x3), 1))
    pyplot.show()
    # pyplot.figure(3)
    # pyplot.show(tarObj)

if __name__ == '__main__':
    main()

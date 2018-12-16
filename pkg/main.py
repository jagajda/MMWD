from pkg import Element, fileInOut, mutation, Order, Population, Speciman, Storage
import os, random
import matplotlib.pyplot as pyplot

def main():
    myStorage = fileInOut.readfile('orderStorage.txt')
    myOrder = fileInOut.readfile('orderSample.txt')
    populationCount = 10
    specimanCount = 20
    populationList = []
    for i in range(1,populationCount):
        populationList.insert(i,Population.Population(i, Speciman.newSpeciman(myStorage, myOrder)))
        for j in populationList[i].specimenList[j]:
            if any(Speciman.checkallocation(j)) is True:


if __name__ == '__main__':
    main()

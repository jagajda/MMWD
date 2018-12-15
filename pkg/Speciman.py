from pkg import Element as Element
import random
""" definition of Speciman class and methods"""


class Speciman:
    def __init__(self, specimanID, intList):
        self.specimanID = specimanID
        self.intList = intList


def targetfunction(Speciman, storageList):
    target = 0
    tempStorage = storageList[:]
#    for i in Speciman.intList:
#       for j in storageList:
#            if i == storageList[j].elementID:
#                if storageList[j].remainder <= 1:
#                    target += 0
#                else:
#                    target += storageList[j].getvalue(storageList[j].remainder)
    for i in storageList.elementsList:
        if i.remainder <= 1:
            target += 0
        else:
            target += i.getvalue(i.remainder)
    return target


def newspeciman(storagelist, orderlist):
    """Generates random elementsList"""
    templist = []
    tempspeciman = orderlist[:]
    tempstorage = storagelist[:]
    for i in tempspeciman:
        for j in tempstorage:
            if i.elementLength <= j.remainder:
                templist.append(j)
            else:
                pass
            tempelement = random.choice(templist)
            i.source = tempelement.elementID
            tempelement.remainder = tempelement.remainder - i.elementLength
            templist.clear()
            tempelement.delete()
    return tempspeciman


def checkallocation(speciman):
    """Check if any element of Speciman has no source"""
    if any(speciman.elementsList.source == -1):
        return True
    else:
        return False


def checkRemainder (self, Order):
    """Evaluate remainder for every element in the solution"""
    for i in range (len (self.elementsList)):
        self.specimenList[i].remainder -= Order.orderElements[i].length


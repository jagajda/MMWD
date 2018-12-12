from pkg import Element as Element
import random
""" definition of Speciman class and methods"""


class Speciman:
    def __init__(self, specimanID, elementsList):
        self.specimanID = specimanID
        self.elementsList = elementsList


def targetfunction(Speciman):
    target = 0
    for i in Speciman.elementsList:
        if i.remainder <= 1:
            target += 0
        else:
            target += Element.getvalue(i.remainder)
    return target


def newspeciman(storagelist, orderlist):
    templist = []
    tempspeciman = orderlist[:]
    tempstorage = storagelist[:]
    for i in tempspeciman:
        for j in tempstorage:
            if i.elementLength <= j.remainder:
                templist.append(j)
            else:
                pass
            tempelement = random.choice(j)
            i.source = tempelement.elementID
            tempelement.remainder = tempelement.remainder - i.elementLength
            templist.clear()
            tempelement.delete()
    return tempspeciman

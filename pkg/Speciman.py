from pkg import Element as Element
""" definition of Speciman class and methods"""
class Speciman:
    def __init__(self, elementsList, specimanID):
        self.elementsLts = elementsList
        self.specimanID = specimanID

def targetfunction(Speciman):
    target = 0
    for i in Speciman.elementsList:
        if i.remainder <= 1:
            target += 0
        else:
             target += Element.getvalue(i.remainder)
    return target
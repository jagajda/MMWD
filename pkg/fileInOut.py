from pkg import Element as Element
"""Functions to write to file and read data from file"""


def readfile(filename):
    """returns list of Elements, read from textfile"""
    with open(filename, 'r') as f:
        read = []
        for line in f:
            id, length = (line.split(";"))
            read.append(Element.Element(int(id), float(length)))
        return read


def writetofile(filename, toWrite):
    with open(filename, 'w') as f:
        for i in toWrite:
            f.write('{};{}\n'.format(str(i.elementID), str(i.elementLength)))


test=readfile('sample.txt')
print(test[4].elementID)
writetofile('testWrite.txt',test)

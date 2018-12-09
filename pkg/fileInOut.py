from pkg import Element as Element
"""Functions to write to file and read data from file"""

def readfile(filename):
    """returns list of Elements, read from textfile"""
    with open(filename, 'r') as f:
        read = []
        for line in f:
            id, length = (line.split(";"))
            read.append(Element.Element(int(id), int(length)))
        return read

test=readfile('sample.txt')
print(test[0].elementID)


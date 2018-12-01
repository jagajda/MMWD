# definition of Element class and methods
class Element:

    def __init__(self, elementLength, elementID):
        self.elementLength = elementLength
        self.elementID = elementID
        self.value = getValue(selfelementLength)

    # returns price of the element, based on it's length


def getValue(length):
    if length < 0:
        return None
    elif 0 <= length < 5:
        return length * 1.5
    elif 5 < length < 10:
        return length * 1.75
    elif 10 < length < 15:
        return length * 2
    elif 15 < length < 20:
        return length * 2.25
    elif length > 20:
        return length * 2.5


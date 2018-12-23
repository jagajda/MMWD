import random
def crossover (crossoverList, crossType):
    #numberOfElements = len(crossoverList)
    numberOfElements = 10
    mothers = []
    fathers = []
    children = []
    mothers = random.sample (crossoverList, len(crossoverList)//2)
    for i in range (len (crossoverList)):
        if crossoverList [i] not in mothers:
            fathers.append (crossoverList [i])
    for i in range (len (mothers)):
        if crossType == 0:
            crossPoint = random.randint (numberOfElements/2 - 1, numberOfElements/2 + 1)
        elif crossType == 1:
            crossPoint = random.randint (numberOfElements/2 - 2, numberOfElements/2 + 2)
        elif crossType == 2:
            crossPoint = random.randint (0, numberOfElements - 1)
        child1 = mothers [i][:crossPoint] + fathers [i][crossPoint+1:]
        child2 = fathers [i][:crossPoint] + mothers [i][crossPoint+1:]
        children.append (child1)
        children.append (child2)
    return children

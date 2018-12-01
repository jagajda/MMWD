def crossover (crossoverList):
    numberOfElements = length (crossoverList[0])
    mothers = []
    fathers = []
    children = []
    mothers = random.sample (crossoverList, len (crossoverList / 2))
    for i in range (len (crossoverList)):
        if crossoverList [i] not in mothers:
            fathers.append (crossoverList [i])
    for i in range (len (mothers)):
        crossPoint = random.randint (0, numberOfElements - 1)
        child1 = mothers [i][:crossPoint] + fathers [i][crossPoint+1:]
        child2 = fathers [i][:crossPoint] + mothers [i][crossPoint+1:]
        children.append (child1)
        children.append (child2)
    return children

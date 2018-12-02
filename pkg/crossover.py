def crossover (specimensList):
    numberOfElements = length (specimensList[0])
    mothers = []
    fathers = []
    children = []
    mothers = random.sample (specimensList, len (specimensList / 2))
    for i in range (len (specimensList)):
        if specimensList [i] not in mothers:
            fathers.append (specimensList [i])
    for i in range (len (mothers)):
        crossPoint = random.randint (0, numberOfElements - 1)
        child1 = mothers [i][:crossPoint] + fathers [i][crossPoint + 1:]
        child2 = fathers [i][:crossPoint] + mothers [i][crossPoint + 1:]
        children.append (child1)
        children.append (child2)
    return children

def mutation (specimensList):
    numberOfElements = len (specimensList [0])
    for i in range (len (specimensList)):
        mutationPoint = random.randint (0, numberOfElements - 1)
        specimensList [i][mutationPoint] = specimensList [i][mutationPiont] + random.randint (-5, 5)
    return specimensList
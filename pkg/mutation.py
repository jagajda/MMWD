def mutation (specimensList, mutType):
    numberOfElements = len (specimensList [0])
    for i in range (len (specimensList)):
        mutationPoint = random.randint (0, numberOfElements - 1)
        if mutType == 0:
            specimensList [i][mutationPoint] = specimensList [i][mutationPiont] + random.randint (-1, 1)
        elif mutType == 1:
            specimensList [i][mutationPoint] = specimensList [i][mutationPiont] + random.randint (-3, 3)
        elif mutType == 2:
            specimensList [i][mutationPoint] = specimensList [i][mutationPiont] + random.randint (-5, 5)
    return specimensList

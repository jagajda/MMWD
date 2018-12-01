def mutation (mutationList):
    numberOfElements = len (mutationList [0])
    for i in range (len (mutationList)):
        mutationPoint = random.randint (0, numberOfElements - 1)
        mutationList [i] = mutationList [i] + random.randint (-5, 5)
    return mutationList

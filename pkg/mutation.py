<<<<<<< HEAD
def mutation (specimensList):
    numberOfElements = len (specimensList [0])
    for i in range (len (specimensList)):
        mutationPoint = random.randint (0, numberOfElements - 1)
        specimensList [i] = specimensList [i] + random.randint (-5, 5)
    return specimensList
=======
def mutation (mutationList):
    numberOfElements = len (mutationList [0])
    for i in range (len (mutationList)):
        mutationPoint = random.randint (0, numberOfElements - 1)
        mutationList [i] = mutationList [i] + random.randint (-5, 5)
    return mutationList
>>>>>>> 0f18e7f1b22f7730caaf160c68104831d4e9eedf

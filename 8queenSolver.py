import random
def view(li, index):
    print()
    print(f"Solution number {index + 1}: ", end='')
    print(li)
    print()

    for i in range(8):
        x = li[i] - 1
        for j in range(8):
            if j == x:
                print('[Q]', end='')
            else:
                print('[ ]', end='')
        print()

    print()


def getHuristic(instance):
    huristic = []
    for i in range(len(instance)):
        j = i - 1
        huristic.append(0)
        while j >= 0:
            if instance[i] == instance[j] or (abs(instance[i] - instance[j]) == abs(i - j)):
                huristic[i] += 1
            j -= 1
        j = i + 1
        while j < len(instance):
            if instance[i] == instance[j] or (abs(instance[i] - instance[j]) == abs(i - j)):
                huristic[i] += 1
            j += 1
    return huristic


def getFitness(instance):
    '''
    This method define to get the fitness value of given instance
    :param instance: We have to pass an array of with queen indexes
    :return: Fitness value of given instance
    '''
    numberOfVoilations = 0                                    # Initialize the numberOfVoilations to 0
    for i in range(len(instance) - 1):                        # Iterate for all the queens in the instance
        for j in range(i + 1, len(instance)):                 # Iterate for all the queens next to i in the instance
            if instance[i] == instance[j]:                    # Check the placement of queen with others queen is same row wise or colunm wise
                numberOfVoilations += 1                       # Increment numberOfVoilations by 1
    for i in range(len(instance) - 1):                        # Iterate for all the queens in the instance
        for j in range(i + 1, len(instance)):                 # Iterate for all the queens in the instance
            if abs(instance[j] - instance[i]) == abs(j - i):  # Check the placement of queen with others queen diagonally
                numberOfVoilations += 1                       # Increment numberOfVoilations by 1
    return 28 - numberOfVoilations                            # Return totalfitnessPossible - numberOfVoilation = currentInstanceFitness

def buildKid(instance1, instance2, crossOver):
    newInstance = []
    for i in range(crossOver):
        newInstance.append(instance1[random.randint(0, 7)])
    for i in range(crossOver, 8):
        newInstance.append(instance2[random.randint(0, 7)])
    return newInstance


def changeChilds(co):
    global parent1, parent2, child1, child2, crossover
    crossover = co
    child1 = buildKid(parent1, parent2, crossover)
    child2 = buildKid(parent2, parent1, crossover)


def changeChromosome(li):
    global crossover, parent1, parent2
    newchange = -1
    while newchange != 0:
        newchange = 0
        tmpli = li
        getHur = getHuristic(tmpli)
        index = getHur.index(max(getHur))
        maxFitness = getFitness(tmpli)
        for i in range(1, 9):
            tmpli[index] = i
            if getFitness(tmpli) > maxFitness:
                maxFitness = getFitness(tmpli)
                newchange = i
            tmpli = li
        if newchange == 0:
            for i in range(len(li) - 1):
                for j in range(i + 1, len(li)):
                    if li[i] == li[j]:
                        li[j] = random.randint(1, 8)
        else:
            li[index] = newchange


if __name__ == "__main__":
    print("Enter number of solution you want: ")
    numberOfSolutions = int(input())
    solutions = []
    crossover = 4                           # Crossover point
    while len(solutions) < numberOfSolutions:
        parent1 = []                            # To build up the parent1
        parent2 = []                            # To build up the parent2

        for i in range(8):
            parent1.append(random.randint(1, 8))
            parent2.append(random.randint(1, 8))
        fitnessFather = getFitness(parent1)
        fitnessMother = getFitness(parent2)
        while fitnessFather != 28 and fitnessMother != 28:
            changeChilds(crossover)
            changeChromosome(child1)
            changeChromosome(child2)
            fitnessFather = getFitness(child1)
            fitnessMother = getFitness(child2)
            parent1 = child1
            parent2 = child2
            print(parent1)
            print(parent2)
        if getFitness(parent1) == 28:
            if parent1 not in solutions:
                solutions.append(parent1)
        else:
            if parent2 not in solutions:
                solutions.append(parent2)

    print("********************** Solutions **********************")
    print(f"The number of solutions you wanted: {numberOfSolutions}")

    for i in range(len(solutions)):
        view(solutions[i], i)

    print("*******************************************************")

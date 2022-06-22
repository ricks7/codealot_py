from random import Random
from codealot.Codealot import Codealot
from codealot.KnightPosition import KnightPosition


if __name__ == "__main__":

    numberOfKnights = 6
    codealot = Codealot(numberOfKnights)

    random = Random(1)
    for hour in range(24):
        positions = list()
        for knight in range(numberOfKnights):
            randomVal = random.randint(0, 1)
            if randomVal == 0:
                positions.append(KnightPosition.TRAINING_YARD)
            elif randomVal == 1:
                positions.append(KnightPosition.TAVERN)
        codealot.moveKnights(positions)
        codealot.process()

    codealot.grantBonusXp()
    totalXp = codealot.calculateEarnedXp()

    print("Total XP earned by all " + str(numberOfKnights) + " knights: " + str(totalXp))



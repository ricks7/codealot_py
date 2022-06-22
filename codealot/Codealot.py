from codealot.KnightPosition import KnightPosition
from codealot.Knight import Knight


class Codealot:

    def __init__(self, number_of_knights):
        self.knights = list()
        # I chose the tavern as the arbitrary starting place of knights
        # It should be changed before an hour is actually processed
        for i in range(number_of_knights):
            self.knights.append(Knight(KnightPosition.TAVERN))

    def process(self):
        for knight in self.knights:
            knight.process()

    def calculateEarnedXp(self):
        total = 0
        for knight in self.knights:
            total += knight.getXp()
        return total

    def moveKnights(self, positions: list[KnightPosition]):
        if len(positions) > len(self.knights):
            raise Exception("Tried to move more knights than exist in Codealot")
        else:
            for i, position in enumerate(positions):
                self.knights[i].move(position)

    def grantBonusXp(self):
        bonusKnights = 0
        for knight in self.knights:
            if knight.isBonus():
                bonusKnights += 1

        if bonusKnights == 3:
            for knight in self.knights:
                if knight.isBonus():
                    knight.addXp(5)

        if bonusKnights == 5:
            for knight in self.knights:
                if knight.isBonus():
                    knight.addXp(10)

        if bonusKnights == 6:
            for knight in self.knights:
                if knight.isBonus():
                    knight.addXp(20)
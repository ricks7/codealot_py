from codealot.KnightPosition import KnightPosition


class Knight(object):

    def __init__(self, position: KnightPosition):
        self.__xp = 0
        self.__stamina = 0
        self.__position = position

    def move(self, position: KnightPosition):
        self.__position = position

    def process(self):
        match self.__position:
            case KnightPosition.TAVERN:
                self.__stamina += 1
            case KnightPosition.TRAINING_YARD:
                self.__xp += 1
                self.__stamina -= 1

    def getXp(self):
        return self.__xp

    def addXp(self, xp):
        self.__xp += xp

    def isBonus(self):
        return self.__xp >= 3

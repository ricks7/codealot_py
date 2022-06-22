from codealot.Codealot import Codealot
from codealot.KnightPosition import KnightPosition

numberOfKnights = 12
codealot = Codealot(numberOfKnights)

positions = [
    KnightPosition.TAVERN,
    KnightPosition.TAVERN,
    KnightPosition.TRAINING_YARD,
    KnightPosition.TRAINING_YARD,
    KnightPosition.TRAINING_YARD,
    KnightPosition.TRAINING_YARD,
    KnightPosition.TAVERN,
    KnightPosition.TAVERN,
    KnightPosition.TRAINING_YARD,
    KnightPosition.TRAINING_YARD,
    KnightPosition.TRAINING_YARD,
    KnightPosition.TRAINING_YARD
]

codealot.moveKnights(positions)
codealot.process()

assert (codealot.calculateEarnedXp() == 8)

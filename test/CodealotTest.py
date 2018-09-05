from test.BasicCodalot import BasicCodalot
from test.KnightPosition import KnightPosition

codalot = BasicCodalot()

codalot.setKnight(0, KnightPosition.TAVERN)
codalot.setKnight(1, KnightPosition.TAVERN)
codalot.setKnight(2, KnightPosition.TRAINING_YARD)
codalot.setKnight(3, KnightPosition.TRAINING_YARD)
codalot.setKnight(4, KnightPosition.TRAINING_YARD)
codalot.setKnight(5, KnightPosition.TRAINING_YARD)
codalot.process()

assert (codalot.calculateEarnedXp() == 4)

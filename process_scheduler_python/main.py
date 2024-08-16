from algorithms.fcfs import FCSF
from utils.process import Process

# FCFS simulation exemple
fcsf = FCSF([Process(1, 5), Process(2, 3), Process(3, 8), Process(4, 6)])
fcsf.run()

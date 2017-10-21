from math import sqrt
import time
import threading
import sys
import signal

from config import *
from communication import *
config = Config()
com = Communication()

from interface import *

def menu_commande(signal, frame):
        Communication().pause()
        robot.stop()
        interface = Interface()
signal.signal(signal.SIGINT, menu_commande)



from robot import *
robot = Robot()
robot.start()



from obstacle import *
from carte import *
from action import *
from deplacement import *
from chemin import *
from parcours import *
from ultrason import *
from urgence import *

carte = Carte()
print(1)
parcours = Parcours(robot,carte)





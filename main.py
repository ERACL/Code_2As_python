from math import sqrt
import time
import threading

from config import *
from communication import *
config = Config()
com = Communication()

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
parcours = Parcours(robot,carte)





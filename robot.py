from threading import Thread
from config import *
from communication import *
import time

class Robot(Thread):
   
   def __init__(self):
      Thread.__init__(self)
      if (True):  #Mettre un test pour savoir si on commence à droite
         self.x = Config().get_x_init_d()
         self.y = Config().get_y_init_d()
         self.theta = Config().get_theta_init_d()
      else:
         self.x = Config().get_x_init_g()
         self.y = Config().get_y_init_g()
         self.theta = Config().get_theta_init_g()
      Communication().set_donnees(self.x,self.y,self.theta)
      self.etat = True
      self.on = True
      
   def run(self):
      tini = time.time()
      while (self.on):
         time.sleep(0.1)
         donnees = Communication().get_donnees()
         self.x, self.y,self.theta = donnees[0],donnees[1],donnees[2]
      return None

   def get_position(self):
      return (self.x,self.y)

   def get_angle(self):
      return self.theta
   
   def arret_robot(self):
      Communication().pause()
      donnees = Communication.get_donnees()
      self.x, self.y,self.theta = donnees[0],donnes[1],donnees[2]
      return None

   def redemarrage_robot(self):
      Communcation().play()
      return None
   
   def get_donnees(self):
      return (self.x,self.y,self.theta)
   
   def stop(self):
      self.on = False
      return None
      



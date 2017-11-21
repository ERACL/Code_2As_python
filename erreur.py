import time
from threading import Thread

class CheminFaux(Exception):
   pass

class ActionLongue(Exception):
   pass

class ErreurActionneur(Exception):
   pass

class TestChemin(Thread):
   
   def __init__(self,temps):
      self.temps = temps
      self.on == True
   
   def run(self):
      debut = time.time()
      while (time.time()<debut + self.temps) and (self.on == True):
         time.sleep(0.2)
      if (self.on == True):
         raise CheminFaux
      return None
   
   def stop(self):
      self.on = False
      return None

class TestAction(Thread):
   
   def __init__(self,temps):
      self.temps = time.time()
      self.on = True
   
   def run(self):
      debut = time.time()
      while (time.time()<debut+self.temps()):
         time.sleep(0.2)
      if (self.on == True):
         raise ActionLongue
      return None
   
   def stop(self):
      self.on = False
      return None      
      

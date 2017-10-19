
class Robot(threading.Thread):
   
   def __init__(self):
      threading.Thread.__init__(self)
      if (True):  #Mettre un test pour savoir si on commence à droite
         self.x = Communication().get_x_init_d()
         self.y = Communication().get_y_init_d()
         self.theta = Communication().get_theta_init_d()
      else:
         self.x = Communication().get_x_init_g()
         self.y = Communication().get_y_init_g()
         self.theta = Communication().get_theta_init_g()
      Communication().set_donnes(x,y,theta)
      self.etat = True
      
   def run(self):
      time.sleep(0.1)
      donnees = Communication().get_donnees()
      self.x, self.y,self.theta = donnees[0],donnes[1],donnees[2]
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



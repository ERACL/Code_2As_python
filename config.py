import os

#Cette classe a pour objectif de charger le fichier de configuration "config.cfg"

class Config():
   

   fichier = open("config.cfg", "r")
   ligne = fichier.read().split("\n")
   for i in range(len(ligne)-1):
      k = ligne[i]
      L = k.split(" = ")
      assert len(L)==2
      if L[0] == "largeur_du_robot" :
         largeur_du_robot = int(L[1])
      elif L[0] == "longueur_du_robot" :
         longueur_du_robot = int(L[1])
      elif L[0] == "largeur_terrain" :
         largeur_terrain = int(L[1])
      elif L[0] == "longueur_terrain" :
         longueur_terrain = int(L[1])
      elif L[0] == "ecart_de_surete" :
         ecart_de_surete = int(L[1])
      elif L[0] == "X" :
         X = int(L[1])      
      elif L[0] == "x_init_g" : #X et Y sont la taille de la carte
         x_init_g = int(L[1])
      elif L[0] == "y_init_g" : #X et Y sont la taille de la carte
         y_init_g = int(L[1])
      elif L[0] == "theta_init_g" : #X et Y sont la taille de la carte
         theta_init_g = int(L[1])
      elif L[0] == "x_init_d" : #X et Y sont la taille de la carte
         x_init_d = int(L[1])
      elif L[0] == "y_init_d" : #X et Y sont la taille de la carte
         y_init_d = int(L[1])
      elif L[0] == "theta_init_d" : #X et Y sont la taille de la carte
         theta_init_d = int(L[1])
      elif L[0] == "precision":
         precision = int(L[1])
      elif L[0] == "precision_theta":
         precision_theta = int(L[1])
      else:
         try:
            assert True==False
         except AssertionError:
            print("Le fichier de configuration a ete mal encodé")
   dx = longueur_terrain/X
   Y = largeur_terrain/dx
   

   def __init__(self):
      return None
   
   @classmethod
   def get_largeur_du_robot(self):
      return self.largeur_du_robot
   
   @classmethod
   def get_longueur_du_robot(self):
      return self.longueur_du_robot
   
   @classmethod
   def get_largeur_terrain(self):
      return self.largeur_terrain
   
   @classmethod
   def get_longueur_terrain(self):
      return self.longueur_terrain
   
   @classmethod
   def get_ecart_de_surete(self):
      return self.ecart_de_surete
   
   @classmethod
   def get_dx(self):
      return self.dx
   
   @classmethod
   def get_Y(self):
      return self.Y
   
   @classmethod
   def get_X(self):
      return self.X
   
   @classmethod
   def get_x_init_d(self):
      return self.x_init_d
   
   @classmethod
   def get_y_init_d(self):
      return self.y_init_d
   
   @classmethod
   def get_theta_init_d(self):
      return self.theta_init_d
   
   @classmethod
   def get_x_init_g(self):
      return self.x_init_g
   
   @classmethod
   def get_y_init_g(self):
      return self.y_init_g
   
   @classmethod
   def get_theta_init_g(self):
      return self.theta_init_g
   
   @classmethod
   def get_precision(self):
      return self.precision

   @classmethod
   def get_precision_theta(self):
      return self.precision_theta
   

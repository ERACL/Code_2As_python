import time
from fonction_chemin_grossier import *
from config import *
class Chemin():
   
   def __init__(self,carte, position_ini, position_fin):
      self.carte = carte
      self.P1 = (position_ini[0],position_ini[1])
      self.P2 = (position_fin[0],position_fin[1])
      print(self.P1,self.P2)
      self.angle_ini = position_ini[2]
      self.angle_fin = position_fin[2]
      self.chemin = self.calcul_chemin()

   
   def calcul_chemin(self):
      dx = Config().get_dx()
      chemin = self.chemin_grossier()
      try:
         assert len(chemin)!=0
      except AssertionError:
         print("Le calcul du chemin s'est mal déroulé")
      compteur = 0
      mouv_prece = ""
      trajet = []
      for k in chemin:
         if (compteur==0):
            compteur = 1
            mouv_prece = k
         else:
            if (mouv_prece == k):
               compteur += 1
            else:
               if (len(mouv_prece) == 4):
                  trajet.append((mouv_prece, dx*compteur*sqrt(2)))
               else:
                  trajet.append((mouv_prece,dx*compteur))
               
      return trajet

   def chemin_grossier(self):
      return fonction_chemin_grossier(self.P1,self.P2,self.carte.get_map())
   
   def get_chemin(self):
      return self.chemin
       

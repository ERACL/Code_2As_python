import time

class Chemin():
   from fonction_chemin_grossier import *
   def __init__(self, position_ini, position_fin):
      self.Pi = position_ini[0]
      self.Pf = position_fin[0]
      self.angle_ini = position_ini[1]
      self.angle_fin = position_fin[1]
      self.chemin = self.calcul_chemin()
   
   def calcul_chemin(self,P1,P2):
      global dx
      chemin = self.chemin_grossier(P1,P2)
      try:
         assert len(chemin)!=0
      except AssertionError:
         print("Le calcul du chemin s'est mal déroulé")
      compteur = 0
      Pini = P1
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
               if (len(mouv_prece) == 3):
                  trajet.append((mouv_prece, dx*compteur*sqrt(2)))
               else:
                  trajet.append((mouv_prece,dx*compteur))
               
      return trajet

   def chemin_grossier(self,P1,P2):
      return fonction_chemin_grossier(P1,P2)
       

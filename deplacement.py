from chemin import *
class Deplacement():
   
   def __init__(self,robot,position_fin,carte):
      self.position_fin = position_fin 
      self.position_ini = robot.get_donnees()
      self.chemin = Chemin(carte,self.position_ini,self.position_fin)
      self.robot = robot
   
      
   def tourner(self,theta_ini,theta_fin):
      """Met tout en oeuvre pour orienter le robot dans le bon sens"""
      theta = theta_fin - theta_ini
      if (theta<0):
         theta += 360 #La convention de communication est un angle entre 0 et 360
      Communication().tourner(theta)
      return None

   def deplacement_elem(self,deplacement):
      
      theta = None
      if (deplacement[0] == "de"):
         theta = 180
      elif (deplacement[0] == 'mo'):
         theta = 0
      elif (deplacement[0] == "dr"):
         theta = 90
      elif (deplacement[0] == 'ga'):
         theta = 270
      elif (deplacement[0] == 'dedr'):
         theta = 135
      elif (deplacement[0] == 'modr'):
         theta = 45
      elif (deplacement[0] == 'dega'):
         theta = 225
      elif (deplacement[0] == 'dedr'):
         theta = 315
      else:
         try:
            assert True == False
         except AssertionError:
            print("Bug dans la lecture du chemin")
      donnees = self.robot.get_donnees()
      self.tourner(donnes[2],theta)
      Communication().avancer(deplacement[1])
       
   def aller_a(self):
      precision = Config().get_precision()
      trajet = self.chemin.get_chemin()
      for k in trajet :
         position_ini = self.robot.get_donnees()
         self.deplacement_elem(k)
         position_fin = self.robot.get_donnees()
         distance_parcourue = sqrt((position_ini[0]-position_fin[0])**2+(position_ini[1]-position_fin[1])**2)
         if (distance_parcourue>k[1]-precision) and (distance_parcourue<k[1]+prcision) :
            continue
         else:
            #Ici, le robot n'a pas avancé de la distance demandée, on lui demande d'avancer la distance manquante
            if (distance_parcourue>=k[1]+precision):
               self.deplacement_elem((k[0],distance_parcourue-k[1]))
            else:
               self.deplacement_elem((k[0],k[1]-distance_parcourue))
      return None




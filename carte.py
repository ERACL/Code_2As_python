class Carte():
   
   def __init__(self):
      self.X = Config().get_X()
      self.Y = Config().get_Y()
      self.map = [[0 for i in range(self.Y)] for j in range(self.X) ]
      self.map_vrai =  [[0 for i in range(self.Y)] for j in range(self.X) ] #map_vrai permet de stocker les endroits réels des obstacles
      
   
   def verification(self,P1,P2):
      """Vérifie la présence d'un obstacle dans le rectangle P1 P2"""
      P3 = (min(P1[0],P2[0]),min(P1[1],P2[1]))
      P4 = (max(P1[0],P2[0]),max(P1[1],P2[1]))
      for i in range(P3[0],P4[0]+1):
         for j in range(P3[1],P4[1]+1):
            if (self.map_vrai()[i][j] != 0.5):
               return False
      return True

   def ajouter_obs(self,P1,P2):
      global longueur_du_robot,ecart_de_surete, longueur_terrain, largeur_terrain, dx
      #On écrit d'abord dans map_vrai les vraies positions de l'obstacle
      P3 = (min(P1[0],P2[0]),min(P1[1],P2[1]))
      P4 = (max(P1[0],P2[0]),max(P1[1],P2[1]))
      for i in range(P3[0],P4[0]+1):
         for j in range(P3[1],P4[1]+1):
            self.map_vrai()[i][j] = 0.5
      #On écrit ensuite les positions de l'obstacle en prenant en compte l'écart de sécurité et la largeur du robot
      L = longueur_du_robot+ecart_de_surete
      P3 = (max(P1[0],P2[0]),max(P1[1],P2[1]))
      P4 = (min(P1[0],P2[0]),min(P1[1],P2[1]))
      P3 = (min(P3[0]+L/2,longueur_terrain),min(P3[1]+L/2,largeur_terrain))
      P4 = (max(P4[0]-L/2,0),max(P4[1]-L/2,0))
      P3 = (int(P3[0]/dx),int(P3[1]/dx))  
      P4 = (int(P4[0]/dx),int(P4[1]/dx))
      for i in range(P3[0],P4[0]+1):
         for j in range(P3[1],P4[1]+1):
            self.map()[i][j] = 0.5
      return None
   
   def retirer_obs(self,P1,P2):
      global longueur_du_robot,ecart_de_surete, longueur_terrain, largeur_terrain, dx
      #On retire d'abord dans map_vrai les vraies positions de l'obstacle
      P3 = (min(P1[0],P2[0]),min(P1[1],P2[1]))
      P4 = (max(P1[0],P2[0]),max(P1[1],P2[1]))
      for i in range(P3[0],P4[0]+1):
         for j in range(P3[1],P4[1]+1):
            self.map_vrai()[i][j] = 0
      #On retire ensuite les positions de l'obstacle en prenant en compte l'écart de sécurité et la largeur du robot
      L = longueur_du_robot+ecart_de_surete
      P3 = (max(P1[0],P2[0]),max(P1[1],P2[1]))
      P4 = (min(P1[0],P2[0]),min(P1[1],P2[1]))
      P3 = (min(P3[0]+L/2,longueur_terrain),min(P3[1]+L/2,largeur_terrain))
      P4 = (max(P4[0]-L/2,0),max(P4[1]-L/2,0))
      P3 = (int(P3[0]/dx),int(P3[1]/dx))  
      P4 = (int(P4[0]/dx),int(P4[1]/dx))
      for i in range(P3[0],P4[0]+1):
         for j in range(P3[1],P4[1]+1):
            self.map()[i][j] = 0
      return None

    
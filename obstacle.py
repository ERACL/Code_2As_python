class obstacle():
   
   #temp vaut False si l'obstacle est permanent et True s'il est temporaire
   #carte est du type Carte (toujours utile de le savoir)

   def __init__(self,carte,P1,P2,temp):
      self.temp = temp
      self.P1 = P1
      self.P2 = P2
      carte.ajouter_obs(self,P1,P2)
   
   def __del__(self,carte):
      carte.retirer_obs(self.P1,self.P2)
      return None
   
   def get_temp(self):
      return self.temp

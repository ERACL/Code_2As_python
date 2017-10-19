class Action():
   
   def __init__(self,robot,position,action,carte):
      self.carte = carte
      self.position = position #Position a laquele l'action est realisee
      self.action = action
      self.robot = robot
   
   def executer(self):
      """Execute l'action"""
      self.deplacer()
      self.action_a_realiser()
   
   def action_a_realiser(self):
      """Cette fonction gere toute la partie de l'action qui n'est pas un déplacement (activation de pinces...)"""
      return None
   
   def deplacer(self):
      """deplacer gere le deplacement du robot à l'endroit ou l'action doit etre realisee"""
      Deplacement(self.robot,self.position)
      test = self.verifier_et_corriger()
      #On peut placer ici un time pour vérifier que le déplacement ne prenne pas trop de temps
      while (test != "bien place"):
         if (test=="position fausse"):
            Deplacement(self.robot,self.position, self.carte)
         else:
            try:
               assert test == "angle faux"
            except AssertionError:
               print("La valeur de test n'est pas cohérente, elle vaut ",test)
            theta_robot = robot.get_donnees()[2]
            theta = theta_robot - self.position[2]
            if (theta<0):
               theta += 360
            Communication().tourner(theta)
      return None
   
   def verifier_et_corriger(self):
      """Cette fonction verifie la position du robot et le cas echeant le replace pour qu'il soit a la position demandee"""
      precision = Config().get_precision()
      precision_theta = Config().get_precision_theta()
      donnees = self.robot.get_donnees()
      x_action = self.position[0]
      y_action = self.position[1]
      theta_action = self.position[2]
      delta_x = x_acton-donnees[0]
      delta_y = y_action-donnees[1]
      delta_theta = theta_action-donnees[2]
      if sqrt(delta_x**2+delta_y**2)>precision:
         #self.deplacer(self.robot,self.position)
         return "position fausse"
      if (abs(delta_theta)>precision_theta):
         return "angle faux"
      return "bien place"

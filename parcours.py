class Parcours():
   def __init__(self,robot,carte):
      self.robot = robot
      self.carte = carte
      self.liste_action = []
      self.charger_actions()
      self.creer_actions()
      self.demarrer()
      return None
   
   def charger_actions(self):
   """Charge les actions depuis le fichier actions.cfg"""
      fichier = open("actions.cfg", "r")
      ligne = fichier.read().split("\n")
      noms = []
      positions_x = [] 
      positions_y = []
      try:
         for k in range(len(ligne)-1):
            donnees = k.split(" ")
            noms.append(donnees[0])
            coordonnees = donnees[1].split(",")
            positions_x.append(int(coordonnees[0]))
            positions_y.append(int(corrdonnees[1]))
         self.liste_action = []
         for k in range(len(ligne)-1):
            self.liste_action.append((noms[k],(position_x[k],position_y[k])))
      except:
         print("le fichier des actions a été mal édité")
      return None
   
   def creer_actions(self):
      """Les objets Actions sont crees dans cette fonction"""
      for k in len(self.liste_action):
         liste_action[k]=Action(self.robot,liste_action[k][0],liste_action[k][1],self.carte)
      return None
   
   def demarrer(self):
      for k in self.liste_action:
         k.executer()
      return None
      

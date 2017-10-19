from action import *
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
      positions_theta = []
      try:
         for k in range(len(ligne)-1):
            donnees = ligne[k].split(" ")
            noms.append(donnees[0])
            coordonnees = donnees[1].split(",")
            positions_x.append(int(coordonnees[0]))
            positions_y.append(int(coordonnees[1]))
            positions_theta.append(int(coordonnees[2]))
         self.liste_action = []
         for k in range(len(ligne)-1):
            self.liste_action.append((noms[k],(positions_x[k],positions_y[k],positions_theta[k])))
      except:
         print("le fichier des actions a été mal édité")
      return None
   
   def creer_actions(self):
      """Les objets Actions sont crees dans cette fonction"""
      for k in range(len(self.liste_action)):
         self.liste_action[k]=Action(self.robot,self.liste_action[k][1],self.liste_action[k][0],self.carte)
      return None
   
   def demarrer(self):
      for k in self.liste_action:
         k.executer()
      return None
      

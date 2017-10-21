import os
from communication import *
import sys

class Interface():
   
   def __init__(self):
      self.menu()
      return None
   
   def menu_commande(self):
      os.system('clear')
      print('\nBienvenue dans le menu de commande du robot en direct ! Voici les differentes options :')
      print('\n1. avancer(distance)')
      print('\n2. reculer(distance)')
      print('\n3. tourner(angle)')
      print('\n4. quitter')
      reponse_valide = False
      reponse = None
      while (reponse_valide == False):
         reponse = input("\nEntrez votre reponse : \n")
         try:
            reponse = int(reponse)
            if (reponse == 1) or (reponse == 2) or (reponse == 3) or (reponse == 4):
               reponse_valide = True
            else:
               print("\nVotre reponse n'est pas valide")
         except:
            print("\nVotre reponse n'est pas valide")
      return reponse
   
   def menu(self):
      while True:
         entree = self.menu_commande()
         bibliotheque = {
           1: self.avancer,
           2: self.reculer,
           3: self.tourner,
           4: self.shutdown,
         }
         bibliotheque[entree]()
      return None
   
   def avancer(self):
      reponse_valide = False
      reponse = None
      while (reponse_valide == False):
         reponse = input("\nDe combien souhaitez-vous avancer?\n")
         try:
            reponse = int(reponse)
            reponse_valide = True
         except:
            print("\nVotre reponse n'est pas valide")
      Communication().avancer(reponse)
      return None
   
   def reculer(self):
      reponse_valide = False
      reponse = None
      while (reponse_valide == False):
         reponse = input("\nDe combien souhaitez-vous reculer?\n")
         try:
            reponse = int(reponse)
            reponse_valide = True
         except:
            print("\nVotre reponse n'est pas valide")
      Communication().reculer(reponse)
      return None
   
   
   def tourner(self):
      reponse_valide = False
      reponse = None
      while (reponse_valide == False):
         reponse = input("\nDe combien souhaitez-vous tourner?\n")
         try:
            reponse = int(reponse)
            reponse = reponse%360
            reponse_valide = True
         except:
            print("\nVotre reponse n'est pas valide")
      Communication().tourner(reponse)
      return None
      
   def shutdown(self):
      Communication().shutdown()
      os._exit(1)
      return None

         


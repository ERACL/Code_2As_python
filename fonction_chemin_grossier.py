from math import sqrt
def fonction_chemin_grossier(depart, arrivee, Map):
   """L'objectif de cette fonction est de trouver le déplacement global du robot. Il est ici assimilé à une case carrée."""
   
   L1 = [depart]
   # Listes des dernières cases à points positifs que l'on a visirées
   
   L2 = [arrivee]
   # Listes des dernières cases à points négatifs que l'on a visirées
   
   fin = []
   #fin stockera les coordonnées finales du point de rencontre
   X = len(Map)
   Y =  len(Map[0])
   compteur = 0
   stop = False
   Map[depart[0]][depart[1]] = 0
   Map[arrivee[0]][arrivee[1]] = 0 
   while not(stop):
   #Les deux goutes d'huiles se répendent dans la Map. Lorsqu'elles se renctontrent, stop vaut True et on sort de la boucle for.
      compteur+=1
      M = []
      for k in L1:
         if (k[0]>0) and (Map[k[0]-1][k[1]]<=0) :
            M.append((k[0]-1,k[1]))
            if Map[k[0]-1][k[1]]==0 :
               Map[k[0]-1][k[1]]=compteur
            else :
               stop = True
               fin =(Map[k[0]-1][k[1]],k[0]-1,k[1])
               break
         if (k[0]<X-1) and (Map[k[0]+1][k[1]]<=0) :
            M.append((k[0]+1,k[1]))
            if Map[k[0]+1][k[1]]==0 :
               Map[k[0]+1][k[1]]=compteur
            else :
               stop = True
               fin =(Map[k[0]+1][k[1]],k[0]+1,k[1])
               break
         if (k[1]>0) and (Map[k[0]][k[1]-1]<=0) :
            M.append((k[0],k[1]-1))
            if Map[k[0]][k[1]-1]==0 :
               Map[k[0]][k[1]-1]=compteur
            else :
               stop = True
               fin =(Map[k[0]][k[1]-1],k[0],k[1]-1)
               break
         if (k[1]<Y-1) and (Map[k[0]][k[1]+1]<=0) :
            M.append((k[0],k[1]+1))
            if Map[k[0]][k[1]+1]==0 :
               Map[k[0]][k[1]+1]=compteur
            else :
               stop = True
               fin =(Map[k[0]][k[1]+1],k[0],k[1]+1)
               break
         
         if (k[1]>0) and (k[0]>0) and (Map[k[0]-1][k[1]]!=0.5) and (Map[k[0]][k[1]-1]!=0.5) and (Map[k[0]-1][k[1]-1]<=0):
            M.append((k[0]-1,k[1]-1))
            if Map[k[0]-1][k[1]-1]==0 :
               Map[k[0]-1][k[1]-1]=compteur
            else :
               stop = True
               fin =(Map[k[0]-1][k[1]-1],k[0]-1,k[1]-1)
               break
         if (k[1]<Y-1) and (k[0]>0) and (Map[k[0]-1][k[1]]!=0.5) and (Map[k[0]][k[1]+1]!=0.5) and (Map[k[0]-1][k[1]+1]<=0):
            M.append((k[0]-1,k[1]+1))
            if Map[k[0]-1][k[1]+1]==0 :
               Map[k[0]-1][k[1]+1]=compteur
            else :
               stop = True
               fin =(Map[k[0]-1][k[1]+1],k[0]-1,k[1]+1)
               break
         if (k[1]<Y-1) and (k[0]<Y-1) and (Map[k[0]+1][k[1]]!=0.5) and (Map[k[0]][k[1]+1]!=0.5) and (Map[k[0]+1][k[1]+1]<=0):
            M.append((k[0]+1,k[1]+1))
            if Map[k[0]+1][k[1]+1]==0 :
               Map[k[0]+1][k[1]+1]=compteur
            else :
               stop = True
               fin =(Map[k[0]+1][k[1]+1],k[0]+1,k[1]+1)
               break
         if (k[1]>0) and (k[0]<Y-1) and (Map[k[0]+1][k[1]]!=0.5) and (Map[k[0]][k[1]-1]!=0.5) and (Map[k[0]+1][k[1]-1]<=0):
            M.append((k[0]+1,k[1]-1))
            if Map[k[0]+1][k[1]-1]==0 :
               Map[k[0]+1][k[1]-1]=compteur
            else :
               stop = True
               fin =(Map[k[0]+1][k[1]-1],k[0]+1,k[1]-1)
               break
      L1[:] = M[:]
      M = [] 
      compteur = -compteur
      if not(stop):
         for k in L2:
            if (k[0]>0) and (Map[k[0]-1][k[1]]!=0.5) and (Map[k[0]-1][k[1]]>=0) :
               M.append((k[0]-1,k[1]))
               if Map[k[0]-1][k[1]]==0 :
                  Map[k[0]-1][k[1]]=compteur
               else :
                  stop = True
                  fin =(Map[k[0]-1][k[1]],k[0]-1,k[1])
                  break
            if (k[0]<X-1) and (Map[k[0]+1][k[1]]!=0.5) and (Map[k[0]+1][k[1]]>=0):
               M.append((k[0]+1,k[1]))
               if Map[k[0]+1][k[1]]==0 :
                  Map[k[0]+1][k[1]]=compteur
               else :
                  stop = True
                  fin =(Map[k[0]+1][k[1]],k[0]+1,k[1])  
                  break
            if (k[1]>0) and (Map[k[0]][k[1]-1]!=0.5) and (Map[k[0]][k[1]-1]>=0):
               M.append((k[0],k[1]-1))
               if Map[k[0]][k[1]-1]==0 :
                  Map[k[0]][k[1]-1]=compteur
               else :
                  stop = True
                  fin =(Map[k[0]][k[1]-1],k[0],k[1]-1)
                  break
            if (k[1]<Y-1) and (Map[k[0]][k[1]+1]!=0.5) and (Map[k[0]][k[1]+1]>=0):
               M.append((k[0],k[1]+1))
               if Map[k[0]][k[1]+1]==0 :
                  Map[k[0]][k[1]+1]=compteur
               else :
                  stop = True
                  fin =(Map[k[0]][k[1]+1],k[0],k[1]+1)
                  break
            if (k[1]>0) and (k[0]>0) and (Map[k[0]-1][k[1]]!=0.5) and (Map[k[0]][k[1]-1]!=0.5) and (Map[k[0]-1][k[1]-1]!=0.5) and (Map[k[0]-1][k[1]-1]>=0):
               M.append((k[0]-1,k[1]-1))
               if Map[k[0]-1][k[1]-1]==0 :
                  Map[k[0]-1][k[1]-1]=compteur   
               else :
                  stop = True
                  fin =(Map[k[0]-1][k[1]-1],k[0]-1,k[1]-1)   
                  break
            if (k[1]<Y-1) and (k[0]>0) and (Map[k[0]-1][k[1]]!=0.5) and (Map[k[0]][k[1]+1]!=0.5) and (Map[k[0]-1][k[1]+1]!=0.5) and (Map[k[0]-1][k[1]+1]>=0):
               M.append((k[0]-1,k[1]+1))
               if Map[k[0]-1][k[1]+1]==0 :
                  Map[k[0]-1][k[1]+1]=compteur
               else :
                  stop = True
                  fin =(Map[k[0]-1][k[1]+1],k[0]-1,k[1]+1)
                  break
            if (k[1]<Y-1) and (k[0]<X-1) and (Map[k[0]+1][k[1]]!=0.5) and (Map[k[0]][k[1]+1]!=0.5) and (Map[k[0]+1][k[1]+1]!=0.5) and (Map[k[0]+1][k[1]+1]>=0):
               M.append((k[0]+1,k[1]+1))   
               if Map[k[0]+1][k[1]+1]==0 :
                  Map[k[0]+1][k[1]+1]=compteur
               else :
                  stop = True
                  fin =(Map[k[0]+1][k[1]+1],k[0]+1,k[1]+1)
                  break
            if (k[1]>0) and (k[0]<Y-1) and (Map[k[0]+1][k[1]]!=0.5) and (Map[k[0]][k[1]-1]!=0.5) and (Map[k[0]+1][k[1]-1]!=0.5) and (Map[k[0]+1][k[1]-1]>=0):
               M.append((k[0]+1,k[1]-1))   
               if Map[k[0]+1][k[1]-1]==0 :
                  Map[k[0]+1][k[1]-1]=compteur   
               else :
                  stop = True
                  fin =(Map[k[0]-1][k[1]+1],k[0]-1,k[1]+1)
                  break
         
      compteur = -compteur
      L2[:] = M[:]

      
      

   #Il faut maintenant remonter pour trouver le chemin le plus court
   
   #On détermine le niveau auquel on s'est arrêté à chaque demi-chemin
   compteur_p = 0
   compteur_n = 0
   
   if (fin[0]<0):
      compteur_p = compteur
      compteur_n = fin[0]
   else:
      compteur_n = -compteur
      compteur_p = fin[0] 
   
   
   #On remonte la partie positive du chemin
   chemin_p = [0]*(compteur_p)
   point = (fin[1],fin[2])  
   Map[depart[0]][depart[1]] = 0
   Map[arrivee[0]][arrivee[1]] = 0
   for k in range(compteur_p-1,-1,-1):
      Map[point[0]][point[1]]=10
      if (Map[point[0]-1][point[1]]==k):
         chemin_p[k]="de" #pour descend
         point = (point[0]-1,point[1])
         continue
      if (Map[point[0]+1][point[1]]==k):
         chemin_p[k]="mo" #pour monte
         point = (point[0]+1,point[1])
         continue
      if (Map[point[0]][point[1]-1]==k):
         chemin_p[k]="dr" #pour droite
         point = (point[0],point[1]-1)
         continue
      if (Map[point[0]][point[1]+1]==k):
         chemin_p[k]="ga" #pour gauche
         point = (point[0],point[1]+1)
         continue
      if (Map[point[0]-1][point[1]-1]==k):
         chemin_p[k]="dedr" #pour descend a droite
         point = (point[0]-1,point[1]-1)
         continue
      if (Map[point[0]+1][point[1]-1]==k):
         chemin_p[k]="modr" #pour monte a droite
         point = (point[0]+1,point[1]-1)
         continue
      if (Map[point[0]-1][point[1]+1]==k):
         chemin_p[k]="dega" #pour descend à gauche
         point = (point[0]-1,point[1]+1)
         continue
      if (Map[point[0]+1][point[1]+1]==k):
         chemin_p[k]="moga" #pour monte a gauche
         point = (point[0]+1,point[1]+1)
         continue
   chemin_n = [0]*(abs(compteur_n))
   point = (fin[1],fin[2])
   for k in range(compteur_n+1,1):
      Map[point[0]][point[1]]=10
      if (Map[point[0]+1][point[1]]==k):
         chemin_n[k-1]="de" #pour descend
         point = (point[0]+1,point[1])
         continue
      if (Map[point[0]-1][point[1]]==k):
         chemin_n[k-1]="mo" #pour monte
         point = (point[0]-1,point[1])
         continue
      if (Map[point[0]][point[1]+1]==k):
         chemin_n[k-1]="dr" #pour droite
         point = (point[0],point[1]+1)
         continue
      if (Map[point[0]][point[1]-1]==k):
         chemin_n[k-1]="ga" #pour gauche
         point = (point[0],point[1]-1)
         continue
      if (Map[point[0]+1][point[1]+1]==k):
         chemin_n[k-1]="dedr" #pour descend a droite
         point = (point[0]+1,point[1]+1)
         continue
      if (Map[point[0]-1][point[1]+1]==k):
         chemin_n[k-1]="modr" #pour monte a droite
         point = (point[0]-1,point[1]+1)
         continue
      if (Map[point[0]+1][point[1]-1]==k):
         chemin_n[k-1]="dega" #pour descend à gauche
         point = (point[0]+1,point[1]-1)
         continue
      if (Map[point[0]-1][point[1]-1]==k):
         chemin_n[k-1]="moga" #pour monte a gauche
         point = (point[0]-1,point[1]-1)
         continue
   chemin = chemin_p+chemin_n
   
   return chemin


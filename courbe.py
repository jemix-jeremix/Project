# -*- coding: utf-8 -*-
"""
Auteur: Jérémy Riporto
Date: 01/02/16
Laboratoire SYMME
"""

import numpy as np
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------

def mafonction(x):  #contrôle+i donne des infos sur la fonction sélectionnée
    """
    Une fonction mathématique
    
    Entrées:
    x : est une variable
    
    Renvoie:
    Le carré de x
    """
    return x**2 
    
#------------------------------------------------------------------------------
    
print "tutu"

#------------------------------------------------------------------------------

#x=[1,2,3] pour créer une liste 
#x=np.array([1,2,3])   va créer une liste "array" grâce à numpy
x = np.linspace(0.,10.,11)
y = mafonction(x)

""" 
- on peut rajouter des  éléments dans la liste:
        x.append("tutu")
- on peut demander d'afficher tous les éléments de la liste sauf l'élément 2:
        x[:2]
"""

#------------------------------------------------------------------------------
#Tracé de la figure
plt.figure("Une figure")
plt.clf() #permet de purger la figure après chaque lancement
plt.plot(x,y)
plt.grid()
plt.xlabel("Temps, $t$ [s]")
plt.ylabel("Amplitude, $a$, [N]")
plt.show()









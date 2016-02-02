# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 09:08:05 2016

@author: jéjé
"""

import numpy as np

#------------------------------------------------------------------------------

class Vector(object):   #permet de créer une classe
  #  coords = np.array([1,2,3])    #coordonnées du vecteur

    def __init__(self,x=0.,y=0.,z=0.):  #permet d'initialiser des valeurs
        self.coords = np.array([x,y,z])
        
    def __repr__(self): #va définir comment sont présentées les données
        c = self.coords
        return"<Vector: ({0},{1},{2})>".format(c[0], c[1], c[2])
    
    def norme(self):    #va déterminer la norme du vecteur
        return (self.coords**2).sum()**.5
        
    def normaliser(self):   #va normaliser la norme du vecteur
        n = self.norme()
        self.coords /= n
        
    def __mul__(self, other):   #on créé un moyen de multiplier un vecteur par un entier
        out = Vector()
        if isinstance(other, Vector):
            out.coords = np.cross(self.coords, other.coords)
        else:
            out.coords = self.coords * other
        return out
        
    __rmul__ = __mul__

#------------------------------------------------------------------------------
        
u = Vector(1,0,0)    #on assigne à u la classe de vecteur avec les coordonnées[1,2,3]
v = Vector(4.,5.,-1.)

#------------------------------------------------------------------------------

print "\n"
print "Multiplication de v par 2:"
print v*2

print "\n"
print "Multiplication de v par u:"
print v*u

print "\n"
print "v est-il un vecteur ?"
print isinstance(v, Vector)

print "\n"
print "2 est-il un vecteur ?"
print isinstance(2, Vector)
print "\n"

print "v*u est-il un vecteur ?"
print isinstance(v*u, Vector)
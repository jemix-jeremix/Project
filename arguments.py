# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 10:15:29 2016

@author: jéjé
"""

def fonction(x, y, z, *args, **kwargs):
    print x, y, z
    print args, kwargs
    
    
fonction(1,2, z=5, truc = 36, machin = 12)

def somme(*args, **kwargs):
    #kwargs correspond aux valeurs déclarées genre "a=..."
    #args correspond aux valeurs déclarées directement "25"
    return sum(args) + sum(kwargs.values())
    
"""
sum(args) va additionner les arguments appelés directement et kwargs va
additionner les valeurs appelées précédées d'un égal
"""
    
print somme(3, 5, 12, x=36)

def fonc(lapin, pomme):
    print lapin, pomme
    
    
fonc(4,5)

dic= {"pomme":"pourrie", "lapin":"oreilles"}

fonc(**dic)
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 14:45:42 2025

@author: Sevde Nur
"""

class Animal: # parent

    def toString(self):
        print("animal")
        
class Monkey(Animal):
    
    def toString(self):
        print("monkey")
        
a1 = Animal()
a1.toString()

m1 = Monkey()
m1.toString() # monkey calls overriding method
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 14:40:06 2025

@author: Sevde Nur
"""

from abc import ABC, abstractmethod

class Animal(ABC): # super class

    @abstractmethod 
    def walk(self): pass

    def run(self): pass

class Bird(Animal): # sub class

    def __init__(self):
        print("bird")
        
    def walk(self):
        print("walk")
        
        
b1 = Bird()
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 14:18:51 2025

@author: Sevde Nur
"""

class Website:
    "parent"
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def loginInfo(self):
        print(self.name +" "+ self.surname )
        
class Website1(Website):
    "child"
    def __init__(self, name, surname, ids):
        Website.__init__(self, name, surname)
        self.ids = ids
        
    def login(self):
        print(self.name +" "+ self.surname +" "+ self.ids)
class Website2(Website):
    
    def __init__(self, name, surname, email):
        Website.__init__(self,name,surname)
        self.email = email

    def login(self):
        print(self.name + " "+ self.surname + " "+self.email)
        
p1 = Website("name", "surname")
p1 = Website1("name", "surname", "123")
p1 = Website2("name", "surname", "email@")        
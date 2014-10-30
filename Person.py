__author__ = 'Андрей'

import pygame

class Person:
    def __init__ (self,
                  coord = (10,10),
                  skin = "default",
                  weapon = ("hammer","rifle"),
                  heals = 10,
                  armor = 0,
                  nationality="NO"):
        self.coord = coord
        self.skin = skin
        #self.ammunition = { "hammer"    : 0,
        #                    "sword"     : 0,
        #                    "gun"       : 0,
        #                    "shotgun"   : 0,
        #                    "mortars"   : 0,
        #                    "plasma"    : 0}
        self.heals = heals
        self.armor = armor
        self.nationality = nationality
        self.doubleJump = True






class Weapon:
    def __init__(self):
        pass
    def shot(self):
        pass
    def draw_weapon(self,x,y):
        pass
    def draw_shot(self):
        pass

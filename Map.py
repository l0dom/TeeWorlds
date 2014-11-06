__author__ = 'Андрей'

from ResMenager import ResManager
import pygame
from pygame import*
from Const import *


class Map:
    def __init__ (self,mapName):
        mapRes = ResManager().getMapRes(mapName)
        self.mapCord=mapRes[0]
        self.imgDict=mapRes[1]
        self.respLst=mapRes[2]

    def start (self,display):
        self.display=display

    def update (self):
        pass

    def draw (self):
        x=y=0 # координаты
        for row in self.mapCord:
            for col in row:
                if col!=" ":
                    pf = pygame.transform.scale(self.imgDict[col],(PLATFORM_WIDTH,PLATFORM_HEIGHT))
                    self.display.blit(pf,(x,y))

                x+=PLATFORM_WIDTH
            y+=PLATFORM_HEIGHT
            x=0







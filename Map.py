__author__ = 'Андрей'

from ResMenager import ResManager
import pygame
from Const import *
from Person import Player
from random import randrange
from Block import Platform


class Map:
    def __init__ (self,mapName):
        mapRes = ResManager().getMapRes(mapName)
        self.mapCord=mapRes[0]
        self.imgDict=mapRes[1]
        self.respLst=mapRes[2]
        self.left=False
        self.right=False
        self.up=False
        self.entities = pygame.sprite.Group() # Все объекты
        self.platforms = [] # то, во что мы будем врезаться или опираться


    def start (self,display):
        self.display=display
        n = self.randResp()
        self.player = Player(n[0]*PLATFORM_WIDTH,n[1]*PLATFORM_HEIGHT)
        self.entities.add(self.player)

    def update (self,dt):
        self.player.update(self.left,self.right,self.up,self.platforms)

    def event(self,event):
        for e in event.get():
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
               self.left = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
               self.right = True

            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
               self.right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
               self.left = False

            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                up = True
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                up = False

    def draw (self):
        x=y=0 # координаты
        for row in self.mapCord:
            for col in row:
                if col == "-":
                    img=pygame.transform.scale(self.imgDict[col],(PLATFORM_WIDTH,PLATFORM_HEIGHT))
                    pf = Platform(x,y,img)
                    self.entities.add(pf)
                    self.platforms.append(pf)
                x+=PLATFORM_WIDTH
            y+=PLATFORM_HEIGHT
            x=0
            self.entities.draw(self.display)

    def randResp (self):
        return self.respLst[randrange(len(self.respLst))]





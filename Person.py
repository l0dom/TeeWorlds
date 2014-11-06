__author__ = 'Андрей'

from pygame import sprite,Surface,transform,Rect
from Const import *
from ResMenager import ResManager

class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0   #скорость перемещения. 0 - стоять на месте
        self.startX = x # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = Surface((PLAYER_WIDTH,PLAYER_HEIGHT))
        self.image = transform.scale(ResManager.get_image("mob.png"),(PLATFORM_WIDTH,PLATFORM_HEIGHT))
        self.rect = Rect(x, y, PLAYER_WIDTH,PLAYER_HEIGHT) # прямоугольный объект

    def update(self,  left, right):
        if left:
            self.xvel = -MOVE_SPEED # Лево = x - n

        if right:
            self.xvel = MOVE_SPEED # Право = x + n

        if not(left or right): # стоим, когда нет указаний идти
            self.xvel = 0

        self.rect.x += self.xvel # переносим свои положение на xvel

    def draw(self, screen): # Выводим себя на экран
        screen.blit(self.image, (self.rect.x,self.rect.y))

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

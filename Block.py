__author__ = 'Андрей'

from Const import *
from pygame import sprite,transform,Surface,Rect

class Platform(sprite.Sprite):
    def __init__(self, x, y, img):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = transform.scale(img,(PLATFORM_WIDTH,PLATFORM_HEIGHT))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

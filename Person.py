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
        self.image = transform.scale(ResManager().get_image("mob.png"),(PLAYER_WIDTH,PLAYER_HEIGHT))
        self.rect = Rect(x, y, PLAYER_WIDTH,PLAYER_HEIGHT) # прямоугольный объект
        self.yvel = 0 # скорость вертикального перемещения
        self.onGround = False

    def update(self,  left, right, up, platforms):
        if left:
            self.xvel = -MOVE_SPEED # Лево = x - n

        if right:
            self.xvel = MOVE_SPEED # Право = x + n

        if not(left or right): # стоим, когда нет указаний идти
            self.xvel = 0

        if up:
           if self.onGround: # прыгаем, только когда можем оттолкнуться от земли
               self.yvel = -JUMP_POWER

        if not self.onGround:
            self.yvel +=  GRAVITY

        self.onGround = False; # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def event (self, event):
        pass

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p): # если есть пересечение платформы с игроком

                if self.xvel > 0:                      # если движется вправо
                    self.rect.right = p.rect.left # то не движется вправо

                if xvel < 0:                      # если движется влево
                    self.rect.left = p.rect.right # то не движется влево

                if yvel > 0:                      # если падает вниз
                    self.rect.bottom = p.rect.top # то не падает вниз
                    self.onGround = True          # и становится на что-то твердое
                    self.yvel = 0                 # и энергия падения пропадает

                if yvel < 0:                      # если движется вверх
                    self.rect.top = p.rect.bottom # то не движется вверх
                    self.yvel = 0                 # и энергия прыжка пропадает


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

__author__ = 'Андрей'

import pygame
import Const

class Scene:
    def __init__(self, next_scene = None):
        self.__next_scene = next_scene

    def loop(self, dt):
        self.__event(pygame.event)
        self._update(dt)
        self._draw(dt)

    def start(self, display, manager):
        self.display = display
        self.manager = manager
        self._start()
        self.__end = False

    # Эту функцию стоит определит в потомке если в
    # сцене нужно что-то создать, например наш логотип.
    def _start(self):
        pass

    # Эта функция которая не должна вызываться вне этого класса,
    # ну и вы конечно поняли зачем нужно __.
    def __event(self, event):
        if len(event.get(pygame.QUIT)) > 0:
            self.__end = True
            self.set_next_scene(None)
            return

        self._event(event)

        # event.get() эквивалентен pygame.event.get()
        # передавая параметр в get мы говорим что именно
        # нас интересует из событий.
        for e in event.get(Const.END_SCENE):
            if e.type == Const.END_SCENE:
                self.__end = True

    # Эту функцию придется переопределить в потомке
    def _draw(self, dt):
        pass

    # и эту тоже
    def _event(self, event):
        pass

    # как и эту.
    def _update(self, dt):
        pass

    def next(self):
        return self.__next_scene

    def is_end(self):
        return self.__end

    def the_end(self):
        pygame.event.post(pygame.event.Event(Const.END_SCENE))

    def set_next_scene(self, scene):
        self.__next_scene = scene

class LoadScene(Scene):
    def _start(self):
        sprite = self.manager.get_image('load_background.png')
        coeficient = self.display.get_rect().w / float(sprite.get_rect().w)
        self.sprite = pygame.transform.scale(sprite, (int(sprite.get_rect().w*coeficient),
                                                      int(sprite.get_rect().h*coeficient)))

    def _event(self, event):
        for e in event.get():
            if e.type == pygame.KEYDOWN:
                self.the_end()
                self.set_next_scene(None)

    def _draw(self, dt):
        self.display.fill((255,255,255))
        self.display.blit(self.sprite,(0, self.display.get_rect().h-self.sprite.get_rect().h))
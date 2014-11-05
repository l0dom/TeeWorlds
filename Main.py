#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Scene
from Game import Game



img={}#stock image


def main():
    # Инициализируем pygame.
    scene = Scene.LoadScene(3000,Scene.MenuScene())
    game = Game(scene=scene)
    game.set_caption(title="TeeWords",icon="icon.png")
    game.game_loop()



if __name__ == '__main__':
    main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Scene
from Game import Game



simg={}#stock image
mimg={}#map image

def main():
    # Инициализируем pygame.
    scene = Scene.LoadScene()
    game = Game(scene=scene)
    game.set_caption(title="TeeWords",icon="icon.png")
    game.game_loop()



if __name__ == '__main__':
    main()
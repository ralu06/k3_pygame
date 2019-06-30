import pygame as pg 
from pygame.locals import *
import sys #libreria que permite acceder al sistema 

FPS = 60

class Game:
    clock = pg.time.Clock() #velocidad de refresh
    
    def __init__(self, width, height):
        self.size = (width, height)
        self.display = pg.display #crear pantalla
        self.screen = self.display.set_mode(self.size)
        self.display.set_caption('Mi juego')

    def start(self): #crear bucle
        while True:
            self.clock.tick(FPS)

            for event in pg.event.get(): #controlar evento
                if event.type == QUIT:
                    pg.quit()  #acabar juego
                    sys.exit() #tirar python

            self.display.flip()

if __name__ == '__main__':
    pg.init()
    game = Game (800, 600)
    game.start() #iniciar juego
import pygame as pg 
from pygame.locals import *
import sys #libreria que permite acceder al sistema 

FPS = 60
'''
class Ball(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((16, 16)) 
        self.rect = self.image.get_rect()  #imagen de un rectangulo

        self.x = x
        self.y = y

        self.color =(255,255,255)


        # iniciar la parte grafica
        self.rect.x = self.x
        self.rect.y = self.y
        self.image.fill(self.color)

        
'''

class Ball(pg.Surface):

    x = 0
    y = 0
    dirx = 1
    diry = 1
    color = (255,255,255)
    velocidad = 5

    def __init__(self, x, y):
        pg.Surface.__init__(self, (16, 16))
        self.fill((color)

    def avanza (self):
            #modifica la posicion de ball
        if x >= 800:
            self.dirx = -self.velocidad
        if x <= 0:
            self.dirx = self.velocidad
        if y >= 600:
            self.diry = -self.velocidad
        if y <= 0:
            self.diry = self.velocidad  
    self.x += self.dirx
    self.y += self.diry


class Game:
    clock = pg.time.Clock() #velocidad de refresh
    VELOCIDAD = 5
    
    def __init__(self, width, height):#crear pantalla
        self.size = (width, height)
        self.display = pg.display 
        self.screen = self.display.set_mode(self.size)
        self.display.set_caption('Mi juego')

        self.ball = Ball()
        self.ball1 = Ball()
        self.ball1.color = (255,0,0)
        self.ball1.x = 392
        self.ball1.y =292

        self.ball = pg.Surface((16, 16)) # bola va a ser una superficie
        self.ball.fill((255, 255, 255))

       

    def start(self): #crear bucle

        

        while True:
            self.clock.tick(FPS)

            for event in pg.event.get(): #controlar evento
                if event.type == QUIT:
                    pg.quit()  #acabar juego
                    sys.exit() #tirar python

            
            self.ball.avanza()
            self.ball1.avanza()

            #pintar los sprites en screen

            self.screen.fill((60, 60 , 60))
            self.screen.blit(self.ball1, (self.ball1.x, self.ball1.y))
            self.screen.blit(self.ball, (self.ball.x, self.ball.y)) #coloca la imagen pequeña

            self.display.flip()

if __name__ == '__main__':
    pg.init()
    game = Game (800, 600)
    game.start() #iniciar juego
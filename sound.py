import pygame

from pygame.locals import *

class sound:
    soundObj = None
    def __init__(self):
        pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
        pygame.mixer.init()      

        self.ataque_hueteolt = pygame.mixer.Sound("./Sonidos/ataque_hueteolt.ogg")
        self.ataque_knight = pygame.mixer.Sound("./Sonidos/ataque_knight.ogg")
        
        self.correr = pygame.mixer.Sound("./Sonidos/correr.ogg")

    def startAtaqueHueteolt(self):

            self.ataque_hueteolt.play(0)
            self.ataque_hueteolt.set_volume(0.03)

    def startAtaqueKnight(self):

            self.ataque_knight.play(0)
            self.ataque_knight.set_volume(0.03)
    
    def startCorrer(self):

            self.correr.play(1)
            
            self.correr.set_volume(0.03)
            
     
    def stopSound(self):
        
            self.ataque_hueteolt.stop()
            self.ataque_knight.stop()
            self.correr.stop()


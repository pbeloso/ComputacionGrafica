import pygame

from pygame.locals import *

class sound:
    soundObj = None
    def __init__(self):
        pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
        pygame.mixer.init()      

        self.ataqueK = pygame.mixer.Sound("./Sonidos/ataque_knight.ogg")
        self.ataqueH = pygame.mixer.Sound("./Sonidos/ataque_hueteolt.ogg")
        self.huirK = pygame.mixer.Sound("./Sonidos/huir_knight.ogg")
        self.huirH = pygame.mixer.Sound("./Sonidos/huir_hueteolt.ogg")
        self.correr = pygame.mixer.Sound("./Sonidos/correr.ogg")
        self.ganador = pygame.mixer.Sound("./Sonidos/ganador.ogg")
        
    def startSound(self):

            self.ganador.play(-1)
            self.ganador.set_volume(0.2)

        
    def stopSound(self, element):
        
            self.ganador.stop()

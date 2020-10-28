
import pygame

class events_obj():
    def __init__(self):
        self.knight = pygame.USEREVENT + 1
        self.hueteotl = pygame.USEREVENT + 2
        

    def setTimeEvents(self):
        pygame.time.set_timer(self.knight, 150)
        pygame.time.set_timer(self.hueteotl, 150)

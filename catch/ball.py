import pygame
from pygame.sprite import Sprite
from random import randint
import catch_func as cf

class Ball(Sprite):
    """A class for a dropping ball"""

    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('redball.png')
        self.rect = self.image.get_rect()

        self.rect.y = 0
        self.rect.x = randint(0, self.settings.screen_width)

        self.y = float(self.rect.y)
        self.speed_force = settings.ball_speed_force
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def check_edges(self, stats):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            cf.lost_life(stats)
            return True
        else:
            return False
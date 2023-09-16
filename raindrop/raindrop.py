import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    def __init__(self, settings, screen):
        """Initialize raindrop"""
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('raindrop.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.x = 50
        self.rect.y = 50

    def blitme(self):
        """Draw raindrop"""
        self.screen.blit(self.image, self.rect)
    
    def check_edges(self):
        """
        Let's see if the top of the raindrop reaches the bottom of the screen
        """
        if self.rect.bottom >= self.screen_rect.bottom:
            return True
        else:
            return False
    


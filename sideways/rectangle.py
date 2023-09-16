import pygame
from pygame.sprite import Sprite

class Rectangle(Sprite):
    """Making rectangle target"""

    def __init__(self, s_settings, screen):
        super().__init__()
        self.screen = screen
        self.s_settings = s_settings
        self.rect = pygame.Rect(0,0, s_settings.rect_width,
            s_settings.rect_height)
        self.screen_rect = screen.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right

        self.y = float(self.rect.y)

        self.color = self.s_settings.rect_color
        self.speed_factor = self.s_settings.rect_speed_factor

    def update(self):
        self.y += (self.s_settings.rect_speed_factor *
                   self.s_settings.rect_direction)
        self.rect.y = self.y

    def blitme(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def check_edges(self):
        if self.rect.bottom >= self.screen_rect.bottom:
            return True
        elif self.rect.top <= 0:
            return True
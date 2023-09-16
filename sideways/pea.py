import pygame
from pygame.sprite import Sprite

class Pea(Sprite):
    """A subclass to manage the peas shot by galaga"""

    def __init__(self, s_settings, screen, galaga):
        """Create a pea object"""
        super().__init__()
        self.screen = screen

        # Create a bullet rect at origin and then set correct position
        self.rect = pygame.Rect(0,0, s_settings.pea_width,
            s_settings.pea_height)
        self.rect.centery = galaga.rect.centery
        self.rect.right = galaga.rect.right

        # Store the pea's as float
        self.x = float(self.rect.x)
        # Do realize that rect.x is not the same as rect.centerx. But we can
        # use either to move the actual pea object. x refers to the left most
        # horizontal value of the object while centerx is the center horizontal
        # value

        # Special details about pea
        self.color = s_settings.pea_color
        self.speed_factor = s_settings.pea_speed_factor

    def update(self):
        """Move bullet to the right"""
        self.x += self.speed_factor
        self.rect.x = self.x
    
    def draw_pea(self):
        """Draw the pea on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
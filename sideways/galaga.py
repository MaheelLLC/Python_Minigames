import pygame

class Galaga():
    """Making Galaga ship"""

    def __init__(self, s_settings, screen):
        """Initialize galaga to left center"""
        self.screen = screen
        self.s_settings = s_settings

        # Load ship image and get its rect.
        self.image = pygame.image.load('images/galaga.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # We need the screen to have a rectangular surface now because of the
        # ship and its desired location

        # Start galaga ship at the left center edge of screen
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left + 10

        # Store galaga's center as a float
        self.center = float(self.rect.centery)

        # Movement flags
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the galaga's position with movement flags"""
        # Update galaga's stored center value
        if self.moving_up and self.rect.top > 1:
            self.center -= self.s_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom - 1:
            self.center += self.s_settings.ship_speed_factor
        
        # Update galaga's location
        self.rect.centery = self.center

    def drawgalaga(self):
        """Draw the ship at current location."""
        self.screen.blit(self.image, self.rect)

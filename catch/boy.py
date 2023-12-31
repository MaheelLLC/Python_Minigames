import pygame

class Boy():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('boy2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.boy_speed_force
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.boy_speed_force
    
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
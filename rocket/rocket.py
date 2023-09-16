import pygame
import sys

class Rocket():
    """Making rocket object"""
    
    def __init__(self, screen):
        """Initialize rocket attributes like starting position"""
        self.screen = screen
        
        # Load rocket image and get its rect
        self.image = pygame.image.load('rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start ship in the center of the screen
        self.rect.center = self.screen_rect.center

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """Update the rocket's position based on the movement flags"""
        if self.moving_right and (self.rect.right + 2) < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and (self.rect.left - 2) > 0:
            self.rect.centerx -= 1
        if self.moving_down and (self.rect.bottom + 2) < \
        self.screen_rect.bottom:
            self.rect.centery += 1
        if self.moving_up and (self.rect.top - 2) > 0:
            self.rect.centery -= 1
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

def check_keydown_events(event, rocket):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_UP:
        rocket.moving_up = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True

def check_keyup_events(event, rocket):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False
    elif event.key == pygame.K_UP:
        rocket.moving_up = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = False

def check_events(rocket):
    """Let's check whether the player pressed or released"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)

def update_screen(setting, screen, rocket):
    """Let's update the screen everytime something goes on"""
    screen.fill(setting.bg_color)
    rocket.blitme()

    pygame.display.flip()
        
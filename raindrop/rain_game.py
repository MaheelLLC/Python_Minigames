import pygame
from pygame.sprite import Group
from settings import Settings
import rain_func as rf

def raining():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Raining")
    raindrops = Group()
    rf.create_rain(settings, screen, raindrops)
    
    while True:
        rf.check_events()
        rf.update_rain(settings, raindrops)
        rf.update_screen(settings, screen, raindrops)

raining()
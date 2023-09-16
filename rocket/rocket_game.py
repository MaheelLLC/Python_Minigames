import pygame

from settings import Settings
import rocket as r

def launch_rocket():
    # Initialize pygame, settings, and screen object
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode(
        (setting.screen_width, setting.screen_height))
    pygame.display.set_caption("Rocket Launcher")

    rocket = r.Rocket(screen)

    while True:
        r.check_events(rocket)
        rocket.update()
        r.update_screen(setting, screen, rocket)

launch_rocket()

    
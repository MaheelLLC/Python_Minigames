import pygame
from pygame.sprite import Group

from settings import Settings
from galaga import Galaga
import galaga_func as gf
from rectangle import Rectangle
from game_stats import GameStats
from button import Button

def run_sideways():
    pygame.init()
    s_settings = Settings()
    screen = pygame.display.set_mode(
        (s_settings.screen_width, s_settings.screen_height))
    pygame.display.set_caption("Sideways")
    
    galaga = Galaga(s_settings, screen)

    peas = Group()

    rectangle = Rectangle(s_settings, screen)

    stats = GameStats(s_settings)

    play_button = Button(screen, "Start it Sucker")
    while True:
        gf.check_events(s_settings, screen, galaga, peas, stats, play_button)
        if stats.game_active:
            galaga.update()
            gf.update_peas(s_settings, screen, stats, peas, rectangle)
            gf.update_rect(s_settings, rectangle)
        gf.update_screen(s_settings, screen, galaga, peas, rectangle, 
                         play_button, stats)

run_sideways()
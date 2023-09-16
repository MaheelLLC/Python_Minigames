import pygame

import catch_func as cf
from settings import Settings
from boy import Boy
from ball import Ball
from game_stats import GameStats

def lets_play_catch():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Let's Play Catch")

    boy = Boy(screen, settings)
    ball = Ball(settings, screen)
    stats = GameStats(settings)
    while True:
        cf.check_events(boy)
        if stats.game_active:
            boy.update()
            cf.update_ball(settings, stats, boy, ball)
        cf.update_screen(settings, screen, boy, ball)

lets_play_catch()
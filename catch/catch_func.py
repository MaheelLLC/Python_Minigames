import pygame
import sys
from random import randint
from time import sleep

def check_keydown_events(event, boy):
    if event.key == pygame.K_a:
        boy.moving_left = True
    elif event.key == pygame.K_d:
        boy.moving_right = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, boy):
    if event.key == pygame.K_a:
        boy.moving_left = False
    elif event.key == pygame.K_d:
        boy.moving_right = False
    
def check_events(boy):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, boy)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, boy)
    
def update_screen(settings, screen, boy, ball):
    screen.fill(settings.bg_color)
    boy.blitme()
    ball.blitme()
    pygame.display.flip()

def update_ball(settings, stats, boy, ball):
    check_ball_edges(settings, stats, boy, ball)
    y = float(ball.rect.y)
    y += settings.ball_speed_force
    ball.rect.y = y

def check_ball_edges(settings, stats, boy, ball):
    if ball.check_edges(stats) or check_collision(boy, ball):
        ball.rect.y = 0
        ball.rect.x = randint(0, settings.screen_width)

def check_collision(boy, ball):
    boy_rect = boy.rect
    ball_rect = ball.rect
    collide = boy_rect.colliderect(ball_rect)
    if collide:
        return True
    
def lost_life(stats):
    if stats.lives_left > 0:
        stats.lives_left -= 1
        sleep(0.5)
    else:
        stats.game_active = False

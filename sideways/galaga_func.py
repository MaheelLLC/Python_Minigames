import sys
import pygame

from pea import Pea
from rectangle import Rectangle

def update_screen(s_settings, screen, galaga, peas, rectangle, play_button, 
                  stats):
    """Take all created objects and update their image on the screen"""
    screen.fill(s_settings.bg_color)
    for pea in peas.sprites():
        pea.draw_pea()
    # Whenever, we update the screen, everything gets deleted and then redrawn
    # Thus, for every frame of the game, we must redraw the peas and galaga
    # to ensure that they stay on the screen
    galaga.drawgalaga()
    rectangle.blitme()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def check_keydown_events(event, galaga):
    """Respond to key presses"""
    if event.key == pygame.K_w:
        galaga.moving_up = True
    elif event.key == pygame.K_s:
        galaga.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, galaga):
    """Respond to key releases"""
    if event.key == pygame.K_w:
        galaga.moving_up = False
    elif event.key == pygame.K_s:
        galaga.moving_down = False

def check_mouse_events(event, s_settings, screen, galaga, peas):
    if event.button == 1:
        fire_pea(s_settings, screen, galaga, peas)
    # Saying event.button equals 1, is just asking the computer whether or not
    # the user clicked their left mouse button

def check_events(s_settings, screen, galaga, peas, stats, play_button):
    """Respond to keypresses"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, galaga)
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, galaga)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if stats.game_active:
                check_mouse_events(event, s_settings, screen, galaga, peas)
            else:
                check_play_button(play_button, stats, peas, s_settings)

def fire_pea(s_settings, screen, galaga, peas):
    if len(peas) < s_settings.peas_allowed:
        new_pea = Pea(s_settings, screen, galaga)
        peas.add(new_pea)

def update_peas(s_settings, screen, stats, peas, rectangle):
    peas.update()
    for pea in peas.copy():
        if pea.rect.x >= s_settings.screen_width + 10:
            peas.remove(pea)
    check_rect_pea_collisions(peas, rectangle, s_settings)
    check_for_life(screen, stats, peas)

def update_rect(s_settings, rectangle):
    check_rect_edges(s_settings, rectangle)
    rectangle.update()

def check_rect_edges(s_settings, rectangle):
    if rectangle.check_edges():
        s_settings.rect_direction *= -1
    
def check_rect_pea_collisions(peas, rectangle, s_settings):
    for pea in peas:
        collision = pygame.sprite.spritecollide(rectangle, peas, False)
        if collision:
            peas.remove(pea)
            s_settings.increase_speed()

# I want to test that if I make the above function return True for 
# every collsion, then what I use it in another new function to speed up
# only after the rectangle gets hit twice, and we can test that it speeds up
# by adding a print statement

def check_for_life(screen, stats, peas):
    screen_rect = screen.get_rect()
    for pea in peas:
        if pea.rect.right == screen_rect.right:
            lost_life(stats)


def lost_life(stats):
    if stats.lives_left > 1:
        stats.lives_left -= 1
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def start_game(s_settings, stats, peas):
    if not stats.game_active:
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        s_settings.initialize_dynamic_settings()
        stats.game_active = True
        peas.empty()

def check_play_button(play_button, stats, peas, s_settings):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        start_game(s_settings, stats, peas)


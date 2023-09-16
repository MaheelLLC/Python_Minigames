import pygame
import sys

from raindrop import Raindrop

def update_screen(settings, screen, raindrops):
    """Update images on the screen and flip to new screens."""
    screen.fill(settings.bg_color)
    raindrops.draw(screen)
    pygame.display.flip()

def check_events():
    """Check to see if user quits"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

def create_raindrop(settings, screen, raindrops, drop_index, row_number):
    raindrop = Raindrop(settings, screen)
    rain_width = raindrop.rect.width
    rain_height = raindrop.rect.height
    rain_x = rain_width + drop_index * (2 * rain_width)
    raindrop.rect.x = rain_x
    rain_y = rain_height + row_number * (2 * rain_height)
    raindrop.rect.y = rain_y
    raindrops.add(raindrop)

def get_raindrops_in_row(settings, rain_width):
    available_space_x = settings.screen_width - (2 * rain_width)
    number_of_raindrops_allowed = int(available_space_x / (2 * rain_width))
    return number_of_raindrops_allowed

def get_number_rows(settings, rain_height):
    available_space_y = settings.screen_height - (2 * rain_height)
    number_of_rows = int(available_space_y / (2 * rain_height))
    return number_of_rows

def create_rain(settings, screen, raindrops):
    raindrop = Raindrop(settings, screen)
    num_drops_per_row = get_raindrops_in_row(settings, raindrop.rect.width)
    num_rows = get_number_rows(settings, raindrop.rect.height)
    for row_number in range(num_rows):
        for drop_index in range(num_drops_per_row):
            create_raindrop(settings, screen, raindrops, drop_index, row_number)

def update_rain(settings, raindrops):
    for raindrop in raindrops:
        check_rain_edges(raindrops)
        y = float(raindrop.rect.y)
        y += settings.rain_speed_factor
        raindrop.rect.y = y

def check_rain_edges(raindrops):
    for raindrop in raindrops.copy():
        if raindrop.check_edges():
            raindrop.rect.y = 0
            # new_raindrop = Raindrop(settings, screen)
            # new_raindrop.rect.x = raindrop.rect.x
            # raindrops.remove(raindrop)
            # respawn_drop(new_raindrop, raindrops)

def respawn_drop(raindrop,raindrops):
    raindrop.rect.y = 0
    raindrops.add(raindrop)
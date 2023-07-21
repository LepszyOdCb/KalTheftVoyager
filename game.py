import pygame
import sys
import time
import hud

from settings import *
from images import *
from character import *
from color import *
from map import *
from car import *
from hud import *
from movement import *

# Inicjalizacja Pygame
pygame.init()

# Główna pętla gry
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Poruszanie postacią lub pojazdem
    keys = pygame.key.get_pressed()
    sprinting = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
    player_in_car, character_x, character_y, car_x, car_y, move_keys_pressed, car_image = movement(keys, player_in_car, character_x, character_y, car_x, car_y, character_speed, car_speed, car_image, car_image_mirrored, car_image2)
    
    # Obliczenie pozycji kamery
    camera_x, camera_y = camera_position(player_in_car, character_x, character_y, car_x, car_y, screen_width, screen_height, map_width, map_height)

    # Ograniczenie poruszania się postaci/pojazdu do granic mapy
    character_x, character_y, car_x, car_y = limit_movement(character_x, character_y, car_x, car_y, map_width, map_height, character_width, character_height, car_width, car_height, player_in_car)
    
    # Aktualizacja sprintu i hp
    stamina, hb, regen_rate, car_speed, character_speed = update_stamina(stamina, sprinting, sprint_cost, max_stamina, regen_rate, pygame.time.get_ticks(), last_regen_time, hb, character_speed, car_speed, player_in_car)
    hp,hb = hphb_limiter(hp, hb, hphblimit)

    # Aktualizacja animacji
    current_image, frame_counter, current_frame = animations(move_keys_pressed, frame_counter, frame_delay, current_frame, animation_frames, player_image)

    # Wyczyszczenie ekranu
    screen.fill((0, 0, 0))

    # Narysowanie mapy
    map_rect = pygame.Rect(camera_x, camera_y, screen_width, screen_height)
    screen.blit(map_image, (0, 0), area=map_rect)

    # Narysowanie pojazdu i postaci
    screen.blit(car_image, (car_x - camera_x, car_y - camera_y))

    if not player_in_car:
        screen.blit(current_image, (character_x - camera_x, character_y - camera_y))
    else:
        screen.blit(current_image, (car_x - camera_x, car_y - camera_y))

    # Narysowanie paska staminy
    stamina_bar_rect = pygame.Rect(stamina_bar_x, stamina_bar_y, stamina / max_stamina * stamina_bar_width, stamina_bar_height)
    pygame.draw.rect(screen, gray, stamina_bar_rect)
    pygame.draw.rect(screen, black, (stamina_bar_x, stamina_bar_y, stamina_bar_width, stamina_bar_height), 1)

    # Rysowanie prostokąta
    pygame.draw.rect(screen, gray, (rectangle_x, rectangle_y, rectangle_width, rectangle_height))
    pygame.draw.rect(screen, black, (rectangle_x, rectangle_y, rectangle_width, rectangle_height), 2)
    screen.blit(text_surface, text_rect)

    # Hud
    hud.update_hud(screen, hp, max_hp, hb, max_hb, map_image, character_x, character_y, car_x, car_y, player_in_car)
    
    # Inicjalizacja
    pygame.display.flip()
    pygame.time.Clock().tick(30)

# Zamknięcie Pygame
pygame.quit()
sys.exit()

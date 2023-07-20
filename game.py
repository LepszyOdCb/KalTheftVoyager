import pygame
import sys
import time

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

car_rect = pygame.Rect(car_x, car_y, car_width, car_height)

# Zmienna dzień
dzien = 1

# Główna pętla gry
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Poruszanie postacią lub pojazdem
    keys = pygame.key.get_pressed()

    player_in_car, character_x, character_y, car_x, car_y, move_keys_pressed, car_image = movement(keys, player_in_car, character_x, character_y, car_x, car_y, character_speed, car_speed, car_image, car_image_mirrored, car_image2)
    
    # Obliczenie pozycji kamery
    if not player_in_car:
        camera_x = character_x - screen_width // 2
        camera_y = character_y - screen_height // 2
    else:
        camera_x = car_x - screen_width // 2
        camera_y = car_y - screen_height // 2

    # Ograniczenie kamery do obszaru mapy
    if camera_x < 0:
        camera_x = 0
    if camera_x > map_width - screen_width:
        camera_x = map_width - screen_width
    if camera_y < 0:
        camera_y = 0
    if camera_y > map_height - screen_height:
        camera_y = map_height - screen_height
        
    # Ograniczenie poruszania się postaci/pojazdu do granic mapy
    if character_x < 0:
        character_x = 0
    if character_x > map_width - character_width:
        character_x = map_width - character_width
    if character_y < 0:
        character_y = 0
    if character_y > map_height - character_height:
        character_y = map_height - character_height
    if car_x < 0:
        car_x = 0
    if car_x > map_width - car_width / 1.5:
        car_x = map_width - car_width / 1.5
    if car_y < 0:
        car_y = 0
    if car_y > map_height - car_height / 1.5:
        car_y = map_height - car_height / 1.5
    # Wyczyszczenie ekranu
    screen.fill((0, 0, 0))

    # Narysowanie mapy
    map_rect = pygame.Rect(camera_x, camera_y, screen_width, screen_height)
    screen.blit(map_image, (0, 0), area=map_rect)

    # Animacja postaci
    if move_keys_pressed:
        frame_counter += 1
        if frame_counter >= frame_delay:
            frame_counter = 0
            current_frame = (current_frame + 1) % len(animation_frames)
        current_image = animation_frames[current_frame]
    else:
        current_image = player_image

    # Sprawdzenie, czy przycisk Shift jest wciśnięty
    sprinting = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]

    # Aktualizacja staminy
    current_time = pygame.time.get_ticks()
    if sprinting:
        if stamina > 0:
            stamina -= sprint_cost
            if stamina < 0:
                stamina = 0
    else:
        if current_time - last_regen_time > regen_time and stamina < max_stamina:
            stamina += regen_rate
            if stamina > max_stamina:
                stamina = max_stamina
            last_regen_time = current_time

    # Zmiana prędkości poruszania się postaci/pojazdu w zależności od sprintu
    if sprinting and stamina > 0 and not player_in_car:
        character_speed = 10
    else:
        character_speed = 5

    if sprinting and stamina > 0 and player_in_car:
        car_speed = 20
    else:
        car_speed = 10

    # Regeneracja staminy
    if not sprinting and stamina < max_stamina:
        stamina += regen_rate
        if stamina > max_stamina:
            stamina = max_stamina

    # Narysowanie pojazdu
    screen.blit(car_image, (car_x - camera_x, car_y - camera_y))

    # Narysowanie postaci
    if not player_in_car:
        screen.blit(current_image, (character_x - camera_x, character_y - camera_y))
    else:
        screen.blit(current_image, (car_x - camera_x, car_y - camera_y))

    # Narysowanie paska staminy
    stamina_bar_rect = pygame.Rect(stamina_bar_x, stamina_bar_y, stamina / max_stamina * stamina_bar_width,
                                   stamina_bar_height)
    pygame.draw.rect(screen, gray, stamina_bar_rect)
    pygame.draw.rect(screen, black,
                     (stamina_bar_x, stamina_bar_y, stamina_bar_width, stamina_bar_height), 1)

    # Rysowanie prostokąta
    pygame.draw.rect(screen, gray, (rectangle_x, rectangle_y, rectangle_width, rectangle_height))
    pygame.draw.rect(screen, black, (rectangle_x, rectangle_y, rectangle_width, rectangle_height), 2)

    screen.blit(text_surface, text_rect)

    # Inicjalizacja
    pygame.display.flip()
    pygame.time.Clock().tick(30)

# Zamknięcie Pygame
pygame.quit()
sys.exit()

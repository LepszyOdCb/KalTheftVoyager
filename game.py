import pygame
import sys
import pygame.time

from settings import *
from images import *
from character import *
from color import *
from map import *
from car import *
from hud import *
from movement import *
from inventory import *

# Inicjalizacja Pygame
pygame.init()
pygame.display.set_icon(logo_image)

# Główna pętla gry
running = True
last_refresh_time = pygame.time.get_ticks() 
while running:
    current_time = pygame.time.get_ticks()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_slots_to_file(slots)
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            inventory_open = not inventory_open
            print(inventory_open)
    # Poruszanie postacią lub pojazdem
    keys = pygame.key.get_pressed()
    sprinting = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
    cursor_pos = pygame.mouse.get_pos()
    player_in_car, character_x, character_y, car_x, car_y, move_keys_pressed, car_image = movement(keys, player_in_car, character_x, character_y, car_x, car_y, character_speed, car_speed, car_image, car_image_mirrored, car_image2)
    
    # Obliczenie pozycji kamery
    camera_x, camera_y = camera_position(player_in_car, character_x, character_y, car_x, car_y, screen_width, screen_height, map_width, map_height)

    # Ograniczenie poruszania się postaci/pojazdu do granic mapy
    character_x, character_y, car_x, car_y = limit_movement(character_x, character_y, car_x, car_y, map_width, map_height, character_width, character_height, car_width, car_height, player_in_car)
    
    # Aktualizacja sprintu i hp
    stamina, hb, regen_rate, car_speed, character_speed = update_stamina(stamina, sprinting, sprint_cost, max_stamina, regen_rate, pygame.time.get_ticks(), last_regen_time, hb, character_speed, car_speed, player_in_car)

    # Wyczyszczenie ekranu
    screen.fill((0, 0, 0))
    
    # Narysowanie mapy
    map_rect = pygame.Rect(camera_x, camera_y, screen_width, screen_height)
    screen.blit(map_image, (0, 0), area=map_rect)

    # Narysowanie pojazdu i postaci
    screen.blit(car_image, (car_x - camera_x, car_y - camera_y))
    
   


    if not player_in_car:
        screen.blit(head,           (character_x - camera_x, character_y - camera_y))
        screen.blit(body,           (character_x - camera_x, character_y - camera_y))
        screen.blit(current_mouth,  (character_x - camera_x, character_y - camera_y))
        screen.blit(current_hair,   (character_x - camera_x, character_y - camera_y))
        screen.blit(current_beard,  (character_x - camera_x, character_y - camera_y))
        screen.blit(current_tshirt, (character_x - camera_x, character_y - camera_y))
        screen.blit(current_arms,   (character_x - camera_x, character_y - camera_y))
        screen.blit(current_legs,   (character_x - camera_x, character_y - camera_y))
        screen.blit(current_feet,   (character_x - camera_x, character_y - camera_y))
    else:
        screen.blit(head,           (car_x - camera_x, car_y - camera_y))
        screen.blit(body,           (car_x - camera_x, car_y - camera_y))
        screen.blit(current_mouth,  (car_x - camera_x, car_y - camera_y))
        screen.blit(current_hair,   (car_x - camera_x, car_y - camera_y))
        screen.blit(current_beard,  (car_x - camera_x, car_y - camera_y))
        screen.blit(current_tshirt, (car_x - camera_x, car_y - camera_y))
        screen.blit(current_arms,   (car_x - camera_x, car_y - camera_y))
        screen.blit(current_legs,   (car_x - camera_x, car_y - camera_y))
        screen.blit(current_feet,   (car_x - camera_x, car_y - camera_y))

    # Narysowanie paska staminy
    stamina_bar_rect = pygame.Rect(stamina_bar_x, stamina_bar_y, stamina / max_stamina * stamina_bar_width, stamina_bar_height)
    pygame.draw.rect(screen, gray, stamina_bar_rect)
    pygame.draw.rect(screen, black, (stamina_bar_x, stamina_bar_y, stamina_bar_width, stamina_bar_height), 1)

    # Rysowanie prostokąta
    pygame.draw.rect(screen, gray, (rectangle_x, rectangle_y, rectangle_width, rectangle_height))
    pygame.draw.rect(screen, black, (rectangle_x, rectangle_y, rectangle_width, rectangle_height), 2)
    screen.blit(text_surface, text_rect)

    # Hud
    draw_minimap(screen, map_image, character_x, character_y, car_x, car_y, player_in_car)
    draw_hp_hb(screen, hp, hb, hp_max, hb_max)

    # Ekwipunek
    draw_inventory(screen, inventory_x, inventory_y, slots, items_images, inventory_open, keys)
    is_cursor_on_slot(inventory_x, inventory_y, inventory_gap, inventory_height, cursor_pos, keys, slots)
    quick_slot_usage(keys, eating_sound, screen, hp, hb, hp_max, hb_max)
    
    
    # Inicjalizacja
    pygame.display.flip()
    pygame.time.Clock().tick(30)

# Zamknięcie Pygame
pygame.quit()
sys.exit()
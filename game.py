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

tick_counter = 0

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  
                selected_slot -= slot_change_amount
                print(selected_slot)
            elif event.button == 5: 
                selected_slot += slot_change_amount
                print(selected_slot)

    # Poruszanie postacią lub pojazdem
    keys = pygame.key.get_pressed()
    sprinting = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
    cursor_pos = pygame.mouse.get_pos()
    player_in_car, character_x, character_y, car_x, car_y, move_keys_pressed, car_image = movement(keys, player_in_car, character_x, character_y, car_x, car_y, character_speed, car_speed, car_image, car_image_mirrored, car_image_2)

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
    draw_character(screen, camera_x, camera_y, character_x, character_y, car_x, car_y, player_in_car, head, body, current_mouth, current_hair, current_beard, current_tshirt, current_arms, current_legs, current_feet)
    tick_counter, current_feet = handle_movement_animation(move_keys_pressed, tick_counter, current_feet, feet)

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
    inventory_draw(screen, inventory_x, inventory_y, slots, items_images, inventory_open, keys)
    inventory_item_use(inventory_x, inventory_y, inventory_gap, inventory_height, cursor_pos, keys, slots, eating_sound, screen, hp, hb, hp_max, hb_max, inventory_open, selected_slot)
    inventory_draw_selected_slot(screen, image_size, selected_slot, inventory_open)
    inventory_to_quick_slot(keys, slots, inventory_open, selected_slot, screen)
    inventory_from_quick_slot(keys, slots, inventory_open, selected_slot, screen)
    #draw_selected_slot_2(screen, image_size, selected_slot, inventory_open)
    #swap_slot(selected_slot, selected_slot_2, inventory_open)
    selected_slot = inventory_slot_limit(selected_slot, inventory_open)
    selected_slot_2 = inventory_slot_limit(selected_slot, inventory_open)
    
    # Inicjalizacja
    pygame.display.flip()
    pygame.time.Clock().tick(30)

# Zamknięcie Pygame
pygame.quit()
sys.exit()
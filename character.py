import pygame

from images import *


# Ustawienia postaci
character_width = 140
character_height = 150
character_x = 9600
character_y = 9830
character_speed = 5

# Ustawienia animacji postaci
animation_frames = [player_moving1_image, player_moving2_image]
current_frame = 0
frame_counter = 0
frame_delay = 5  # Opóźnienie między klatkami animacji

# Ustawienia sprintu
stamina = 2500
max_stamina = 2500
sprint_cost = 20
regen_rate = 1
regen_time = 3000  # 3 sekundy w milisekundach
last_regen_time = pygame.time.get_ticks()

#Ustawienia hudu
hp = 10
max_hp = 10
hb = 10
max_hb = 10

def update_stamina(stamina, sprinting, sprint_cost, max_stamina, regen_rate, current_time, last_regen_time, hb, character_speed, car_speed, player_in_car):
    # Aktualizacja staminy
    if sprinting:
        if stamina > 0:
            stamina -= sprint_cost
            if stamina < 0:
                stamina = 0
                hb += 1
                print(hb)
    else:
        if current_time - last_regen_time > regen_time and stamina < max_stamina:
            stamina += regen_rate
            if stamina > max_stamina:
                stamina = max_stamina
            last_regen_time = current_time
    
    # Regeneracja staminy
    if not sprinting and stamina < max_stamina:
        stamina += regen_rate
        if stamina > max_stamina:
            stamina = max_stamina
    
    # Zmiana prędkości poruszania się postaci/pojazdu w zależności od sprintu
    if sprinting and stamina > 0 and not player_in_car:
        character_speed = 10
    else:
        character_speed = 5

    if sprinting and stamina > 0 and player_in_car:
        car_speed = 20
    else:
        car_speed = 10        
    return stamina, hb, regen_rate, car_speed, character_speed


def animations(move_keys_pressed, frame_counter, frame_delay, current_frame, animation_frames, player_image):
    # Animacja postaci
    if move_keys_pressed:
        frame_counter += 1
        if frame_counter >= frame_delay:
            frame_counter = 0
            current_frame = (current_frame + 1) % len(animation_frames)
        current_image = animation_frames[current_frame]
    else:
        current_image = player_image
    return current_image, frame_counter, current_frame

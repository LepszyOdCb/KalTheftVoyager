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

def update_stamina(stamina, sprinting, sprint_cost, max_stamina, regen_rate, current_time, last_regen_time, hb):
    # Aktualizacja staminy
    if sprinting:
        if stamina > 0:
            stamina -= sprint_cost
            if stamina < 0:
                stamina = 0
                hb -= 1
                print(hb)
    if hb >= 2:
        if current_time - last_regen_time > regen_time and stamina < max_stamina:
            stamina += regen_rate
            if stamina > max_stamina:
                stamina = max_stamina
            last_regen_time = current_time
    if hb <= 2:
        regen_rate = 000.1
    if hb > 2:
        regen_rate = 1

    return stamina, hb, regen_rate

import pygame

from images import *

# Ustawienia postaci
character_width = 200
character_height = 150
character_x = 9600
character_y = 9830
character_speed = 5

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

current_mouth  = mouth["mouth_2"]
current_hair   = hair["hair_1"]
current_beard  = beard["beard_1"]
current_tshirt = tshirts["tshirt_1"]
current_arms   = arms["arms_1a"]
current_legs   = legs["legs_1"]
current_feet   = feet["feet_1"]

#def draw_player(player_in_car, camera_x, camera_y):

import pygame

animations_frequency = 60
ticks_since_last_animations = 0

def movement(keys, player_in_car, character_x, character_y, car_x, car_y, character_speed, car_speed, car_image, car_image_mirrored, car_image_2):
    move_keys_pressed = False

    if not player_in_car:
        if keys[pygame.K_w]:
            character_y -= character_speed
            move_keys_pressed = True

        if keys[pygame.K_s]:
            character_y += character_speed
            move_keys_pressed = True

        if keys[pygame.K_a]:
            character_x -= character_speed
            move_keys_pressed = True

        if keys[pygame.K_d]:
            character_x += character_speed
            move_keys_pressed = True

        if not move_keys_pressed:
            distance_to_car = pygame.math.Vector2(car_x - character_x, car_y - character_y).length()
            if distance_to_car < 150 and keys[pygame.K_f]:
                player_in_car = True
                character_x, character_y = car_x, car_y

    else:
        if keys[pygame.K_w]:
            car_y -= car_speed
            move_keys_pressed = True
        if keys[pygame.K_s]:
            car_y += car_speed
            move_keys_pressed = True
        if keys[pygame.K_a]:
            car_x -= car_speed
            move_keys_pressed = True
            car_image = car_image_mirrored
        if keys[pygame.K_d]:
            car_x += car_speed
            move_keys_pressed = True
            car_image = car_image_2

        if keys[pygame.K_g]:
            player_in_car = False
            character_x, character_y = car_x, car_y
    
    #if move_keys_pressed == True:
    #    ticks_since_last_animations += 1
    #    
    #    if ticks_since_last_animations >= animations_frequency:
    #        ticks_since_last_animations = 0
    #        if 
    #elif move_keys_pressed == False:
    #    current_feet = 
    return player_in_car, character_x, character_y, car_x, car_y, move_keys_pressed, car_image
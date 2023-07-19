import pygame

def movement(keys, character_x, character_y, car_x, car_y, character_speed, car_speed, move_keys_pressed, player_in_car, car_image, car_image_mirrored, car_image2):
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
            car_image = car_image2

    return character_x, character_y, car_x, car_y, move_keys_pressed, car_image

import pygame

def movement(keys, player_in_car, character_x, character_y, car_x, car_y, character_speed, car_speed, car_image, car_image_mirrored, car_image2):
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
            car_image = car_image2

        if keys[pygame.K_g]:
            player_in_car = False
            character_x, character_y = car_x, car_y

    return player_in_car, character_x, character_y, car_x, car_y, move_keys_pressed, car_image

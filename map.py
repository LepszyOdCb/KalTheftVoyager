# Ustawienia mapy
map_height = 10000
map_width = map_height

# Funkcje związane z mapą

def camera_position(player_in_car, character_x, character_y, car_x, car_y, screen_width, screen_height, map_width, map_height):
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

    return camera_x, camera_y

def limit_movement(character_x, character_y, car_x, car_y, map_width, map_height, character_width, character_height, car_width, car_height, player_in_car):
    # Ograniczenie poruszania się postaci/pojazdu do granic mapy
    if not player_in_car:
        if character_x < 0:
            character_x = 0
        if character_x > map_width - character_width:
            character_x = map_width - character_width
        if character_y < 0:
            character_y = 0
        if character_y > map_height - character_height:
            character_y = map_height - character_height
    else:
        if car_x < 0:
            car_x = 0
        if car_x > map_width - car_width / 1.5:
            car_x = map_width - car_width / 1.5
        if car_y < 0:
            car_y = 0
        if car_y > map_height - car_height / 1.5:
            car_y = map_height - car_height / 1.5

    return character_x, character_y, car_x, car_y

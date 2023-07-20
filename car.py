from character import *

# Ustawienia pojazdu
car_width = 250
car_height = 250
car_x = character_x - 300
car_y = character_y
car_speed = 20
car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
distance_to_car = pygame.math.Vector2(car_x - character_x, car_y - character_y).length()

# Zmienne dotyczące gracza w pojeździe
player_in_car = False


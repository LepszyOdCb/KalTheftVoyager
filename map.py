from character import *
from car import *

# Ustawienia mapy
map_height = 10000
map_width = map_height

# Ograniczenie poruszania się postaci/pojazdu do granic mapy
if character_x < 0:
    character_x = 0
if character_x > map_width - character_width:
    character_x = map_width - character_width
if character_y < 0:
    character_y = 0
if character_y > map_height - character_height:
    character_y = map_height - character_height
if car_x < 0:
    car_x = 0
if car_x > map_width - car_width / 1.5:
    car_x = map_width - car_width / 1.5
if car_y < 0:
    car_y = 0
if car_y > map_height - car_height / 1.5:
    car_y = map_height - car_height / 1.5
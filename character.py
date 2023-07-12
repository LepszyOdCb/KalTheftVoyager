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
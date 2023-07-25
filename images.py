import pygame

# Wczytanie grafik
player_image = pygame.image.load("images/player.png").convert_alpha()
player_moving1_image = pygame.image.load("images/player_moving1.png").convert_alpha()
player_moving2_image = pygame.image.load("images/player_moving2.png").convert_alpha()
map_image = pygame.image.load("images/map.png").convert_alpha()
car_image = pygame.image.load("images/car.png").convert_alpha()
car_image2 = pygame.image.load("images/car.png").convert_alpha()
car_image_mirrored = pygame.image.load("images/car_mirrored.png").convert_alpha()
heart_image = pygame.image.load("images/heart.png").convert_alpha()
hunger_image = pygame.image.load("images/hunger.png").convert_alpha()
logo_image = pygame.image.load("images/logo.png").convert()
inventory_slot_image = pygame.image.load("images/inventory_slot.png")
bread_image = pygame.image.load("images/bread.png")

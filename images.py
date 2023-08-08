import pygame

from settings import your_file_directory

# Wczytanie grafik 
player_image = pygame.image.load(f"{your_file_directory}images/player.png").convert_alpha()
player_moving1_image = pygame.image.load(f"{your_file_directory}images/player_moving1.png").convert_alpha()
player_moving2_image = pygame.image.load(f"{your_file_directory}images/player_moving2.png").convert_alpha()
map_image = pygame.image.load(f"{your_file_directory}images/map.png").convert_alpha()
car_image = pygame.image.load(f"{your_file_directory}images/car.png").convert_alpha()
car_image2 = pygame.image.load(f"{your_file_directory}images/car.png").convert_alpha()
car_image_mirrored = pygame.image.load(f"{your_file_directory}images/car_mirrored.png").convert_alpha()
heart_image = pygame.image.load(f"{your_file_directory}images/heart.png").convert_alpha()
heart_empty_image = pygame.image.load(f"{your_file_directory}images/heart_empty.png").convert_alpha()
hunger_image = pygame.image.load(f"{your_file_directory}images/hunger.png").convert_alpha()
hunger_empty_image = pygame.image.load(f"{your_file_directory}images/hunger_empty.png")
logo_image = pygame.image.load(f"{your_file_directory}images/logo.png").convert()

items_images = {
    "bread": pygame.image.load(f"{your_file_directory}images/bread.png"),
    "None": pygame.image.load(f"{your_file_directory}images/none.png"),
    "Logo": pygame.image.load(f"{your_file_directory}images/logo.png")
}

eating_sound = f"{your_file_directory}sound/eating_sound.mp3"
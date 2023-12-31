import pygame

from settings import your_file_directory

# Map
map_image = pygame.image.load(f"{your_file_directory}images/map.png").convert_alpha()

# Car
car_image =          pygame.image.load(f"{your_file_directory}images/bike/car.png").convert_alpha()
car_image_2 =        pygame.image.load(f"{your_file_directory}images/bike/car.png").convert_alpha()
car_image_3 =        pygame.image.load(f"{your_file_directory}images/items/none.png").convert_alpha()
car_image_mirrored = pygame.image.load(f"{your_file_directory}images/bike/car_mirrored.png").convert_alpha()

# Hud
heart_image =        pygame.image.load(f"{your_file_directory}images/hud/heart.png").convert_alpha()
heart_empty_image =  pygame.image.load(f"{your_file_directory}images/hud/heart_empty.png").convert_alpha()
hunger_image =       pygame.image.load(f"{your_file_directory}images/hud/hunger.png").convert_alpha()
hunger_empty_image = pygame.image.load(f"{your_file_directory}images/hud/hunger_empty.png")

# Logo
logo_image = pygame.image.load(f"{your_file_directory}images/logo.png").convert()

# Items
items_images = {
    "bread": pygame.image.load(f"{your_file_directory}images/items/bread.png"),
    "None":  pygame.image.load(f"{your_file_directory}images/items/none.png"),
}

# Sounds
eating_sound = f"{your_file_directory}sound/eating_sound.mp3"
moving_sound = f"{your_file_directory}sound/moving_sound.mp3"
# Player

# Face
head = pygame.image.load(f"{your_file_directory}images/player/face/hitbox_head.png")

mouth = {
    "mouth_1": pygame.image.load(f"{your_file_directory}images/player/face/mouth/mouth_1.png"),
    "mouth_2": pygame.image.load(f"{your_file_directory}images/player/face/mouth/mouth_2.png"),
    "mouth_3": pygame.image.load(f"{your_file_directory}images/player/face/mouth/hitbox_mouth.png")
}

hair = {
    "hair_1": pygame.image.load(f"{your_file_directory}images/player/face/hair/defult_hair.png"),
    "hair_2": pygame.image.load(f"{your_file_directory}images/player/face/hair/hitbox_hair.png"),
}

beard = {
    "beard_1": pygame.image.load(f"{your_file_directory}images/player/face/beard/defult_beard.png"),
}  

# Body
body = pygame.image.load(f"{your_file_directory}images/player/body/hitbox_body.png")

tshirts = {
    "tshirt_1": pygame.image.load(f"{your_file_directory}images/player/body/tshirts/audiquatro/audi_quatro.png"),
    "tshirt_2": pygame.image.load(f"{your_file_directory}images/player/body/tshirts/hitbox_tshirt/hitbox_tshirt.png"),
}

# Arms

arms = {
    "arms_1a": pygame.image.load(f"{your_file_directory}images/player/body/tshirts/audiquatro/audi_quatro_1.png"),
    "arms_1b": pygame.image.load(f"{your_file_directory}images/player/body/tshirts/audiquatro/audi_quatro_2.png"),
    "arms_1c": pygame.image.load(f"{your_file_directory}images/player/body/tshirts/audiquatro/audi_quatro_3.png"),
    "arms_2a": pygame.image.load(f"{your_file_directory}images/player/body/tshirts//hitbox_tshirt/hitbox_tshirt_1.png"),
    "arms_2b": pygame.image.load(f"{your_file_directory}images/player/body/tshirts//hitbox_tshirt/hitbox_tshirt_2.png"),
    "arms_2c": pygame.image.load(f"{your_file_directory}images/player/body/tshirts//hitbox_tshirt/hitbox_tshirt_3.png"),
}

# Legs

legs = {
    "legs_1": pygame.image.load(f"{your_file_directory}images/player/legs/blue_jeans.png"),
    "legs_2": pygame.image.load(f"{your_file_directory}images/player/legs/hitbox_legs.png"),
}

# Feet

feet = {
    "feet_1": pygame.image.load(f"{your_file_directory}images/player/feet/vans/vans.png"),
    "feet_2a": pygame.image.load(f"{your_file_directory}images/player/feet/hitbox/hitbox_shoe_1.png"),
    "feet_2b": pygame.image.load(f"{your_file_directory}images/player/feet/hitbox/hitbox_shoe_2.png"),
    "feet_2c": pygame.image.load(f"{your_file_directory}images/player/feet/hitbox/hitbox_shoe_3.png"),
}
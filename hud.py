import pygame

from settings import *
from color import *
from images import *
from map import *
from character import *

pygame.font.init()

# Ustawienia paska staminy
stamina_bar_width = screen_width - 40
stamina_bar_height = 10
stamina_bar_x = 20
stamina_bar_y = 10
stamina_bar_rect = pygame.Rect(stamina_bar_x, stamina_bar_y, stamina / max_stamina * stamina_bar_width, stamina_bar_height)

# Ustawienia HUD
hud_x = 20
hud_y = screen_height - 60
hud_spacing = 20

# Zmienna dzień
dzien = 1

# Ustawienia prostokąta na dole ekranu
rectangle_width = 200
rectangle_height = 50
rectangle_x = (screen_width - rectangle_width) // 2
rectangle_y = screen_height - rectangle_height - 3

# Rysowanie tekstu w prostokącie
font = pygame.font.SysFont(None, 30)
text = "Dzień: " + str(dzien)
text_surface = font.render(text, True, black)
text_rect = text_surface.get_rect(center=(rectangle_x + rectangle_width // 2, rectangle_y + rectangle_height // 2))

# Funkcja rysująca minimape
def draw_minimap(screen, map_image, player_x, player_y, car_x, car_y, player_in_car):
    minimap_size = 250
    minimap_border = 10  # Increased border size to 15px10
    minimap_x = screen.get_width() - minimap_size - minimap_border - 30
    minimap_y = 40

    # Draw minimap background with wider and taller gray border
    minimap_surface = pygame.Surface((minimap_size + 2 * minimap_border, minimap_size + 2 * minimap_border))
    minimap_surface.fill(gray)
    pygame.draw.rect(minimap_surface, black, minimap_surface.get_rect(), 1)

    # Scale and draw the map image on the minimap
    scaled_map_image = pygame.transform.scale(map_image, (minimap_size, minimap_size))
    minimap_surface.blit(scaled_map_image, (minimap_border, minimap_border))

    # Calculate player and car positions on the minimap
    player_pos_on_minimap = (int(player_x * minimap_size / map_width) + minimap_border,
                             int(player_y * minimap_size / map_height) + minimap_border)
    car_pos_on_minimap = (int(car_x * minimap_size / map_width) + minimap_border,
                          int(car_y * minimap_size / map_height) + minimap_border)

    # Draw player as a red dot on the minimap
    if not player_in_car:
        pygame.draw.circle(minimap_surface, red, player_pos_on_minimap, 4)
    # Draw the car as a blue dot on the minimap
    pygame.draw.circle(minimap_surface, blue, car_pos_on_minimap, 4)

    # Draw the minimap on the main screen
    screen.blit(minimap_surface, (minimap_x, minimap_y))

hp, hb = 10, 9
hp_max, hb_max = 10, 10
hp_hb_size = 64
hp_hb_gap = 4
        
def draw_hp_hb(screen, hp, hb, hp_max, hb_max):
    for i in range (0, hp_max):
        screen.blit(heart_empty_image, (hp_hb_gap + (hp_hb_size + hp_hb_gap)*i, 30))
        for i in range (0, hp):
            screen.blit(heart_image, (hp_hb_gap + (hp_hb_size + hp_hb_gap)*i, 30))
    
    for i in range (0, hb_max):
        screen.blit(hunger_empty_image, (hp_hb_gap + (hp_hb_size + hp_hb_gap)*i, hp_hb_size + hp_hb_size))
    for i in range (0, hb):
        screen.blit(hunger_image, (hp_hb_gap + (hp_hb_size + hp_hb_gap)*i, hp_hb_size + hp_hb_size))

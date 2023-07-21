import pygame

from settings import *
from color import *
from images import *
from map import *

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

# Stałe
HEART_SIZE = (50, 50)
HUNGER_SIZE = (50, 50)
HEART_SPACING = 5
HUNGER_SPACING = 5
HUD_OFFSET_X = 20
HUD_OFFSET_Y = 20

# Funkcja inicjalizująca HUD
def init_hud():
    global heart_image, hunger_image
    heart_image = pygame.transform.scale(heart_image, HEART_SIZE)
    hunger_image = pygame.transform.scale(hunger_image, HUNGER_SIZE)

# Funkcja aktualizująca HUD
def update_hud(screen, hp, max_hp, hb, max_hb, map_image, player_x, player_y, car_x, car_y, player_in_car):
    heart_count = min(hp, max_hp)
    hunger_count = min(hb, max_hb)

    for i in range(max_hp):
        x = HUD_OFFSET_X + i * (HEART_SIZE[0] + HEART_SPACING)
        y = HUD_OFFSET_Y
        if i < heart_count:
            screen.blit(heart_image, (x, y))
        else:
            # Wyświetlenie pustego serca, jeśli HP jest mniejsze niż max_hp
            screen.blit(heart_image, (x, y), (0, 0, 0, 0))

    for i in range(max_hb):
        x = HUD_OFFSET_X + i * (HUNGER_SIZE[0] + HUNGER_SPACING)
        y = HUD_OFFSET_Y + HEART_SIZE[1] + HUD_OFFSET_Y
        if i < hunger_count:
            screen.blit(hunger_image, (x, y))
        else:
            # Wyświetlenie pustego elementu głodu, jeśli HB jest mniejsze niż max_hb
            screen.blit(hunger_image, (x, y), (0, 0, 0, 0))
    draw_minimap(screen, map_image, player_x, player_y, car_x, car_y, player_in_car)

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

hphblimit = 0
def hphb_limiter(hp, hb, hphblimit):
    
    if hb < hphblimit:
        hb += 1
    if hp < 0:
        hp += 1
    return hp, hb
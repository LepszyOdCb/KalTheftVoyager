import pygame

from settings import *
from color import *
from images import *

pygame.font.init()

# Ustawienia paska staminy
stamina_bar_width = screen_width - 40
stamina_bar_height = 10
stamina_bar_x = 20
stamina_bar_y = 10

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
HEART_SIZE = (40, 40)
HUNGER_SIZE = (40, 40)
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
def update_hud(screen, hp, max_hp, hb, max_hb):
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


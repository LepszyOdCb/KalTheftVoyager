import pygame

from settings import *
from color import *

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
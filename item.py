import pygame

from images import *

def use_bread(eating_sound, hb):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(eating_sound)
    sound.play()
    hb += 1
    return print(hb) 

 
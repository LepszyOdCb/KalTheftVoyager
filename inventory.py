import pygame
import csv

from color import *
from settings import *
from images import *

inventory_height = 64
inventory_widht = 64
inventory_x = screen_width / 2 - inventory_widht / 2
inventory_y = screen_width / 4
inventory_gap = 8
inventory_open = True

image_size = 64

slot_vertically = 5
slot_horizontally = slot_vertically
slot_amount = 30

def read_slots_from_file():
    slots = []
    with open("inventory.csv", "r", newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            slots.append(row[1])
    return tuple(slots)

def save_slots_to_file(slots):
    with open("inventory.csv", "w", newline='') as file:
        csv_writer = csv.writer(file)
        for i, slot in enumerate(slots, start=1):
            csv_writer.writerow([f"slot_{i}", slot])

slots = list(read_slots_from_file())

# Read the values of slots from the CSV file
slot_1, slot_2, slot_3, slot_4, slot_5, slot_6, slot_7, slot_8, slot_9, slot_10, slot_11, slot_12, slot_13, slot_14, slot_15, slot_16, slot_17, slot_18, slot_19, slot_20, slot_21, slot_22, slot_23, slot_24, slot_25, slot_26, slot_27, slot_28, slot_29, slot_30 = read_slots_from_file()
        
def draw_inventory(inventory_x, inventory_y, slots, item_image):
    item_images = [None, items_images[slot_1], items_images[slot_2], items_images[slot_3], items_images[slot_4], items_images[slot_5], items_images[slot_6], items_images[slot_7], items_images[slot_9], items_images[slot_9], items_images[slot_10], items_images[slot_11], items_images[slot_12], items_images[slot_13], items_images[slot_14], items_images[slot_15], items_images[slot_16], items_images[slot_17], items_images[slot_18], items_images[slot_19], items_images[slot_20], items_images[slot_21], items_images[slot_22], items_images[slot_23], items_images[slot_24], items_images[slot_25], items_images[slot_26], items_images[slot_27], items_images[slot_28], items_images[slot_29], items_images[slot_30]]
    for col in range(1, slot_amount + 1):
        if col < 6:
            item_image = item_images[col]
            pygame.draw.rect(screen, gray,  (inventory_gap, inventory_y + (inventory_gap + inventory_height) * col, inventory_widht, inventory_height))  
            pygame.draw.rect(screen, black, (inventory_gap, inventory_y + (inventory_gap + inventory_height) * col, inventory_widht, inventory_height), 2)
            screen.blit(item_image,         (inventory_gap, inventory_y + (inventory_gap + inventory_height) * col))
        elif inventory_open == True:
            if col > 5 and col < 11:
                item_image = item_images[col]
                pygame.draw.rect(screen, gray,  (inventory_x + (inventory_gap + inventory_height), inventory_y + (inventory_gap + inventory_height) * (col - 5), inventory_widht, inventory_height))  
                pygame.draw.rect(screen, black, (inventory_x + (inventory_gap + inventory_height), inventory_y + (inventory_gap + inventory_height) * (col - 5), inventory_widht, inventory_height), 2)
                screen.blit(item_image,         (inventory_x + (inventory_gap + inventory_height), inventory_y + (inventory_gap + inventory_height) * (col - 5)))
            elif col > 10 and col < 16:
                item_image = item_images[col]
                pygame.draw.rect(screen, gray,  (inventory_x + (inventory_gap + inventory_height) * 2, inventory_y + (inventory_gap + inventory_height) * (col - 10), inventory_widht, inventory_height))  
                pygame.draw.rect(screen, black, (inventory_x + (inventory_gap + inventory_height) * 2, inventory_y + (inventory_gap + inventory_height) * (col - 10), inventory_widht, inventory_height), 2)
                screen.blit(item_image,         (inventory_x + (inventory_gap + inventory_height) * 2, inventory_y + (inventory_gap + inventory_height) * (col - 10)))
            elif col > 15 and col < 21:
                item_image = item_images[col]
                pygame.draw.rect(screen, gray,  (inventory_x + (inventory_gap + inventory_height) * 3, inventory_y + (inventory_gap + inventory_height) * (col - 15), inventory_widht, inventory_height))  
                pygame.draw.rect(screen, black, (inventory_x + (inventory_gap + inventory_height) * 3, inventory_y + (inventory_gap + inventory_height) * (col - 15), inventory_widht, inventory_height), 2)
                screen.blit(item_image,         (inventory_x + (inventory_gap + inventory_height) * 3, inventory_y + (inventory_gap + inventory_height) * (col - 15)))
            elif col > 20 and col < 26:
                item_image = item_images[col]
                pygame.draw.rect(screen, gray,  (inventory_x + (inventory_gap + inventory_height) * 4, inventory_y + (inventory_gap + inventory_height) * (col - 20), inventory_widht, inventory_height))  
                pygame.draw.rect(screen, black, (inventory_x + (inventory_gap + inventory_height) * 4, inventory_y + (inventory_gap + inventory_height) * (col - 20), inventory_widht, inventory_height), 2)
                screen.blit(item_image,         (inventory_x + (inventory_gap + inventory_height) * 4, inventory_y + (inventory_gap + inventory_height) * (col - 20)))
            elif col > 25 and col < 31:
                item_image = item_images[col]
                pygame.draw.rect(screen, gray,  (inventory_x + (inventory_gap + inventory_height) * 5, inventory_y + (inventory_gap + inventory_height) * (col - 25), inventory_widht, inventory_height))  
                pygame.draw.rect(screen, black, (inventory_x + (inventory_gap + inventory_height) * 5, inventory_y + (inventory_gap + inventory_height) * (col - 25), inventory_widht, inventory_height), 2)
                screen.blit(item_image,         (inventory_x + (inventory_gap + inventory_height) * 5, inventory_y + (inventory_gap + inventory_height) * (col - 25)))

def is_cursor_on_slot_1(inventory_x, inventory_y, inventory_gap, inventory_height, cursor_pos):
    for i in range(1, slot_vertically + 1):
        is_q_pressed = pygame.key.get_pressed()[pygame.K_q]
        if (inventory_gap <= cursor_pos[0] <= (inventory_gap + inventory_widht)) and (inventory_y + (inventory_gap + inventory_height)*i <= cursor_pos[1] <= (inventory_y + (inventory_gap + inventory_height)*i + image_size)) and (is_q_pressed):
            slots[i-1], slots[5] = slots[5], slots[i-1]
            save_slots_to_file(slots)
            return print(i)
        

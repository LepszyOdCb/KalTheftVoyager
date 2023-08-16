import pygame
from pygame.locals import *
import csv

from color import *
from settings import *
from images import *
from item import *
from hud import *

inventory_height = 64
inventory_widht = 64
inventory_gap = 8
inventory_x = screen_width / 2 - (inventory_widht + inventory_gap) * 2.5
inventory_y = screen_width / 4
inventory_open = True

image_size = 64

slot_vertically = 5
slot_horizontally = slot_vertically
slot_amount = 30

slot_change_amount = 1
selected_slot = 0
selected_slot_2 = 0

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

def inventory_draw(screen, inventory_x, inventory_y, slots, items_images, inventory_open, keys):
    item_images = [None] + [items_images[slot] for slot in slots]
    item_image = True  

    for col in range(1, slot_amount + 1):
        if col <= 5:
            item_image = item_images[col]

            slot_x = inventory_gap 
            slot_y = inventory_y + (inventory_gap + inventory_height) * col

            pygame.draw.rect(screen, gray, (slot_x, slot_y, inventory_widht, inventory_height))
            pygame.draw.rect(screen, black, (slot_x, slot_y, inventory_widht, inventory_height), 2)
            
            if item_image:
                screen.blit(item_image, (slot_x, slot_y))
        if inventory_open == True:
            if col <= 10 and col >= 6:
                item_image = item_images[col]

                slot_x = inventory_x + (inventory_gap + inventory_height)*1
                slot_y = inventory_y + (inventory_gap + inventory_height) * (col - 5)

                pygame.draw.rect(screen, gray, (slot_x, slot_y, inventory_widht, inventory_height))
                pygame.draw.rect(screen, black, (slot_x, slot_y, inventory_widht, inventory_height), 2)

                if item_image:
                    screen.blit(item_image, (slot_x, slot_y))
            if col <= 15 and col >= 11:
                    item_image = item_images[col]

                    slot_x = inventory_x + (inventory_gap + inventory_height)*2
                    slot_y = inventory_y + (inventory_gap + inventory_height) * (col - 10)

                    pygame.draw.rect(screen, gray, (slot_x, slot_y, inventory_widht, inventory_height))
                    pygame.draw.rect(screen, black, (slot_x, slot_y, inventory_widht, inventory_height), 2)

                    if item_image:
                        screen.blit(item_image, (slot_x, slot_y))
            if col <= 20 and col >= 16:
                    item_image = item_images[col]

                    slot_x = inventory_x + (inventory_gap + inventory_height)*3
                    slot_y = inventory_y + (inventory_gap + inventory_height) * (col - 15)

                    pygame.draw.rect(screen, gray, (slot_x, slot_y, inventory_widht, inventory_height))
                    pygame.draw.rect(screen, black, (slot_x, slot_y, inventory_widht, inventory_height), 2)

                    if item_image:
                        screen.blit(item_image, (slot_x, slot_y))
            if col <= 25 and col >= 21:
                    item_image = item_images[col]

                    slot_x = inventory_x + (inventory_gap + inventory_height)*4
                    slot_y = inventory_y + (inventory_gap + inventory_height) * (col - 20)

                    pygame.draw.rect(screen, gray, (slot_x, slot_y, inventory_widht, inventory_height))
                    pygame.draw.rect(screen, black, (slot_x, slot_y, inventory_widht, inventory_height), 2)

                    if item_image:
                        screen.blit(item_image, (slot_x, slot_y))
            if col <= 30 and col >= 26:
                    item_image = item_images[col]

                    slot_x = inventory_x + (inventory_gap + inventory_height)*5
                    slot_y = inventory_y + (inventory_gap + inventory_height) * (col - 25)

                    pygame.draw.rect(screen, gray, (slot_x, slot_y, inventory_widht, inventory_height))
                    pygame.draw.rect(screen, black, (slot_x, slot_y, inventory_widht, inventory_height), 2)

                    if item_image:
                        screen.blit(item_image, (slot_x, slot_y))
    return item_image, inventory_open

def inventory_item_use(inventory_x, inventory_y, inventory_gap, inventory_height, cursor_pos, keys, slots, eating_sound, screen, hp, hb, hp_max, hb_max, inventory_open, selected_slot):
    if inventory_open == False:
            left_mouse_button_pressed = pygame.mouse.get_pressed()[0]
            if left_mouse_button_pressed and slots[selected_slot - 1] == "bread":
               use_bread(eating_sound, hb)
               draw_hp_hb(screen, hp, hb, hp_max, hb_max)
               slots[selected_slot - 1] = "None"
               return print(slots[selected_slot])
           
def inventory_draw_selected_slot(screen, image_size, selected_slot, inventory_open):
    for slot in range(1, 6):
        if slot == selected_slot:
            slot_x = inventory_gap 
            slot_y = inventory_y + (inventory_gap + inventory_height) * slot
            pygame.draw.rect(screen, orange, (slot_x, slot_y, image_size, image_size), 4)
    if inventory_open == True:
        for slot in range(6, 11):
            if slot == selected_slot:
                slot_x = inventory_x + (inventory_gap + inventory_height)*1
                slot_y = inventory_y + (inventory_gap + inventory_height)*(slot - 5)
                pygame.draw.rect(screen, orange, (slot_x, slot_y, image_size, image_size), 4)
    if inventory_open == True:
        for slot in range(11, 16):
            if slot == selected_slot:
                slot_x = inventory_x + (inventory_gap + inventory_height)*2
                slot_y = inventory_y + (inventory_gap + inventory_height)*(slot - 10)
                pygame.draw.rect(screen, orange, (slot_x, slot_y, image_size, image_size), 4)
    if inventory_open == True:
      for slot in range(16, 21):
          if slot == selected_slot:
                slot_x = inventory_x + (inventory_gap + inventory_height)*3
                slot_y = inventory_y + (inventory_gap + inventory_height) * (slot - 15)
                pygame.draw.rect(screen, orange, (slot_x, slot_y, image_size, image_size), 4)
    if inventory_open == True:
        for slot in range(21, 26):
            if slot == selected_slot:
                slot_x = inventory_x + (inventory_gap + inventory_height)*4
                slot_y = inventory_y + (inventory_gap + inventory_height) * (slot - 20)
                pygame.draw.rect(screen, orange, (slot_x, slot_y, image_size, image_size), 4)
    if inventory_open == True:
        for slot in range(26, 31):
            if slot == selected_slot:
                slot_x = inventory_x + (inventory_gap + inventory_height)*5
                slot_y = inventory_y + (inventory_gap + inventory_height) * (slot - 25)
                pygame.draw.rect(screen, orange, (slot_x, slot_y, image_size, image_size), 4)

#def draw_selected_slot_2(screen, image_size, selected_slot, inventory_open):
#    if inventory_open == True:
#        for slot in range(6, 11):
#            if slot == selected_slot_2:
#                slot_x = inventory_x + (inventory_gap + inventory_height)*1
#                slot_y = inventory_y + (inventory_gap + inventory_height)*(slot - 5)
#                pygame.draw.rect(screen, blue, (slot_x, slot_y, image_size, image_size), 4)
#    if inventory_open == True:
#        for slot in range(11, 16):
#            if slot == selected_slot_2:
#                slot_x = inventory_x + (inventory_gap + inventory_height)*2
#                slot_y = inventory_y + (inventory_gap + inventory_height)*(slot - 10)
#                pygame.draw.rect(screen, blue, (slot_x, slot_y, image_size, image_size), 4)
#    if inventory_open == True:
#      for slot in range(16, 21):
#          if slot == selected_slot_2:
#                slot_x = inventory_x + (inventory_gap + inventory_height)*3
#                slot_y = inventory_y + (inventory_gap + inventory_height) * (slot - 15)
#                pygame.draw.rect(screen, blue, (slot_x, slot_y, image_size, image_size), 4)
#    if inventory_open == True:
#        for slot in range(21, 26):
#            if slot == selected_slot_2:
#                slot_x = inventory_x + (inventory_gap + inventory_height)*4
#                slot_y = inventory_y + (inventory_gap + inventory_height) * (slot - 20)
#                pygame.draw.rect(screen, blue, (slot_x, slot_y, image_size, image_size), 4)
#    if inventory_open == True:
#        for slot in range(26, 31):
#            if slot == selected_slot_2:
#                slot_x = inventory_x + (inventory_gap + inventory_height)*5
#                slot_y = inventory_y + (inventory_gap + inventory_height) * (slot - 25)
#                pygame.draw.rect(screen, blue, (slot_x, slot_y, image_size, image_size), 4)

def inventory_slot_limit(selected_slot, inventory_open):
    if inventory_open == False:
        if selected_slot <= -1:
            selected_slot = 5
            return selected_slot
        elif selected_slot >= 6:
            selected_slot = 0
            return selected_slot
        else:
            return selected_slot
    if inventory_open == True:
        if selected_slot <= -1:
            selected_slot = 5
            return selected_slot
        elif selected_slot >= 31:
            selected_slot = 0
            return selected_slot
        else:
            return selected_slot
        
    if inventory_open == True:
        if selected_slot_2 <= 5:
            selected_slot_2 = 30
            return selected_slot_2
        elif selected_slot_2 >= 32:
            selected_slot_2 = 5
            return selected_slot_2
        else:
            return selected_slot_2
        
def inventory_to_quick_slot(keys, slots, inventory_open, selected_slot, screen):
    if inventory_open == True:
        for i in range(1, 6):
            if keys[getattr(pygame, f"K_{i}")] and slots[selected_slot-1] != "None":
                if selected_slot >= 6 and selected_slot <= 30:
                    slots[i-1] = slots[selected_slot-1]
                    slots[selected_slot-1] = "None" 
                    return print(slots[selected_slot-1]) and print(slots[i-1])

def inventory_from_quick_slot(keys, slots, inventory_open, selected_slot, screen):
    is_q_pressed = keys[pygame.K_q]  
    if inventory_open and is_q_pressed:
        if 1 <= selected_slot <= 5:  
            if slots[selected_slot - 1] != "None":
                slot_index = 5
                while slot_index <= 30:
                    if slots[slot_index] == "None":
                        slots[slot_index] = slots[selected_slot - 1]
                        slots[selected_slot - 1] = "None"
                        break
                    slot_index += 1
                


    

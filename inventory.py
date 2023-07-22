import pygame
import csv
import os

# Inicjalizacja pygame
pygame.init()

# Stałe dotyczące ekranu
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
CELL_SIZE = 50
NUM_ROWS, NUM_COLS = 4, 5
INVENTORY_SIZE = NUM_ROWS * NUM_COLS
SLOT_PADDING = 5
SLOT_BORDER_SIZE = 2

# Stałe dotyczące kolorów
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Ładowanie obrazka przedmiotu
item_image = pygame.image.load('images/bread.png')

# Tworzenie ekranu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Jebany w dupe ekwipunek')

# Funkcja do rysowania slotu
def draw_slot(x, y, item=None, surface=None):
    target_surface = screen if surface is None else surface
    pygame.draw.rect(target_surface, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(target_surface, BLACK, (x, y, CELL_SIZE, CELL_SIZE), SLOT_BORDER_SIZE)
    if item:
        target_surface.blit(item, (x, y))

# Funkcja do wczytania ekwipunku z pliku CSV
def load_inventory():
    if not os.path.exists('inventory.csv'):
        create_empty_inventory()
    with open('inventory.csv', 'r') as file:
        inventory_reader = csv.reader(file)
        inventory = [int(item) for item in next(inventory_reader)]
    return inventory

# Funkcja do zapisania ekwipunku do pliku CSV
def save_inventory(inventory):
    with open('inventory.csv', 'w', newline='') as file:
        inventory_writer = csv.writer(file)
        inventory_writer.writerow(inventory)

# Funkcja do utworzenia pustego ekwipunku w pliku CSV
def create_empty_inventory():
    empty_inventory = [0] * (INVENTORY_SIZE + 4)
    save_inventory(empty_inventory)

# Funkcja do rysowania ekwipunku
def draw_inventory(inventory):
    for i in range(4):
        draw_slot(10, i * (CELL_SIZE + SLOT_PADDING) + 10, item_image if inventory[i] else None)
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            slot_index = i * NUM_COLS + j + 4
            draw_slot(SCREEN_WIDTH // 2 + j * (CELL_SIZE + SLOT_PADDING),
                      i * (CELL_SIZE + SLOT_PADDING) + 10, item_image if inventory[slot_index] else None)

# Główna pętla gry
def main():
    clock = pygame.time.Clock()
    inventory = load_inventory()
    dragging_item = None
    dragging_from_quickbar = False

    # Dodanie chleba na 16 slocie (indeks 15)
    inventory[15] = 1

    while True:
        screen.fill(GRAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_inventory(inventory)
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    save_inventory(inventory)
                    pygame.quit()
                    return
                elif event.key == pygame.K_q:
                    # Przenoszenie przedmiotu z paska szybkiego wyboru do ekwipunku
                    if dragging_item is not None and 0 <= dragging_item < 4:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        row_index = (mouse_y - 10) // (CELL_SIZE + SLOT_PADDING)
                        slot_index = row_index * NUM_COLS
                        target_index = slot_index + (dragging_item % NUM_COLS) + 4
                        if 4 <= target_index < INVENTORY_SIZE + 4:
                            inventory[dragging_item], inventory[target_index] = inventory[target_index], inventory[dragging_item]
                            dragging_item = None
                elif event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4:
                    # Przenoszenie przedmiotu z ekwipunku do paska szybkiego wyboru
                    if dragging_item is not None and 4 <= dragging_item < INVENTORY_SIZE + 4:
                        quickbar_slot = event.key - pygame.K_1
                        inventory[quickbar_slot] = inventory[dragging_item]
                        inventory[dragging_item] = 0
                        dragging_item = None

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for i in range(4):
                        slot_rect = pygame.Rect(10, i * (CELL_SIZE + SLOT_PADDING) + 10, CELL_SIZE, CELL_SIZE)
                        if slot_rect.collidepoint(mouse_x, mouse_y):
                            dragging_item = i
                            dragging_from_quickbar = True
                            break
                    else:
                        for i in range(NUM_ROWS):
                            for j in range(NUM_COLS):
                                slot_index = i * NUM_COLS + j + 4
                                slot_rect = pygame.Rect(SCREEN_WIDTH // 2 + j * (CELL_SIZE + SLOT_PADDING),
                                                        i * (CELL_SIZE + SLOT_PADDING) + 10, CELL_SIZE, CELL_SIZE)
                                if slot_rect.collidepoint(mouse_x, mouse_y) and inventory[slot_index]:
                                    dragging_item = slot_index
                                    dragging_from_quickbar = False
                                    break
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for i in range(NUM_ROWS):
                        for j in range(NUM_COLS):
                            slot_index = i * NUM_COLS + j + 4
                            slot_rect = pygame.Rect(SCREEN_WIDTH // 2 + j * (CELL_SIZE + SLOT_PADDING),
                                                    i * (CELL_SIZE + SLOT_PADDING) + 10, CELL_SIZE, CELL_SIZE)
                            if slot_rect.collidepoint(mouse_x, mouse_y) and dragging_item:
                                if dragging_from_quickbar:
                                    # Przenoszenie przedmiotu z paska szybkiego wyboru do ekwipunku
                                    target_index = i * NUM_COLS + j
                                    inventory[dragging_item], inventory[target_index] = inventory[target_index], inventory[dragging_item]
                                else:
                                    # Przenoszenie przedmiotu wewnątrz ekwipunku
                                    target_index = slot_index
                                    inventory[dragging_item], inventory[target_index] = inventory[target_index], inventory[dragging_item]
                                dragging_item = None
                                break
                    else:
                        dragging_item = None

        if dragging_item is not None:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Rysowanie przenoszonego przedmiotu na nowej powierzchni
            dragged_item_surface = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
            draw_slot(0, 0, item_image if inventory[dragging_item] else None, dragged_item_surface)
            screen.blit(dragged_item_surface, (mouse_x - CELL_SIZE // 2, mouse_y - CELL_SIZE // 2))

        draw_inventory(inventory)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()

import csv

def load_inventory():
    inventory = []
    try:
        with open('inventory.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                inventory.append(row[0])
    except FileNotFoundError:
        print("Nie znaleziono pliku inventory.csv. Tworzenie nowego ekwipunku...")
    return inventory

# Funkcja zapisująca ekwipunek do pliku inventory.csv
def save_inventory(inventory):
    with open('inventory.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for item in inventory:
            writer.writerow([item])

inventory = load_inventory()
quick_slots = [None] * 5
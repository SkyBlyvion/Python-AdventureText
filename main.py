import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.inventory = []
        self.hp = 100

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item['name']} added to your inventory.")

    def show_inventory(self):
        if self.inventory:
            print("You have the following items in your inventory:")
            for item in self.inventory:
                print(f"- {item['name']}")
        else:
            print("Your inventory is empty.")

    def use_item(self, item_name):
        for item in self.inventory:
            if item['name'] == item_name:
                if item['type'] == 'healing':
                    self.hp += item['effect']
                    print(f"Used {item_name}. Restored {item['effect']} HP.")
                    self.inventory.remove(item)
                    return True
        print("Item not found in inventory.")
        return False

    def check_hp(self):
        print(f"Your HP: {self.hp}")

player = Player()

def welcome_message():
    clear_screen()
    print("Welcome to the Eldritch Estate, built atop the ancient ruins of Aetherius.")
    print("Legend holds that the mansion is filled with powerful artifacts and dark secrets.")
    time.sleep(2)

def choose_path():
    print("\nDo you wish to explore the grand library to your left or the mysterious atrium straight ahead?")
    print("1: Grand Library")
    print("2: Mysterious Atrium")
    return input("> ")

def grand_library():
    clear_screen()
    print("You're surrounded by ancient books. A strange glow catches your eye from a book on Aetherius.")
    print("Options:")
    print("1: Investigate the glow")
    print("2: Search for a book about the mansion's history")
    choice = input("> ")

    if choice == "1":
        player.add_to_inventory({'name': 'Magical Orb', 'type': 'artifact'})
        secret_room()
    elif choice == "2":
        player.add_to_inventory({'name': 'Ancient Tome', 'type': 'lore'})
        print("You've uncovered lore about the mansion's ancient curse and its connection to the underworld.")
        time.sleep(2)
        explore_mansion()

def mysterious_atrium():
    clear_screen()
    print("The atrium is filled with exotic plants and a sealed stone door with runes.")
    print("Options:")
    print("1: Attempt to read the runes")
    print("2: Explore the plants")
    choice = input("> ")

    if choice == "1":
        print("The runes hint at a key to unlock the door, hidden within the mansion.")
        explore_mansion()
    elif choice == "2":
        player.add_to_inventory({'name': 'Potion of Health', 'type': 'healing', 'effect': 20})
        explore_mansion()

def explore_mansion():
    clear_screen()
    print("Exploring the mansion, you encounter a spectral guardian!")
    combat()

def secret_room():
    clear_screen()
    print("A hidden room reveals itself, filled with ancient artifacts.")
    player.add_to_inventory({'name': 'Crystal of Power', 'type': 'artifact'})
    explore_mansion()

def combat():
    print("A spectral guardian appears! Options:")
    print("1: Fight")
    print("2: Use Item")
    print("3: Flee")
    choice = input("> ")

    if choice == "1":
        print("You bravely confront the guardian but suffer injuries.")
        player.hp -= 30
        player.check_hp()
        if player.hp > 0:
            print("Defeated the guardian and found a key to the mysterious atrium door.")
            player.add_to_inventory({'name': 'Atrium Key', 'type': 'key'})
            post_combat_scenario()  # Continue the game after combat
        else:
            print("You have been defeated. Game Over.")
            return
    elif choice == "2":
        player.show_inventory()
        item_name = input("Enter the item you want to use: ")
        if player.use_item(item_name):
            combat()
        else:
            print("You couldn't find that item.")
            combat()
    elif choice == "3":
        print("You fled back to the atrium.")
        mysterious_atrium()

def post_combat_scenario():
    # This function decides what happens next after the guardian combat.
    print("With the Atrium Key in hand, you now have access to the mysterious stone door in the atrium.")
    print("Do you wish to open the door, or explore the mansion further?")
    print("1: Open the door")
    print("2: Explore the mansion")
    choice = input("> ")
    if choice == "1":
        open_atrium_door()
    elif choice == "2":
        explore_mansion()
    else:
        print("Invalid choice.")
        post_combat_scenario()

def open_atrium_door():
    clear_screen()
    print("You use the Atrium Key to open the stone door. A gust of cold air greets you as you step into a hidden garden.")
    # Continue the story from here

def explore_mansion():
    clear_screen()
    print("You decide to explore more of the mansion, uncovering its many secrets.")
    # Provide options for further exploration

def start_game():
    welcome_message()
    path = choose_path()
    if path == "1":
        grand_library()
    elif path == "2":
        mysterious_atrium()
    else:
        print("Invalid choice.")
        start_game()

start_game()

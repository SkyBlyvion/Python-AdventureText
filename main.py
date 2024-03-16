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
    time.sleep(3)

#Main entrance
#You can go to Grand Library, Mysterious Atrium, Underground Catacombs, or Explore Mansion
def main_hall():
    clear_screen()
    print("You're back in the main hall of the mansion. Where would you like to go next?")
    print("1: Grand Library")
    print("2: Mysterious Atrium")
    print("3: Underground Catacombs")
    print("4: Explore Mansion")
    choice = input("> ")

    if choice == "1":
        grand_library()
    elif choice == "2":
        mysterious_atrium()
    elif choice == "3":
        underground_catacombs()
    elif choice == "4":
        explore_mansion()
    else:
        print("Invalid choice.")
        main_hall()

#Second grand library
def main_halle():
    clear_screen()
    print("You're back in the main hall of the mansion. Where would you like to go next?")
    print("1: Mysterious Atrium")
    print("2: Underground Catacombs")
    print("3: Explore Mansion")
    choice = input("> ")

    if choice == "1":
        mysterious_atrium()
    elif choice == "2":
        underground_catacombs()
    elif choice == "3":
        explore_mansion()
    else:
        print("Invalid choice.")
        main_halle()


def next_action():
    clear_screen()
    print("What would you like to do next?")
    print("1: Return to the mansion's main hall to choose another path")
    print("2: Check your inventory")
    print("3: Rest and regain some health")
    choice = input("> ")

    if choice == "1":
        main_hall()
    elif choice == "2":
        player.show_inventory()
        input("Press enter to continue...")
        next_action() 
    elif choice == "3":
        player.hp = min(100, player.hp + 20)
        print(f"You rested and regained some health. Current HP: {player.hp}")
        input("Press enter to continue...")
        next_action()
    else:
        print("Invalid choice. Please choose a valid action.")
        next_action()

def grand_library():
    clear_screen()
    print("You're surrounded by ancient books. A strange glow catches your eye from a book on Aetherius.")
    print("Options:")
    print("1: Investigate the glow")
    print("2: Search for a book about the mansion's history")
    choice = input("> ")

    if choice == "1":
        player.add_to_inventory({'name': 'Magical Orb', 'type': 'artifact'})
        print("You've uncovered a new artifact, the Magical Orb")
        print("As you carefully take the artifact, the wall before you begins to open, as if by magic. You uncovered a secret room")
        input("Press Enter to continue...")
        secret_room()
    elif choice == "2":
        player.add_to_inventory({'name': 'Ancient Tome', 'type': 'lore'})
        print("You've uncovered lore about the mansion's ancient curse and its connection to the underworld.")
        print("As you read the ancient tome, you feel a sense of peace and calm. You found a note stamped with the phrase 'The door '")
        print("you decide to go back to the grand library")
        input("Press Enter to continue...")
        grand_librar()

def grand_librar():
    clear_screen()
    print("You're back in the grand library.")
    print("1: Investigate the glow")
    choice = input("> ")

    if choice == "1":
        player.add_to_inventory({'name': 'Magical Orb', 'type': 'artifact'})
        print("You've uncovered a new artifact, the Magical Orb")
        print("As you carefully take the artifact, the wall before you begins to open, as if by magic. You uncovered a secret room")
        input("Press Enter to continue...")
        secret_room()
    else:
        print("Invalid choice. Please choose a valid action.")
        grand_librar()
        


def mysterious_atrium():
    clear_screen()
    print("The atrium is filled with exotic plants and a sealed stone door with runes.")
    print("Options:")
    print("1: Attempt to read the runes")
    print("2: Explore the plants")
    choice = input("> ")

    if choice == "1":
        print("The runes hint at a key to unlock the door, hidden within the mansion.")
        time.sleep(2)
        next_action()#TODO: modifier le next_action
    elif choice == "2":
        player.add_to_inventory({'name': 'Potion of Health', 'type': 'healing', 'effect': 20})
        print("You find a health potion")
        time.sleep(2)
        next_action()#TODO: modifier le next_action

def explore_mansion():
    clear_screen()
    print("Exploring the mansion, you encounter a spectral guardian!")
    combat()

def secret_room():
    clear_screen()
    print("A hidden room reveals itself, filled with an ancient artifacts.")
    player.add_to_inventory({'name': 'Crystal of Power', 'type': 'artifact'})
    print("You've uncovered a new artifact, the Crystal of Power.")
    print("Upon taking the artifact, unaware of the events that unfolded, you find yourself back in the main hall.")
    input("Press Enter to continue...")
    main_hall()


def hidden_garden(): # post combat
    clear_screen()
    print("The hidden garden is lush and overgrown, with an aura of magic. In the center lies a pond that glimmers with magical energy.")
    print("Options:")
    print("1: Investigate the pond")
    print("2: Explore the surrounding flora")
    choice = input("> ")

    if choice == "1":
        print("The pond's water has healing properties. You feel rejuvenated.")
        player.hp = min(100, player.hp + 30)
        player.check_hp()
    elif choice == "2":
        print("Among the exotic plants, you find a rare herb.")
        player.add_to_inventory({'name': 'Rare Herb', 'type': 'healing', 'effect': 50})
    input("Press enter to continue...")
    next_action()#TODO: modifier le next_action

def underground_catacombs(): 
    clear_screen()
    print("You discover a hidden entrance to the catacombs beneath the mansion. Shadows dance along the walls.")
    print("Options:")
    print("1: Delve deeper into the catacombs")
    print("2: Search for inscriptions or artifacts")
    choice = input("> ")

    if choice == "1":
        print("You encounter ancient guardians. Prepare for combat.")
        combat()
    elif choice == "2":
        print("You find an ancient inscription that reveals a secret passage.")
        secret_passage()

def mystical_observatory():
    clear_screen()
    print("The observatory is filled with astronomical instruments and ancient tomes on astrology.")
    print("Options:")
    print("1: Study the stars for guidance")
    print("2: Search for the key hint by the book in the grand library")
    choice = input("> ")

    if choice == "1":
        print("You decipher an astral alignment that points to a hidden artifact within the mansion.")
        print("You go back to the mystical observatory and continue exploring.")
        mystical_observatory()
    elif choice == "2":
        print("A hidden compartment in the wall reveals the key to the .")
        player.add_to_inventory({'name': 'Atrium Key', 'type': 'key'})
    next_action()  # Ensures continuity after exploring the observatory #TODO: modifier le next_action
        
def secret_passage():
    clear_screen()
    print("The ancient inscription leads you to a secret passage hidden behind a movable wall panel.")
    print("As you traverse the dimly lit corridor, you realize it's leading you deeper into the heart of the mansion.")
    print("The passage ends at a heavy door carved with symbols that resonate with magical energy.")
    print("As you remember reading in the grand library, that door could unravel the secrets of the Aetherius.")
    print("Options:")
    print("1: Open the door with the Atrium Key found in the mystical observatory")
    print("2: Inspect the symbols before proceeding")

    choice = input("> ")

    if choice == "1":
        if any(item['name'] == 'Atrium Key' for item in player.inventory):  # Assuming player.inventory is a list of items
            mysterious_chamber()
        else:
            print("The door is locked. You need the Atrium Key from the mystical observatory to open it.")
    elif choice == "2":
        print("The symbols tell the tale of the Aetherius, an ancient society that mastered the elemental magics.")
        print("Realizing the significance of this place, you decide to proceed with caution.")
        input("Press Enter to continue...")  # Added to give players a moment before proceeding
        mysterious_chamber()
    else:
        print("Invalid choice. Please choose to 'open the door cautiously' or 'inspect the symbols before proceeding'.")
        secret_passage()

def mysterious_chamber():
    clear_screen()
    print("The door creaks open to reveal a chamber, untouched by time. In the center, a pedestal holds an ancient artifact.")
    print("This must be the Heart of Aetherius, the source of the mansion's boundless magical energy.")
    print("Options:")
    print("1: Approach the artifact cautiously")
    print("2: Examine the room for traps or hidden dangers")

    choice = input("> ")

    if choice == "1":
        approach_artifact()
    elif choice == "2":
        print("Your caution pays off as you notice subtle magical runes on the floor, likely a protective measure.")
        print("Carefully navigating around them, you make your way to the artifact.")
        approach_artifact()
    else:
        print("Invalid choice. Please choose to 'approach the artifact cautiously' or 'examine the room for traps or hidden dangers'.")
        mysterious_chamber()

def approach_artifact():
    clear_screen()
    print("As you touch the artifact, a surge of energy flows through you. Visions of Aetherius fill your mind, revealing secrets long forgotten.")
    print("You now hold the power to shape the future of the mansion and its legacy. What will you do with this newfound power?")
    print("Congratulations! You've reached the end of this adventure. Will you safeguard the mansion's secrets, or seek to uncover more?")
    # This is the end of the game. Player has completed the main adventure.

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
            print("Defeated the guardian. You continue exploring the mansion.")
            
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
    clear_screen()
    print("With the spectral guardian defeated, the mansion's secrets lie before you.")
    print("Where do you wish to explore next?")
    print("1: The Underground Catacombs")
    print("2: The Mystical Observatory")
    choice = input("> ")

    if choice == "1":
        underground_catacombs()
    elif choice == "2":
        mystical_observatory()
    elif choice == "3":
        main_hall()
    else:
        print("Invalid choice. Please select a valid option.")
        post_combat_scenario()

def start_game():
    welcome_message()
    main_hall()

start_game()

import random
from typing import Tuple, List, Dict, Optional
from dataclasses import dataclass
from enum import Enum

# Dungeon elements
WALL = "█"
FLOOR = "·"
PLAYER = "P" 
MONSTER = "M"
TREASURE = "T"
EXIT = "E"

class ItemType(Enum):
    WEAPON = "Weapon"
    ARMOR = "Armor"
    CONSUMABLE = "Consumable"

@dataclass
class Item:
    name: str
    item_type: ItemType
    attack_bonus: int = 0
    defense_bonus: int = 0
    hp_bonus: int = 0
    mana_bonus: int = 0
    heal_amount: int = 0
    
class PlayerClass(Enum):
    WARRIOR = "Warrior"
    MAGE = "Mage" 
    ROGUE = "Rogue"

@dataclass
class Monster:
    hp: int
    attack: int
    defense: int
    level: int = 1
    hit_chance: float = 0.8
    exp_value: int = 50  # Base exp value
    
    def drop_item(self) -> Optional[Item]:
        """Generate random item drop based on monster level"""
        if random.random() < 0.3:  # 30% drop chance
            if self.level >= 10:
                dropped_item = random.choice(ITEM_DROPS["rare"])
                print(f"\nThe monster dropped a rare item: {dropped_item.name}!")
                return dropped_item
            elif self.level >= 5:
                dropped_item = random.choice(ITEM_DROPS["uncommon"])
                print(f"\nThe monster dropped an uncommon item: {dropped_item.name}!")
                return dropped_item
            dropped_item = random.choice(ITEM_DROPS["common"])
            print(f"\nThe monster dropped a common item: {dropped_item.name}!")
            return dropped_item
        return None

@dataclass
class Player:
    player_class: PlayerClass
    hp: int = 100
    max_hp: int = 100
    attack: int = 10
    defense: int = 5
    mana: int = 100
    max_mana: int = 100
    inventory: Dict[str, int] = None
    equipment: Dict[str, Item] = None
    escape_attempts: int = 0
    damage_dealt: int = 0  # Track damage dealt for stats
    damage_taken: int = 0  # Track damage taken for stats
    level: int = 1
    exp: int = 0
    exp_to_next_level: int = 100
    
    def __post_init__(self):
        if self.inventory is None:
            self.inventory = {"health_potion": 3}
        if self.equipment is None:
            self.equipment = {
                "weapon": None,
                "armor": None
            }
            
        # Set class-specific stats
        if self.player_class == PlayerClass.WARRIOR:
            self.max_hp = 150
            self.hp = 150
            self.attack = 15
            self.defense = 8
            self.max_mana = 50
            self.mana = 50
        elif self.player_class == PlayerClass.MAGE:
            self.max_hp = 80
            self.hp = 80
            self.attack = 8
            self.defense = 3
            self.max_mana = 150
            self.mana = 150
        elif self.player_class == PlayerClass.ROGUE:
            self.max_hp = 100
            self.hp = 100
            self.attack = 12
            self.defense = 4
            self.max_mana = 80
            self.mana = 80

    def get_total_stats(self):
        """Calculate total stats including equipment bonuses"""
        total_attack = self.attack
        total_defense = self.defense
        total_max_hp = self.max_hp
        total_max_mana = self.max_mana

        for item in self.equipment.values():
            if item:
                total_attack += item.attack_bonus
                total_defense += item.defense_bonus
                total_max_hp += item.hp_bonus
                total_max_mana += item.mana_bonus

        return total_attack, total_defense, total_max_hp, total_max_mana

    def equip_item(self, item: Item) -> str:
        """Equip an item and return message about what happened"""
        if item.item_type == ItemType.WEAPON:
            old_item = self.equipment["weapon"]
            self.equipment["weapon"] = item
            return f"Equipped {item.name}" + (f" (Replaced {old_item.name})" if old_item else "")
        elif item.item_type == ItemType.ARMOR:
            old_item = self.equipment["armor"]
            self.equipment["armor"] = item
            return f"Equipped {item.name}" + (f" (Replaced {old_item.name})" if old_item else "")
        return "Cannot equip this item type"

    def gain_exp(self, exp_amount: int):
        """Add experience points and level up if threshold reached"""
        self.exp += exp_amount
        while self.exp >= self.exp_to_next_level:
            self.level_up()

    def level_up(self):
        """Increase player level and stats"""
        self.level += 1
        self.exp -= self.exp_to_next_level
        self.exp_to_next_level = int(self.exp_to_next_level * 1.5)

        # Increase stats based on class
        if self.player_class == PlayerClass.WARRIOR:
            self.max_hp += 20
            self.attack += 3
            self.defense += 2
            self.max_mana += 5
        elif self.player_class == PlayerClass.MAGE:
            self.max_hp += 10
            self.attack += 2
            self.defense += 1
            self.max_mana += 20
        elif self.player_class == PlayerClass.ROGUE:
            self.max_hp += 15
            self.attack += 2
            self.defense += 1
            self.max_mana += 10

        # Restore HP and mana on level up
        self.hp = self.max_hp
        self.mana = self.max_mana
        print(f"\nLevel Up! You are now level {self.level}!")
        attack, defense, max_hp, max_mana = self.get_total_stats()
        print(f"Total Stats (with equipment):")
        print(f"Max HP: {max_hp}, Attack: {attack}, Defense: {defense}, Max Mana: {max_mana}")
            
    def use_potion(self):
        """Use health potion to heal 50% of max HP"""
        if self.inventory.get("health_potion", 0) > 0:
            heal_amount = int(self.max_hp * 0.5)
            self.hp = min(self.max_hp, self.hp + heal_amount)
            self.inventory["health_potion"] -= 1
            return True
        return False
        
    def try_escape(self) -> bool:
        """Attempt to escape combat with increasing probability"""
        self.escape_attempts += 1
        base_chance = random.random() * 0.5  # 0-50% base chance
        bonus = 0.15 * self.escape_attempts  # +15% per attempt
        # Rogues have higher escape chance
        if self.player_class == PlayerClass.ROGUE:
            bonus += 0.2
        return (base_chance + bonus) >= 0.5

    def special_attack(self, monster) -> Tuple[int, str]:
        """Execute class-specific special attack if enough mana"""
        mana_cost = 30
        
        if self.mana < mana_cost:
            return 0, "Not enough mana!"
            
        self.mana -= mana_cost
        attack, _, _, _ = self.get_total_stats()
        
        if self.player_class == PlayerClass.WARRIOR:
            # Warrior's Mighty Strike - high damage
            damage = int(attack * 2.5)
            return damage, "Mighty Strike!"
            
        elif self.player_class == PlayerClass.MAGE:
            # Mage's Fireball - guaranteed hit with magic damage
            damage = int(attack * 3)
            return damage, "Fireball!"
            
        elif self.player_class == PlayerClass.ROGUE:
            # Rogue's Backstab - chance for critical
            if random.random() < 0.6:  # 60% crit chance
                damage = int(attack * 3)
                return damage, "Critical Backstab!"
            return int(attack * 1.5), "Backstab!"

    def show_inventory(self):
        """Display inventory and equipment"""
        print("\n=== INVENTORY ===")
        print("Consumables:")
        for item, count in self.inventory.items():
            print(f"- {item}: {count}")
            
        print("\nEquipment:")
        for slot, item in self.equipment.items():
            if item:
                print(f"- {slot.capitalize()}: {item.name}")
                print(f"  Bonuses: ", end="")
                bonuses = []
                if item.attack_bonus: bonuses.append(f"Attack +{item.attack_bonus}")
                if item.defense_bonus: bonuses.append(f"Defense +{item.defense_bonus}")
                if item.hp_bonus: bonuses.append(f"HP +{item.hp_bonus}")
                if item.mana_bonus: bonuses.append(f"Mana +{item.mana_bonus}")
                print(", ".join(bonuses))
            else:
                print(f"- {slot.capitalize()}: Empty")

# Define possible item drops
ITEM_DROPS = {
    "common": [
        Item("Rusty Sword", ItemType.WEAPON, attack_bonus=2),
        Item("Leather Armor", ItemType.ARMOR, defense_bonus=2),
        Item("Health Potion", ItemType.CONSUMABLE, heal_amount=50)
    ],
    "uncommon": [
        Item("Steel Sword", ItemType.WEAPON, attack_bonus=5),
        Item("Chain Mail", ItemType.ARMOR, defense_bonus=5, hp_bonus=20),
        Item("Mana Crystal", ItemType.CONSUMABLE, mana_bonus=50)
    ],
    "rare": [
        Item("Enchanted Blade", ItemType.WEAPON, attack_bonus=8, mana_bonus=20),
        Item("Plate Armor", ItemType.ARMOR, defense_bonus=8, hp_bonus=50),
        Item("Greater Health Potion", ItemType.CONSUMABLE, heal_amount=100)
    ]
}

def create_maze(width: int, height: int) -> List[List[str]]:
    """Creates a maze using a recursive backtracking algorithm"""
    # Initialize maze with walls
    maze = [[WALL for _ in range(width)] for _ in range(height)]
    
    def carve_path(x: int, y: int):
        maze[y][x] = FLOOR
        
        # Define possible directions (right, down, left, up)
        directions = [(2,0), (0,2), (-2,0), (0,-2)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < width and 0 <= new_y < height and 
                maze[new_y][new_x] == WALL):
                # Carve the wall between current and new position
                maze[y + dy//2][x + dx//2] = FLOOR
                carve_path(new_x, new_y)
    
    # Start from top-left corner
    carve_path(1, 1)
    return maze

def create_dungeon(width: int, height: int, difficulty: int = 1) -> List[List[str]]:
    """Creates a maze-like dungeon with monsters and treasures."""
    # Make sure dimensions are odd
    width = width if width % 2 == 1 else width + 1
    height = height if height % 2 == 1 else height + 1
    
    # Create base maze
    dungeon = create_maze(width, height)
    
    # Add monsters and treasures along the paths
    monster_chance = 0.08 * difficulty
    treasure_chance = 0.12 / difficulty
    
    for y in range(height):
        for x in range(width):
            if dungeon[y][x] == FLOOR:
                chance = random.random()
                if chance < monster_chance:
                    dungeon[y][x] = MONSTER
                elif chance < monster_chance + treasure_chance:
                    dungeon[y][x] = TREASURE
    
    # Clear starting position
    dungeon[1][1] = FLOOR
    
    # Place exit at the furthest reachable point from start
    max_dist = 0
    exit_pos = (1, 1)
    
    for y in range(height):
        for x in range(width):
            if dungeon[y][x] == FLOOR:
                dist = abs(x - 1) + abs(y - 1)  # Manhattan distance from start
                if dist > max_dist:
                    max_dist = dist
                    exit_pos = (x, y)
    
    dungeon[exit_pos[1]][exit_pos[0]] = EXIT
    
    return dungeon

def print_dungeon(dungeon: List[List[str]], player_pos: Tuple[int, int], player: Player) -> None:
    """Prints the current state of the dungeon and player stats."""
    # Print dungeon
    for y in range(len(dungeon)):
        for x in range(len(dungeon[0])):
            if (x, y) == player_pos:
                print(PLAYER, end=' ')
            else:
                print(dungeon[y][x], end=' ')
        print()
        
    # Print player stats
    print(f"\nPlayer Stats ({player.player_class.value}):")
    print(f"Level: {player.level} (EXP: {player.exp}/{player.exp_to_next_level})")
    print(f"HP: {player.hp}/{player.max_hp}")
    print(f"Mana: {player.mana}/{player.max_mana}")
    print(f"Attack: {player.attack}")
    print(f"Defense: {player.defense}")
    print("\nInventory:")
    for item, count in player.inventory.items():
        print(f"{item}: {count}")

def combat(player: Player, difficulty: int) -> bool:
    """Handles combat between player and monster. Returns True if player wins."""
    monster = Monster(
        hp=30 * difficulty,
        attack=5 * difficulty,
        defense=2 * difficulty,
        level=difficulty,
        exp_value=50 * difficulty  # Scale exp with difficulty
    )
    
    print(f"\nA level {monster.level} monster appears!")
    
    # Determine who goes first based on attack values
    total_attack = player.attack + monster.attack
    initiative_roll = random.randint(1, total_attack)
    monster_starts = initiative_roll > player.attack
    
    if monster_starts:
        print("The monster attacks first!")
    else:
        print("You get the first strike!")
    
    player.escape_attempts = 0  # Reset escape counter
    
    while True:
        if not monster_starts:
            # Player turn
            print(f"\nYour HP: {player.hp}/{player.max_hp} | Mana: {player.mana}/{player.max_mana}")
            print(f"Monster HP: {monster.hp}")
            action = input("What do you want to do? [a]ttack, [s]pecial attack, use [p]otion, [f]lee, or view [i]nventory? ").lower()
            
            if action == 'i':
                player.show_inventory()
                continue
                
            if action == 'a':
                if random.random() < 0.8:  # 80% hit chance
                    damage = max(1, player.attack - monster.defense)
                    # Critical hit system
                    if random.random() < 0.1:  # 10% crit chance
                        damage *= 2
                        print("Critical hit!")
                    monster.hp -= damage
                    player.damage_dealt += damage  # Track damage dealt
                    print(f"You deal {damage} damage!")
                else:
                    print("Your attack missed!")
                    
            elif action == 's':
                damage, message = player.special_attack(monster)
                if damage > 0:
                    monster.hp -= damage
                    player.damage_dealt += damage
                    print(f"{message} You deal {damage} damage!")
                else:
                    print(message)
                    continue
                
            elif action == 'p':
                if player.use_potion():
                    print(f"You used a health potion! HP restored to {player.hp}")
                else:
                    print("No health potions left!")
                    continue
                    
            elif action == 'f':
                if player.try_escape():
                    print("You successfully fled from combat!")
                    return True
                print("Couldn't escape!")
            
            if monster.hp <= 0:
                exp_gained = monster.exp_value
                player.gain_exp(exp_gained)
                print(f"You defeated the monster and gained {exp_gained} experience!")
                dropped_item = monster.drop_item()
                if dropped_item:
                    if dropped_item.item_type == ItemType.CONSUMABLE:
                        if dropped_item.name == "Health Potion":
                            player.inventory["health_potion"] = player.inventory.get("health_potion", 0) + 1
                    else:
                        print(player.equip_item(dropped_item))
                return True
            
                    
        # Monster turn
        if random.random() < monster.hit_chance:
            damage = max(1, monster.attack - player.defense)
            player.hp -= damage
            player.damage_taken += damage  # Track damage taken
            print(f"Monster deals {damage} damage!")
        else:
            print("Monster's attack missed!")
        
        if player.hp <= 0:
            print("You were defeated!")
            return False
            
        monster_starts = False  # Reset for next round

def move_player(dungeon: List[List[str]], player_pos: Tuple[int, int], 
                direction: str, player: Player, difficulty: int) -> Tuple[Tuple[int, int], str]:
    """Moves the player in the specified direction if possible."""
    x, y = player_pos
    new_x, new_y = x, y
    
    # Calculate new position based on direction
    if direction == 'w' and y > 0:
        new_y -= 1
    elif direction == 's' and y < len(dungeon) - 1:
        new_y += 1
    elif direction == 'a' and x > 0:
        new_x -= 1
    elif direction == 'd' and x < len(dungeon[0]) - 1:
        new_x += 1
    
    # Check if new position is valid
    if dungeon[new_y][new_x] == WALL:
        return (x, y), "You can't move through walls!"
    
    # Handle special tiles
    if dungeon[new_y][new_x] == MONSTER:
        if combat(player, difficulty):
            dungeon[new_y][new_x] = FLOOR
            return (new_x, new_y), "You defeated a monster!"
        else:
            return (x, y), "GAME OVER"
    elif dungeon[new_y][new_x] == TREASURE:
        player.inventory["health_potion"] = player.inventory.get("health_potion", 0) + 1
        dungeon[new_y][new_x] = FLOOR
        return (new_x, new_y), "You found a health potion!"
    elif dungeon[new_y][new_x] == EXIT:
        choice = input("You found the exit! Do you want to [d]escend to the next floor or [e]scape the dungeon? ").lower()
        if choice == 'd':
            return (new_x, new_y), "NEXT_FLOOR"
        else:
            return (new_x, new_y), "EXIT"
    
    return (new_x, new_y), "You moved."

def show_stats(player: Player):
    """Display combat statistics"""
    print("\nCombat Statistics:")
    print(f"Character Class: {player.player_class.value}")
    print(f"Level: {player.level}")
    print(f"Experience: {player.exp}/{player.exp_to_next_level}")
    print(f"Total damage dealt: {player.damage_dealt}")
    print(f"Total damage taken: {player.damage_taken}")
    print(f"Remaining HP: {player.hp}/{player.max_hp}")
    print(f"Remaining Mana: {player.mana}/{player.max_mana}")
    print(f"Potions remaining: {player.inventory.get('health_potion', 0)}")

def main_game_loop():
    """Main game loop handling player input and game state."""
    print("\n=== DUNGEON CRAWLER ===")
    input("Press Enter to start...")
    
    # Initialize game
    difficulty = int(input("Choose difficulty (1-3): "))
    difficulty = max(1, min(3, difficulty))
    
    # Class selection
    print("\nChoose your class:")
    print("1. Warrior - High HP and defense, powerful melee strikes")
    print("2. Mage - High mana, powerful spells but low defense")
    print("3. Rogue - Balanced stats, high critical chance and escape rate")
    
    while True:
        try:
            class_choice = int(input("Enter class number (1-3): "))
            if class_choice == 1:
                player_class = PlayerClass.WARRIOR
            elif class_choice == 2:
                player_class = PlayerClass.MAGE
            elif class_choice == 3:
                player_class = PlayerClass.ROGUE
            else:
                raise ValueError
            break
        except ValueError:
            print("Invalid choice. Please enter 1-3.")
    
    while True:  # Main game loop with restart capability
        width, height = 25, 25  # Bigger maze dimensions
        dungeon = create_dungeon(width, height, difficulty)
        player = Player(player_class=player_class)
        player_pos = (1, 1)
        floor = 1
        
        print("\nControls: W/A/S/D to move, I to view inventory, Q to quit")
        print(f"Legend: {PLAYER}=Player, {WALL}=Wall, {FLOOR}=Floor, ", end='')
        print(f"{MONSTER}=Monster, {TREASURE}=Treasure, {EXIT}=Exit\n")
        
        game_result = ""
        
        while True:  # Individual game loop
            print(f"\nFloor {floor}")
            print_dungeon(dungeon, player_pos, player)
            
            action = input("\nWhat would you like to do? ").lower()
            
            if action == 'q':
                game_result = "quit"
                break
                
            if action == 'i':
                player.show_inventory()
                continue
            
            if action in ['w', 'a', 's', 'd']:
                player_pos, message = move_player(dungeon, player_pos, action, player, difficulty)
                print(message)
                
                if message == "NEXT_FLOOR":
                    floor += 1
                    difficulty += 1
                    dungeon = create_dungeon(width, height, difficulty)
                    player_pos = (1, 1)
                    print(f"\nDescending to floor {floor}! Difficulty increased!")
                    continue
                elif message == "EXIT":
                    game_result = "win"
                    break
                elif message == "GAME OVER":
                    game_result = "lose"
                    break
            else:
                print("Invalid input! Use W/A/S/D to move, I for inventory, or Q to quit.")
        
        # End game menu
        while True:
            if game_result == "win":
                print(f"\nCongratulations! You escaped the dungeon after reaching floor {floor}!")
            elif game_result == "lose":
                print(f"\nGame Over! You were defeated on floor {floor}!")
            
            print("\nWhat would you like to do?")
            print("1. Play again")
            print("2. View statistics")
            print("3. Exit game")
            
            choice = input("Enter your choice (1-3): ")
            
            if choice == "1":
                break  # Break inner loop to restart game
            elif choice == "2":
                show_stats(player)
            elif choice == "3":
                print("\nThanks for playing!")
                return  # Exit the entire game
            else:
                print("Invalid choice. Please enter 1-3.")

if __name__ == "__main__":
    main_game_loop()


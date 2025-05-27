"""
Game module for the RPG game.

This module contains the Game class that manages the game flow.
"""
import sys
import os
from typing import List, Tuple, Optional

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rpg_game.character import Character, Boss
from rpg_game.game_logger import GameLogger
from rpg_game.utils.console import clear_screen, press_enter, print_border
from rpg_game.inventory import Potion
from rpg_game.constants import (
    # Player constants
    PLAYER_INITIAL_HEALTH, PLAYER_INITIAL_DAMAGE,
    # Boss constants
    GOBLIN_KING_NAME, GOBLIN_KING_HEALTH, GOBLIN_KING_DAMAGE,
    DARK_SORCERER_NAME, DARK_SORCERER_HEALTH, DARK_SORCERER_DAMAGE,
    # Weapon constants
    WEAPON_ROCK_NAME, WEAPON_ROCK_DAMAGE,
    WEAPON_PAPER_NAME, WEAPON_PAPER_DAMAGE,
    WEAPON_SCISSORS_NAME, WEAPON_SCISSORS_DAMAGE,
    # UI constants
    SEPARATOR_LENGTH, BORDER_LENGTH,
    # Game messages
    WELCOME_MESSAGE, INTRO_MESSAGE,
    # Level messages
    GOBLIN_KING_INTRO, DARK_SORCERER_INTRO,
    # Combat messages
    VICTORY_MESSAGE, DEFEAT_MESSAGE,
    GAME_WIN_MESSAGE, GAME_OVER_MESSAGE
)


class Game:
    """
    Manages the game flow, including character creation, combat, and game state.
    
    This class demonstrates orchestration of other classes and game logic.
    """

    def __init__(self) -> None:
        """Initialize the game."""
        self.logger = GameLogger()
        self.player: Optional[Character] = None
        self.bosses: List[Boss] = []

    def show_intro(self) -> None:
        """Display the game introduction and set up the player character."""
        clear_screen()
        print(WELCOME_MESSAGE)
        player_name = input("Enter your character's name: ").strip().capitalize()
        if not player_name:
            print("You must enter a name to continue.")
            return self.show_intro()
        print(INTRO_MESSAGE.format(player_name=player_name))
        self.setup_game(player_name)

    def setup_game(self, name: str) -> None:
        """
        Set up the game with player character and bosses.
        
        Args:
            name: The player character's name
        """
        weapon_name, weapon_damage = self.choose_weapon()
        self.player = Character(name, PLAYER_INITIAL_HEALTH, PLAYER_INITIAL_DAMAGE, 
                                weapon_name, weapon_damage)
        
        # Add initial items to player's inventory
        health_potion = Potion("Health Potion", "Restores 30 health", 30)
        self.player.add_item(health_potion)
        
        self.player.display()
        press_enter()
        self.bosses = [
            Boss(GOBLIN_KING_NAME, GOBLIN_KING_HEALTH, GOBLIN_KING_DAMAGE), 
            Boss(DARK_SORCERER_NAME, DARK_SORCERER_HEALTH, DARK_SORCERER_DAMAGE)
        ]

    def choose_weapon(self) -> Tuple[str, int]:
        """
        Let the player choose a weapon.
        
        Returns:
            Tuple of weapon name and damage bonus
        """
        weapons = [
            {"name": WEAPON_ROCK_NAME, "damage_bonus": WEAPON_ROCK_DAMAGE},
            {"name": WEAPON_PAPER_NAME, "damage_bonus": WEAPON_PAPER_DAMAGE},
            {"name": WEAPON_SCISSORS_NAME, "damage_bonus": WEAPON_SCISSORS_DAMAGE}
        ]
        options = [weapon["name"] for weapon in weapons]
        prompt = "\nChoose your weapon (Rock, Paper, Scissors): "
        choice_index = self.get_valid_input(prompt, options)
        weapon_data = weapons[choice_index]
        return weapon_data["name"], weapon_data["damage_bonus"]

    def get_valid_input(self, prompt: str, options: List[str]) -> int:
        """
        Get valid user input from a list of options.
        
        Args:
            prompt: The prompt to display to the user
            options: List of valid options
            
        Returns:
            The index of the chosen option
        """
        while True:
            try:
                user_input = input(prompt).capitalize()
            except EOFError:
                print("\nUsing default weapon 'Rock' since input is not available")
                return options.index("Rock")
            if user_input in options:
                return options.index(user_input)
            print("Invalid input, please try again.")

    def show_combat_menu(self) -> str:
        """Display the combat menu and get player's choice."""
        print("\nWhat will you do?")
        print("1. Attack")
        print("2. Use Item")
        print("3. Check Inventory")
        
        while True:
            choice = input("\nEnter your choice (1-3): ")
            if choice in ["1", "2", "3"]:
                return choice
            print("Invalid choice. Please enter a number between 1 and 3.")

    def handle_item_usage(self, player: Character) -> bool:
        """Handle item usage during combat."""
        items = player._inventory.items
        if not items:
            print("\nYour inventory is empty!")
            press_enter()
            return False
            
        print("\nYour items:")
        for i, item in enumerate(items, 1):
            print(f"{i}. {item.get_name()}: {item.get_description()}")
        print(f"{len(items) + 1}. Back")
        
        while True:
            try:
                choice = int(input("\nSelect an item to use (or 0 to cancel): "))
                if choice == 0:
                    return False
                if 1 <= choice <= len(items):
                    item = items[choice - 1]
                    result = player.use_item(item.get_name())
                    print(f"\n{result}")
                    
                    # If it's a potion, apply the healing
                    if isinstance(item, Potion):
                        player.set_health(min(player.get_health() + item.get_heal_amount(), 100))
                        print(f"Healed to {player.get_health()} HP!")
                        
                    press_enter()
                    return True
                print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    def combat(self, player: Character, enemy: Boss) -> bool:
        """
        Handle combat between player and enemy with critical hit support.
        
        Args:
            player: The player character
            enemy: The enemy character
            
        Returns:
            True if the player won, False otherwise
        """
        while player.get_health() > 0 and enemy.get_health() > 0:
            self.display_combat_status(player, enemy)
            
            # Player's turn
            action = self.show_combat_menu()
            
            if action == "1":  # Attack
                damage_dealt, is_critical = player.attack(enemy, self.logger)
                if damage_dealt > 0:
                    print(f"\n You strike {enemy.get_name()} with your {player._weapon.get_name()}!")
                    if is_critical:
                        print("✨ CRITICAL HIT! ✨".center(50))
                    print(f" DEALT {damage_dealt} DAMAGE!")
                    if enemy.get_health() < 30:
                        print(f"\n {enemy.get_name()} is wounded and looks desperate!")
                else:
                    print(f"\n You swing at {enemy.get_name()} but miss!")
                
                press_enter()
                if enemy.get_health() <= 0:
                    break
                    
            elif action == "2":  # Use Item
                self.handle_item_usage(player)
                continue
                
            elif action == "3":  # Check Inventory
                player.display_inventory()
                press_enter()
                continue
            
            # Enemy's turn only if player chose to attack
            if action == "1":
                self.display_combat_status(player, enemy)
                damage_received, enemy_critical = enemy.attack(player, self.logger)
                if damage_received > 0:
                    print(f"\n {enemy.get_name()} attacks you!")
                    if enemy_critical:
                        print("💥 CRITICAL HIT! 💥".center(50))
                    print(f" TOOK {damage_received} DAMAGE!")
                    if player.get_health() < 30:
                        print(f"\n You're badly hurt! Use a potion if you have one!")
                else:
                    print(f"\n {enemy.get_name()} swings at you but misses!")
                    
                press_enter()
                
        if enemy.get_health() <= 0:
            self.print_victory_message(enemy)
            return True
        if player.get_health() <= 0:
            self.print_defeat_message(enemy)
            return False

    def display_combat_status(self, player: Character, enemy: Boss) -> None:
        """
        Display the current combat status with damage amounts.
        
        Args:
            player: The player character
            enemy: The enemy character
        """
        clear_screen()
        level = "LEVEL 1" if enemy.get_name() == GOBLIN_KING_NAME else "LEVEL 2"
        print(f"\n {'=' * 80}")
        print(f"{level}: {enemy.get_name()}")
        print(f" {'=' * 80}")
        print("\nPlayer Stats:")
        player.display()
        print("\nEnemy Stats:")
        enemy.display()
        print(f"\n {'=' * 80}")

    def handle_boss_battles(self) -> None:
        """Handle battles with all bosses in sequence."""
        for boss in self.bosses:
            self.introduce_boss(boss)
            if not self.combat(self.player, boss):
                self.end_game(False)
                return
        self.end_game(True)

    def introduce_boss(self, boss: Boss) -> None:
        """
        Introduce a boss before battle.
        
        Args:
            boss: The boss to introduce
        """
        clear_screen()
        intro_messages = {
            GOBLIN_KING_NAME: GOBLIN_KING_INTRO.format(player_name=self.player.get_name()),
            DARK_SORCERER_NAME: DARK_SORCERER_INTRO.format(player_name=self.player.get_name())
        }
        print(intro_messages.get(boss.get_name(), "A new boss appears!"))
        press_enter()

    def print_victory_message(self, enemy: Boss) -> None:
        """
        Print a victory message and give rewards.
        
        Args:
            enemy: The defeated enemy
        """
        print_border()
        print(VICTORY_MESSAGE.format(enemy_name=enemy.get_name()))
        
        # Add rewards based on the enemy
        if enemy.get_name() == GOBLIN_KING_NAME:
            # Give a health potion after defeating Goblin King
            potion = Potion("Greater Health Potion", "Restores 50 health", 50)
            self.player.add_item(potion)
            print(f"\nYou found a {potion.get_name()} in the Goblin King's loot!")
            print(f"Added {potion.get_name()} to your inventory!")
            
        elif enemy.get_name() == DARK_SORCERER_NAME:
            # Give a special item after defeating Dark Sorcerer
            key = Key("Ancient Key", "A mysterious key that glows with magic", "Final Door")
            self.player.add_item(key)
            print(f"\nThe Dark Sorcerer dropped an {key.get_name()}!")
            print("It might be useful later...")
        
        # Always give some gold
        gold_reward = 50 if enemy.get_name() == GOBLIN_KING_NAME else 100
        self.player.add_gold(gold_reward)
        print(f"You found {gold_reward} gold!")
        
        press_enter()

    def print_defeat_message(self, enemy: Boss) -> None:
        """
        Print a defeat message.
        
        Args:
            enemy: The enemy that defeated the player
        """
        print_border()
        print(DEFEAT_MESSAGE.format(enemy_name=enemy.get_name()))
        press_enter()

    def end_game(self, player_won: bool) -> None:
        """
        End the game and show the final message.
        
        Args:
            player_won: Whether the player won the game
        """
        print_border()
        if player_won:
            print(GAME_WIN_MESSAGE.format(player_name=self.player.get_name()))
        else:
            print(GAME_OVER_MESSAGE.format(player_name=self.player.get_name()))
        print_border()

    def run(self) -> None:
        """Run the game from start to finish."""
        try:
            self.show_intro()
            self.handle_boss_battles()
        except Exception as e:
            print(f"An error occurred: {e}")


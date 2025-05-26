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
from rpg_game.utils.logger import GameLogger
from rpg_game.utils.console import clear_screen, press_enter, print_border
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
        """Initialize a new Game instance."""
        self.player: Optional[Character] = None
        self.bosses: List[Boss] = []
        # Create and manage a GameLogger instance (association)
        self.logger = GameLogger()

    # Show the introductory message and set up the game
    def show_intro(self) -> None:
        """Display the game introduction and set up the player character."""
        clear_screen()
        print(WELCOME_MESSAGE)
        player_name = input("Enter your character's name: ").capitalize()
        print(INTRO_MESSAGE.format(player_name=player_name))
        self.setup_game(player_name)

    # Set up the game by creating the player character and bosses
    def setup_game(self, name: str) -> None:
        """
        Set up the game with player character and bosses.
        
        Args:
            name: The player character's name
        """
        # Get weapon details instead of a Weapon object
        weapon_name, weapon_damage = self.choose_weapon()
        self.player = Character(name, PLAYER_INITIAL_HEALTH, PLAYER_INITIAL_DAMAGE, 
                               weapon_name, weapon_damage)
        self.player.display()
        press_enter()
        self.bosses = [
            Boss(GOBLIN_KING_NAME, GOBLIN_KING_HEALTH, GOBLIN_KING_DAMAGE), 
            Boss(DARK_SORCERER_NAME, DARK_SORCERER_HEALTH, DARK_SORCERER_DAMAGE)
        ]

    # Allow the player to choose a weapon
    def choose_weapon(self) -> Tuple[str, int]:
        """
        Let the player choose a weapon.
        
        Returns:
            A tuple containing the weapon name and damage bonus
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
        # Return weapon name and damage instead of creating a Weapon object
        return weapon_data["name"], weapon_data["damage_bonus"]

    # Get valid user input for weapon choice
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
            user_input = input(prompt).capitalize()
            if user_input in options:
                return options.index(user_input)
            print("Invalid input, please try again.")

    # Handle the combat between player and enemy
    def combat(self, player: Character, enemy: Boss) -> bool:
        """
        Handle combat between player and enemy.
        
        Args:
            player: The player character
            enemy: The enemy character
            
        Returns:
            True if the player won, False otherwise
        """
        while player.get_health() > 0 and enemy.get_health() > 0:
            self.display_combat_status(player, enemy)
            # Pass the logger to the attack methods
            damage_dealt = player.attack(enemy, self.logger)
            print(f"You dealt {damage_dealt} damage to {enemy.name}.")
            if enemy.get_health() <= 0:
                self.print_victory_message(enemy)
                return True

            # Pass the logger to the attack methods
            damage_received = enemy.attack(player, self.logger)
            print(f"{enemy.name} dealt {damage_received} damage to you.")
            if player.get_health() <= 0:
                self.print_defeat_message(enemy)
                return False
            press_enter()

    # Display the current status of the combat
    def display_combat_status(self, player: Character, enemy: Boss) -> None:
        """
        Display the current combat status.
        
        Args:
            player: The player character
            enemy: The enemy character
        """
        clear_screen()
        level = "LEVEL 1" if enemy.name == "Goblin King" else "LEVEL 2"
        print(f"\n=============> {level}: {enemy.name} <=============")
        player.display()
        print("-" * SEPARATOR_LENGTH)
        enemy.display()
        print("-" * SEPARATOR_LENGTH)

    # Handle battles with bosses
    def handle_boss_battles(self) -> None:
        """Handle battles with all bosses in sequence."""
        for boss in self.bosses:
            self.introduce_boss(boss)
            if not self.combat(self.player, boss):
                self.end_game(False)
                return
        self.end_game(True)

    # Introduce each boss before the battle
    def introduce_boss(self, boss: Boss) -> None:
        """
        Introduce a boss before battle.
        
        Args:
            boss: The boss to introduce
        """
        clear_screen()
        intro_messages = {
            GOBLIN_KING_NAME: GOBLIN_KING_INTRO.format(player_name=self.player.name),
            DARK_SORCERER_NAME: DARK_SORCERER_INTRO.format(player_name=self.player.name)
        }
        print(intro_messages.get(boss.name, "A new boss appears!"))
        press_enter()

    # Print victory message after defeating an enemy
    def print_victory_message(self, enemy: Boss) -> None:
        """
        Print a victory message.
        
        Args:
            enemy: The defeated enemy
        """
        print_border()
        print(VICTORY_MESSAGE.format(enemy_name=enemy.name))
        press_enter()

    # Print defeat message after being defeated by an enemy
    def print_defeat_message(self, enemy: Boss) -> None:
        """
        Print a defeat message.
        
        Args:
            enemy: The enemy that defeated the player
        """
        print_border()
        print(DEFEAT_MESSAGE.format(enemy_name=enemy.name))
        press_enter()

    # End the game and show final message
    def end_game(self, player_won: bool) -> None:
        """
        End the game and show the final message.
        
        Args:
            player_won: Whether the player won the game
        """
        print_border()
        if player_won:
            print(GAME_WIN_MESSAGE.format(player_name=self.player.name))
        else:
            print(GAME_OVER_MESSAGE.format(player_name=self.player.name))
        print_border()

    # Run the game
    def run(self) -> None:
        """Run the game from start to finish."""
        self.show_intro()
        self.handle_boss_battles()

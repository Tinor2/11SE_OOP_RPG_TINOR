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
                
            # Enemy's turn
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
        Print a victory message.
        
        Args:
            enemy: The defeated enemy
        """
        print_border()
        print(VICTORY_MESSAGE.format(enemy_name=enemy.get_name()))
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


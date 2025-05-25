from .character import Character, Boss
from .game_logger import GameLogger
from .utils import clear_screen, press_enter, print_border

class Game:
    """
    Main game class that manages the game flow and state.
    Demonstrates association with Character, Boss, and GameLogger classes.
    """
    def __init__(self):
        """Initialize the game with empty player and bosses list."""
        self.player = None
        self.bosses = []
        self.logger = GameLogger()  # Association with GameLogger

    def show_intro(self):
        """Display the game introduction and set up the player."""
        clear_screen()
        print("Welcome to the RPG Adventure!")
        print("In a world where darkness looms, you are the chosen hero "
              "destined to defeat the evil bosses and restore peace.")
        self.setup_game(input("Enter your character's name: ").capitalize())

    def setup_game(self, name):
        """
        Set up the game with player and bosses.
        
        Args:
            name (str): The player's character name
        """
        weapon_name, weapon_damage = self.choose_weapon()
        self.player = Character(name, 110, 10, weapon_name, weapon_damage)
        self.player.display()
        press_enter()
        self.bosses = [Boss("Goblin King", 50, 8), Boss("Dark Sorcerer", 60, 9)]

    def choose_weapon(self):
        """
        Let the player choose a weapon.
        
        Returns:
            tuple: (weapon_name, weapon_damage)
        """
        weapons = [
            {"name": "Rock", "damage_bonus": 2},
            {"name": "Paper", "damage_bonus": 3},
            {"name": "Scissors", "damage_bonus": 4}
        ]
        options = [weapon["name"] for weapon in weapons]
        choice_index = self.get_valid_input("\nChoose your weapon (Rock, Paper, Scissors): ", options)
        weapon_data = weapons[choice_index]
        return weapon_data["name"], weapon_data["damage_bonus"]

    def get_valid_input(self, prompt, options):
        """
        Get valid input from the user.
        
        Args:
            prompt (str): The prompt to display
            options (list): List of valid options
            
        Returns:
            int: Index of the selected option
        """
        while True:
            user_input = input(prompt).capitalize()
            if user_input in options:
                return options.index(user_input)
            print("Invalid input, please try again.")

    def combat(self, player, enemy):
        """
        Handle combat between player and enemy.
        
        Args:
            player (Character): The player character
            enemy (Character): The enemy character
            
        Returns:
            bool: True if player wins, False if player is defeated
        """
        while player.health > 0 and enemy.health > 0:
            self.display_combat_status(player, enemy)
            damage_dealt = player.attack(enemy, self.logger)
            print(f"You dealt {damage_dealt} damage to {enemy.name}.")
            
            if enemy.health <= 0:
                self.print_victory_message(enemy)
                return True

            damage_received = enemy.attack(player, self.logger)
            print(f"{enemy.name} dealt {damage_received} damage to you.")
            
            if player.health <= 0:
                self.print_defeat_message(enemy)
                return False
                
            press_enter()

    def display_combat_status(self, player, enemy):
        """Display the current status of combat."""
        clear_screen()
        level = "LEVEL 1" if enemy.name == "Goblin King" else "LEVEL 2"
        print(f"\n=============> {level}: {enemy.name} <=============")
        player.display()
        print("-" * 30)
        enemy.display()
        print("-" * 30)

    def handle_boss_battles(self):
        """Handle the sequence of boss battles."""
        for boss in self.bosses:
            self.introduce_boss(boss)
            if not self.combat(self.player, boss):
                self.end_game(False)
                return
        self.end_game(True)

    def introduce_boss(self, boss):
        """
        Display the boss introduction.
        
        Args:
            boss (Boss): The boss being introduced
        """
        clear_screen()
        intro_messages = {
            "Goblin King": f"Level 1 - You have entered the lair of the Goblin King. "
                          f"He is known for his strength and brutality. "
                          f"Prepare for battle, {self.player.name}!",
            "Dark Sorcerer": f"Level 2 - You have defeated the Goblin King! Now, you face "
                           f"the Dark Sorcerer, a master of dark magic. "
                           f"Good luck, {self.player.name}!"
        }
        print(intro_messages.get(boss.name, "A new boss appears!"))
        press_enter()

    def print_victory_message(self, enemy):
        """Display victory message after defeating an enemy."""
        print_border()
        print(f"Victory! You defeated {enemy.name}.")
        press_enter()

    def print_defeat_message(self, enemy):
        """Display defeat message after being defeated by an enemy."""
        print_border()
        print(f"Defeat! You were defeated by {enemy.name}.")
        press_enter()

    def end_game(self, victory):
        """
        End the game with the appropriate message.
        
        Args:
            victory (bool): Whether the player won the game
        """
        clear_screen()
        if victory:
            print("Congratulations! You have defeated all the bosses and saved the kingdom!")
        else:
            print("Game Over! The forces of darkness have prevailed...")
        press_enter()

    def run(self):
        """Start and run the game."""
        self.show_intro()
        self.handle_boss_battles()

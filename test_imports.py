"""
Test script to verify imports are working correctly.
"""
from rpg_game.character import Character, Boss
from rpg_game.weapon import Weapon
from rpg_game.utils.logger import GameLogger
from rpg_game.utils.console import print_border


def test_imports():
    """Test that all imports are working correctly."""
    print_border()
    print("Testing imports...")
    print_border()
    
    # Create a weapon
    weapon = Weapon("Test Sword", 5)
    print(f"Created weapon: {weapon.name} with damage bonus: {weapon.damage_bonus}")
    
    # Create a character
    character = Character("Hero", 100, 10, weapon.name, weapon.damage_bonus)
    print(f"Created character: {character.name} with health: {character.get_health()}")
    
    # Create a boss
    boss = Boss("Test Boss", 50, 8)
    print(f"Created boss: {boss.name} with health: {boss.get_health()}")
    
    # Create a logger
    logger = GameLogger()
    print("Created logger")
    
    # Test combat
    damage = character.attack(boss, logger)
    print(f"Character attacked boss for {damage} damage")
    print(f"Boss health after attack: {boss.get_health()}")
    
    print_border()
    print("All imports are working correctly!")
    print_border()


if __name__ == "__main__":
    test_imports()

"""
Character module for the RPG game.

This module contains the Character base class and the Boss subclass.
"""
import sys
import os
from typing import Optional, Union

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rpg_game.weapon import Weapon
from rpg_game.utils.logger import GameLogger
from rpg_game.inventory import Inventory, Item, Potion, Key


class Character:
    """
    Represents a game character with health, damage, and weapon attributes.
    
    This class demonstrates encapsulation with private attributes and getter/setter methods.
    """
    
    def __init__(
        self, 
        name: str, 
        health: int, 
        damage: int, 
        weapon_name: str, 
        weapon_damage_bonus: int
    ) -> None:
        """
        Initialize a new Character.
        Args:   name: The character's name
                health: The character's initial health
                damage: The character's base damage
                weapon_name: The name of the character's weapon
                 weapon_damage_bonus: The damage bonus from the weapon
        """
        self._name = name
        self._health = health
        self._damage = damage
        self._weapon = Weapon(weapon_name, weapon_damage_bonus)
        self._inventory = Inventory()  # Each character has their own inventory
        # The underscore prefix (_) indicates that this attribute is intended to be "private"
        # - meaning it should only be accessed through the getter and setter methods.
        # This is a convention in Python, not a strict rule enforced by the language.

    # Getter for health - provides controlled access to the private attribute
    def get_health(self) -> int:
        """
        Get the character's current health.
        Returns:    The character's current health
        """
        return self._health
    
    # Setter for health with validation - ensures health is never negative
    def set_health(self, new_health: int) -> None:
        """
        Set the character's health with validation.
        Args:   new_health: The new health value
        """
        if new_health < 0:
            self._health = 0
        else:
            self._health = new_health

    # Method for the character to attack an enemy
    def attack(self, enemy: 'Character', logger: Optional[GameLogger] = None) -> int:
        """
        Attack another character.
        
        Args:   enemy: The character to attack
                logger: Optional logger to log the combat
        Returns:    The total damage dealt
        """
        total_damage = self._damage + self._weapon.get_damage_bonus()
        if logger:
            logger.log_combat(self, enemy, total_damage)
        enemy.set_health(enemy.get_health() - total_damage)
        return total_damage

    # Inventory methods
    def add_item(self, item: Item) -> bool:
        """
        Add an item to the character's inventory.
        Args:   item: The item to add
        Returns:    True if item was added, False if inventory is full
        """
        return self._inventory.add_item(item)

    def remove_item(self, item_name: str) -> Optional[Item]:
        """
        Remove an item from the character's inventory.
        Args:   item_name: The name of the item to remove
        Returns:    The removed item if found, None otherwise
        """
        return self._inventory.remove_item(item_name)

    def use_item(self, item_name: str) -> str:
        """
        Use an item from the character's inventory.
        Args:   item_name: The name of the item to use
        Returns:    A message describing the item's effect
        """
        return self._inventory.use_item(item_name)

    def display_inventory(self) -> None:
        """
        Display the contents of the character's inventory.
        """
        print("\n=== Inventory ===")
        print(f"Gold: {self._inventory.gold}")
        print("Items:")
        items = self._inventory.items
        if not items:
            print("  - Empty")
        for item in items:
            print(f"  - {item.get_name()}: {item.get_description()}")
        print("==============")

    def add_gold(self, amount: int) -> None:
        """
        Add gold to the character's inventory.
        Args:   amount: The amount of gold to add
        """
        self._inventory.add_gold(amount)

    def remove_gold(self, amount: int) -> bool:
        """
        Remove gold from the character's inventory.
        Args:   amount: The amount of gold to remove
        Returns:    True if successful, False if not enough gold
        """
        return self._inventory.remove_gold(amount)

    # Getter for name
    def get_name(self) -> str:
        """Get the character's name."""
        return self._name

    # Getter for damage
    def get_damage(self) -> int:
        """Get the character's base damage."""
        return self._damage

    # Method to display character information
    def display(self) -> None:
        """Display the character's information with ASCII art and dynamic effects."""
        weapon_name = self._weapon.get_name() if self._weapon else 'No Weapon'
        weapon_damage = self._weapon.get_damage_bonus() if self._weapon else 0
        health_bar = "❤️" * (self.get_health() // 10)  # Simple health bar
        damage_indicator = "⚔️" if self.get_damage() > 0 else ""
        
        print(f"\n{'=' * 40}")
        print(f"{self.get_name()} {damage_indicator}")
        print(f"Health: {self.get_health()} {health_bar}")
        print(f"Damage: {self.get_damage()}")
        print(f"Weapon: {weapon_name} (+{weapon_damage} Damage)")
        print(f"{'=' * 40}")
        
        # Add some dynamic effects
        if self.get_health() < 30:
            print("⚠️  WARNING: Low health! ⚠️")
        elif self.get_health() < 60:
            print("⚠️  Caution: Health is dropping ⚠️")
        
        # Show weapon effects if equipped
        if self._weapon:
            print(f"\nWeapon Effects:")
            print(f"- {weapon_name} boosts damage by {weapon_damage}")


class Boss(Character):
    """
    Represents a boss enemy that inherits from Character.
    
    This class demonstrates inheritance and method overriding.
    """
    def __init__(self, name: str, health: int, damage: int) -> None:
        """
        Initialize a new Boss.
        Args:      name: The boss's name
                health: The boss's initial health
                damage: The boss's base damage
        """
        # Pass weapon details to parent constructor instead of creating a Weapon object here
        super().__init__(name, health, damage, "Boss Weapon", 5)

    # Boss's special attack with additional damage
    def attack(self, enemy: Character, logger: Optional[GameLogger] = None) -> int:
        """
        Attack another character with the boss's special attack.
        
        Overrides the Character.attack method to add additional damage based on the boss's level.
        
        Args:   enemy: The character to attack
                logger: Optional logger to log the combat
        Returns:    The total damage dealt
        """
        # Call the parent class attack method first
        base_damage = super().attack(enemy, logger)
        
        # Calculate additional damage based on boss's level
        # Using a more consistent formula for additional damage
        boss_level = self.get_damage() // 10  # Simple way to determine boss level
        additional_damage = 3 + boss_level  # Base 3 damage plus level bonus
        
        # Apply the additional damage
        enemy.set_health(enemy.get_health() - additional_damage)
        
        # Log the special attack
        print(f"{self.get_name()} uses a special attack! (+{additional_damage} Damage)")
        if logger:
            logger.log_combat(self, enemy, additional_damage)
        
        # Return total damage (base + additional)
        return base_damage + additional_damage
        # Call the parent class attack method first
        base_damage = super().attack(enemy, logger)
        
        # Calculate additional damage based on boss's level
        # Using a more consistent formula for additional damage
        boss_level = self.get_damage() // 10  # Simple way to determine boss level
        additional_damage = 3 + boss_level  # Base 3 damage plus level bonus
        
        # Apply the additional damage
        enemy.set_health(enemy.get_health() - additional_damage)
        
        # Log the special attack
        print(f"{self.get_name()} uses a special attack! (+{additional_damage} Damage)")
        if logger:
            logger.log_combat(self, enemy, additional_damage)
        
        # Return total damage (base + additional)
        return base_damage + additional_damage

    
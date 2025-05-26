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
        weapon_name: Optional[str] = None, 
        weapon_damage: int = 0
    ) -> None:
        """
        Initialize a new Character.
        
        Args:
            name: The character's name
            health: The character's initial health
            damage: The character's base damage
            weapon_name: The name of the character's weapon (optional)
            weapon_damage: The damage bonus of the character's weapon
        """
        self.name = name
        # The underscore prefix (_) indicates that this attribute is intended to be "private"
        # - meaning it should only be accessed through the getter and setter methods.
        # This is a convention in Python, not a strict rule enforced by the language.
        self._health = health  # Private attribute (by convention)
        self.damage = damage
        # Create the weapon inside the Character constructor (strong composition)
        self.weapon = Weapon(weapon_name, weapon_damage) if weapon_name else None

    # Getter for health - provides controlled access to the private attribute
    def get_health(self) -> int:
        """
        Get the character's current health.
        
        Returns:
            The character's current health
        """
        return self._health
    
    # Setter for health with validation - ensures health is never negative
    def set_health(self, new_health: int) -> None:
        """
        Set the character's health with validation.
        
        Args:
            new_health: The new health value
        """
        if new_health < 0:
            self._health = 0
        else:
            self._health = new_health

    # Method for the character to attack an enemy
    def attack(self, enemy: 'Character', logger: Optional[GameLogger] = None) -> int:
        """
        Attack another character.
        
        Args:
            enemy: The character to attack
            logger: Optional logger to log the combat
            
        Returns:
            The total damage dealt
        """
        total_damage = self.damage + (self.weapon.damage_bonus if self.weapon else 0)
        # Use getter and setter instead of direct attribute access
        current_health = enemy.get_health()
        enemy.set_health(current_health - total_damage)
        # Use the logger if provided (dependency), otherwise fall back to static method
        if logger:
            logger.log_combat(self, enemy, total_damage)
        return total_damage

    # Method to display character information
    def display(self) -> None:
        """Display the character's information."""
        weapon_name = self.weapon.name if self.weapon else 'No Weapon'
        weapon_damage = self.weapon.damage_bonus if self.weapon else 0
        # Use getter instead of direct attribute access
        print(f"Name: {self.name}\nHealth: {self.get_health()}\nDamage: {self.damage}\nWeapon: {weapon_name} (+{weapon_damage} Damage)")


class Boss(Character):
    """
    Represents a boss enemy that inherits from Character.
    
    This class demonstrates inheritance and method overriding.
    """
    
    def __init__(self, name: str, health: int, damage: int) -> None:
        """
        Initialize a new Boss.
        
        Args:
            name: The boss's name
            health: The boss's initial health
            damage: The boss's base damage
        """
        # Pass weapon details to parent constructor instead of creating a Weapon object here
        super().__init__(name, health, damage, "Boss Weapon", 5)

    # Boss's special attack with additional damage
    def attack(self, enemy: Character, logger: Optional[GameLogger] = None) -> int:
        """
        Attack another character with the boss's special attack.
        
        Overrides the Character.attack method to add additional damage.
        
        Args:
            enemy: The character to attack
            logger: Optional logger to log the combat
            
        Returns:
            The total damage dealt
        """
        additional_damage = 1  # Example of special attack causing additional damage
        total_damage = super().attack(enemy, logger)  # Call Character's attack, then add bonus
        # Use getter and setter instead of direct attribute access
        current_health = enemy.get_health()
        enemy.set_health(current_health - additional_damage)  # Apply additional damage
        print(f"{self.name} uses a special attack! (+{additional_damage} Damage)")
        # Use the logger if provided for the special attack
        if logger:
            logger.log_combat(self, enemy, additional_damage)
        return total_damage + additional_damage

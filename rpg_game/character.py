"""
Character module for the RPG game.

This module contains the Character base class and the Boss subclass.
"""
import sys
import os
import random
from typing import Optional, Union, Tuple

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rpg_game.weapon import Weapon
from rpg_game.game_logger import GameLogger
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
        weapon_damage_bonus: int,
        crit_chance: float = 0.1,  # 10% base critical hit chance
        crit_multiplier: float = 1.5  # 1.5x damage on critical hit
    ) -> None:
        """
        Initialize a new Character.
        Args:   name: The character's name
                health: The character's initial health
                damage: The character's base damage
                weapon_name: The name of the character's weapon
                weapon_damage_bonus: The damage bonus from the weapon
                crit_chance: The chance to land a critical hit (0.0 to 1.0)
                crit_multiplier: The damage multiplier for critical hits
        """
        self._name = name
        self._health = health
        self._damage = damage
        self._weapon = Weapon(weapon_name, weapon_damage_bonus)
        self._inventory = Inventory()  # Each character has their own inventory
        self._crit_chance = min(max(crit_chance, 0.0), 1.0)  # Ensure between 0 and 1
        self._crit_multiplier = max(crit_multiplier, 1.0)  # Ensure at least 1.0
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
    def attack(self, enemy: 'Character', logger: Optional[GameLogger] = None) -> Tuple[int, bool]:
        """
        Attack another character with a chance for a critical hit.
        
        Args:
            enemy: The character to attack
            logger: Optional logger to log the combat
            
        Returns:
            Tuple containing (total_damage_dealt, was_critical)
        """
        import random
        
        # Calculate base damage
        base_damage = self._damage + self._weapon.get_damage_bonus()
        
        # Check for critical hit
        is_critical = random.random() < self._crit_chance
        
        # Apply critical multiplier if critical hit
        if is_critical:
            total_damage = int(base_damage * self._crit_multiplier)
        else:
            total_damage = base_damage
            
        # Apply damage to enemy
        enemy.set_health(enemy.get_health() - total_damage)
        
        # Log the attack if logger is provided
        if logger:
            logger.log_combat(self, enemy, total_damage, is_critical)
            
        return total_damage, is_critical

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
        # Find the item in the inventory
        item = None
        for inv_item in self._inventory.items:
            if inv_item.get_name().lower() == item_name.lower():
                item = inv_item
                break
                
        if not item:
            return f"You don't have a {item_name} in your inventory."
            
        # Use the item and get the result message
        result = item.use()
        
        # If it's a potion, remove it after use
        if isinstance(item, Potion):
            self._inventory.items.remove(item)
            
        return result

    def display_inventory(self) -> None:
        """
        Display the contents of the character's inventory with detailed information.
        """
        print("\n" + "=" * 40)
        print("INVENTORY".center(40))
        print("=" * 40)
        
        # Display gold
        print(f"\n💰 GOLD: {self._inventory.gold}")
        
        # Display items
        print("\n📦 ITEMS:")
        items = self._inventory.items
        if not items:
            print("  Your inventory is empty.")
        else:
            for i, item in enumerate(items, 1):
                item_type = "🧪" if isinstance(item, Potion) else "🔑" if isinstance(item, Key) else "📜"
                print(f"  {i}. {item_type} {item.get_name()}: {item.get_description()}")
                
                # Show additional info for potions
                if isinstance(item, Potion):
                    print(f"     Heals: {item.get_heal_amount()} HP")
                # Add more item type specific info here if needed
        
        print("\n" + "=" * 40)

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
        Initialize a new Boss with enhanced combat abilities.
        
        Args:
            name: The boss's name
            health: The boss's initial health
            damage: The boss's base damage
        """
        # Initialize with higher crit chance (25%) and multiplier (2.0x) than regular characters
        super().__init__(
            name=name,
            health=health,
            damage=damage,
            weapon_name="Boss Weapon",
            weapon_damage_bonus=5,
            crit_chance=0.25,  # 25% crit chance
            crit_multiplier=2.0  # 2.0x damage on crit
        )

    # Boss's special attack with additional damage
    def attack(self, enemy: 'Character', logger: Optional[GameLogger] = None) -> Tuple[int, bool]:
        """
        Attack another character with the boss's special attack.
        
        Overrides the Character.attack method to add additional damage based on the boss's level.
        
        Args:
            enemy: The character to attack
            logger: Optional logger to log the combat
            
        Returns:
            Tuple containing (total_damage_dealt, was_critical)
        """
        # Call parent's attack method
        damage, is_critical = super().attack(enemy, logger)
        
        # Boss gets a small chance to deal bonus damage
        if random.random() < 0.2:  # 20% chance for bonus damage
            bonus_damage = self._damage // 2
            enemy.set_health(enemy.get_health() - bonus_damage)
            if logger:
                print(f"\n{self._name} uses a powerful attack! (+{bonus_damage} BONUS DAMAGE!)")
                logger.log_combat(self, enemy, damage + bonus_damage, is_critical=is_critical)
            return damage + bonus_damage, is_critical
            
        return damage, is_critical
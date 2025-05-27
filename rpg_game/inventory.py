"""
Inventory system for the RPG game.

This module demonstrates composition relationships and collection management.
"""
import sys
import os
from typing import List, Optional

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Item:
    """
    Base class for all game items.
    Demonstrates inheritance and base class functionality.
    """
    def __init__(self, name: str, description: str):
        """
        Initialize a new Item.
        Args:   name: The name of the item
                description: A description of the item
        """
        self._name = name
        self._description = description

    def get_name(self) -> str:
        """Get the item's name."""
        return self._name

    def get_description(self) -> str:
        """Get the item's description."""
        return self._description
    
    def use(self) -> str:
        """
        Use the item.
        Returns:    A message describing the item's effect
        """
        return f"Used {self.name}"

class Potion(Item):
    """
    A healing potion that restores health.
    Demonstrates inheritance and overriding methods.
    """
    def __init__(self, name: str, description: str, heal_amount: int):
        """
        Initialize a new Potion.
        Args:   name: The name of the potion
                description: A description of the potion
                heal_amount: The amount of health restored
        """
        super().__init__(name, description)
        self._heal_amount = heal_amount

    def get_heal_amount(self) -> int:
        """Get the potion's heal amount."""
        return self._heal_amount
    
    def use(self) -> str:
        """
        Use the potion to heal.
        Returns:    A message describing the healing effect
        """
        return f"You used {self._name} and recovered {self._heal_amount} HP!"

class Key(Item):
    """
    A key that can unlock doors or chests.
    Demonstrates inheritance with additional attributes.
    """
    def __init__(self, name: str, description: str, location: str):
        """
        Initialize a new Key.
        Args:   name: The name of the key
                description: A description of the key
                location: Where the key can be used
        """
        super().__init__(name, description)
        self._location = location

    def get_location(self) -> str:
        """Get the key's location."""
        return self._location

class Inventory:
    """
    Inventory class to manage items
    Demonstrates composition relationship with Character class.
    """
    def __init__(self, max_slots: int = 10):
        """
        Initialize a new Inventory.
        Args:   max_slots: Maximum number of items that can be carried
        """
        self.max_slots = max_slots
        self.items: List[Item] = []
        self.gold: int = 0
    
    def add_item(self, item: Item) -> bool:
        """
        Add an item to the inventory.
        Args:   item: The item to add
        Returns:    True if item was added, False if inventory is full
        """
        if len(self.items) < self.max_slots:
            self.items.append(item)
            return True
        return False
    
    def remove_item(self, item_name: str) -> Optional[Item]:
        """
        Remove an item from the inventory.
        Args:   item_name: The name of the item to remove
        Returns:    The removed item if found, None otherwise
        """
        for i, item in enumerate(self.items):
            if item.name == item_name:
                return self.items.pop(i)
        return None
    
    def use_item(self, item_name: str) -> str:
        """
        Use an item from the inventory.
        Args:   item_name: The name of the item to use
        Returns:    A message describing the item's effect
        """
        item = self.remove_item(item_name)
        if item:
            return item.use()
        return f"No {item_name} found in inventory"
    
    def display_inventory(self) -> None:
        """
        Display the contents of the inventory.
        """
        print("\n=== Inventory ===")
        print(f"Gold: {self.gold}")
        print("Items:")
        if not self.items:
            print("  - Empty")
        for item in self.items:
            print(f"  - {item.get_name()}: {item.get_description()}")
        print("==============")
    
    def add_gold(self, amount: int) -> None:
        """
        Add gold to the inventory.
        Args:   amount: The amount of gold to add
        """
        self.gold += amount
    
    def remove_gold(self, amount: int) -> bool:
        """
        Remove gold from the inventory.
        Args:   amount: The amount of gold to remove
        Returns:    True if successful, False if not enough gold
        """
        if self.gold >= amount:
            self.gold -= amount
            return True
        return False

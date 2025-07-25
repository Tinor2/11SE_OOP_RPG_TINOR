"""
Weapon module for the RPG game.
"""
import sys
import os
from typing import Optional

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



class Weapon:
    """
    Represents a weapon in the game that can be equipped by characters.
    This class demonstrates composition when used in the Character class.
    """
    def __init__(self, name: str, damage_bonus: int) -> None:
        """
        Initialize a new Weapon.
        Args:   name: The name of the weapon
                damage_bonus: The additional damage this weapon provides
        """
        self._name = name
        self._damage_bonus = damage_bonus

    def get_name(self) -> str:
        """Get the weapon's name."""
        return self._name

    def get_damage_bonus(self) -> int:
        """Get the weapon's damage bonus."""
        return self._damage_bonus

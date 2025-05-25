"""
RPG OOP Concepts - A simple RPG game demonstrating object-oriented programming principles.

This package contains the core components of the RPG game, including character classes,
combat system, and game flow management.
"""

# Import key classes for easier access
from .character import Character, Boss
from .weapon import Weapon
from .game import Game
from .game_logger import GameLogger

__version__ = "0.1.0"

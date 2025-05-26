"""
Logger module for the RPG game.
"""
import sys
import os
import datetime
from typing import Any

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))



class GameLogger:
    """
    GameLogger class to log combat and other game events.
    
    This class demonstrates association relationship with Game (solid line in UML).
    """
    
    def __init__(self, log_to_console: bool = True) -> None:
        """
        Initialize a new GameLogger.
        
        Args:
            log_to_console: Whether to print logs to the console
        """
        self.log_to_console = log_to_console
        
    def log_combat(self, attacker: Any, defender: Any, damage: int) -> None:
        """
        Log a combat event.
        
        Args:
            attacker: The attacking character
            defender: The defending character
            damage: The amount of damage dealt
        """
        # Get current time for the log
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_message = f"[{timestamp}] COMBAT LOG: {attacker.name} attacked {defender.name} for {damage} damage"
        if self.log_to_console:
            print(log_message)
        # Future enhancement: could log to file, database, etc.

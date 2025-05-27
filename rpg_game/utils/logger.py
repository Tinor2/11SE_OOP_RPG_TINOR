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
        
    def log_combat(self, attacker: Any, defender: Any, damage: int, is_critical: bool = False) -> None:
        """
        Log a combat event with optional critical hit information.
        
        Args:
            attacker: The attacking character
            defender: The defending character
            damage: The amount of damage dealt
            is_critical: Whether the attack was a critical hit (default: False)
        """
        # Get current time for the log
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        
        # Prepare the base log message
        critical_text = " CRITICAL HIT!" if is_critical else ""
        log_message = (
            f"[{timestamp}] COMBAT: {attacker.get_name()} attacked {defender.get_name()}"
            f" for {damage} damage{critical_text}"
        )
        
        if self.log_to_console:
            print(log_message)
            # Add some visual feedback for critical hits
            if is_critical:
                print("✨ CRITICAL HIT! ✨".center(50))
        
        # Future enhancement: could log to file, database, etc.

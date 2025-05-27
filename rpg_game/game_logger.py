"""
GameLogger module for the RPG game.

This module contains the GameLogger class which handles logging of game events,
including combat and other important game actions.
"""
import datetime
from typing import Any, Optional


class GameLogger:
    """
    A logger class for recording game events and combat actions.
    
    This class demonstrates the Singleton pattern by maintaining a single instance
    throughout the game, ensuring consistent logging across all components.
    
    Attributes:
        log_to_console (bool): Whether to print logs to the console
    """
    _instance = None
    
    def __new__(cls, log_to_console: bool = True):
        """
        Create a new instance or return the existing one (Singleton pattern).
        
        Args:
            log_to_console: Whether to print logs to the console (default: True)
            
        Returns:
            GameLogger: The single instance of GameLogger
        """
        if cls._instance is None:
            cls._instance = super(GameLogger, cls).__new__(cls)
            cls._instance.log_to_console = log_to_console
        return cls._instance
    
    def log_combat(self, attacker: Any, defender: Any, damage: int, is_critical: bool = False) -> None:
        """
        Log a combat event with optional critical hit information.
        
        Args:
            attacker: The attacking character
            defender: The defending character
            damage: The amount of damage dealt
            is_critical: Whether the attack was a critical hit (default: False)
        """
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        critical_text = " CRITICAL HIT!" if is_critical else ""
        log_message = (
            f"[{timestamp}] COMBAT: {attacker.get_name()} attacked {defender.get_name()}"
            f" for {damage} damage{critical_text}"
        )
        
        if self.log_to_console:
            print(log_message)
            if is_critical:
                print("✨ CRITICAL HIT! ✨".center(50))

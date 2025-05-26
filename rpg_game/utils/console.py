"""
Console utility functions for the RPG game.
"""
import sys
import os
from typing import Any

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))



def clear_screen() -> None:
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def press_enter() -> None:
    """Prompt the user to press Enter to continue."""
    input("\nPress Enter to continue...\n")


def print_border() -> None:
    """Print a border for visual separation."""
    print("-" * 80)

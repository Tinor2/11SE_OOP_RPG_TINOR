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
    try:
        input("\nPress Enter to continue...\n")
    except EOFError:
        print("\n")


def print_border() -> None:
    """Print a border for visual separation with a simple animation effect."""
    border = "-" * 80
    print(border)
    # Simple animation effect
    for i in range(3):
        print(" " * i + "🌟" + " " * (78 - i) + "🌟")
    print(border)

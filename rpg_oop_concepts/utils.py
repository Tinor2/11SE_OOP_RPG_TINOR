import os

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def press_enter():
    """Prompt the user to press Enter to continue."""
    input("\nPress Enter to continue...\n")

def print_border():
    """Print a border for visual separation."""
    print("-" * 80)

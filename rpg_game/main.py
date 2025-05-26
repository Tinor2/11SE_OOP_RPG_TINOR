"""
Main entry point for the RPG game.
"""
import sys
import os

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from rpg_game.game import Game


def main() -> None:
    """Run the RPG game."""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()

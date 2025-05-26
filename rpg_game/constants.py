"""
Constants for the RPG game.

This module contains all the constant values used throughout the game.
"""

# Player constants
PLAYER_INITIAL_HEALTH = 110
PLAYER_INITIAL_DAMAGE = 10

# Boss constants
GOBLIN_KING_NAME = "Goblin King"
GOBLIN_KING_HEALTH = 50
GOBLIN_KING_DAMAGE = 8

DARK_SORCERER_NAME = "Dark Sorcerer"
DARK_SORCERER_HEALTH = 60
DARK_SORCERER_DAMAGE = 9

# Weapon constants
WEAPON_ROCK_NAME = "Rock"
WEAPON_ROCK_DAMAGE = 2

WEAPON_PAPER_NAME = "Paper"
WEAPON_PAPER_DAMAGE = 3

WEAPON_SCISSORS_NAME = "Scissors"
WEAPON_SCISSORS_DAMAGE = 4

# UI constants
SEPARATOR_LENGTH = 30
BORDER_LENGTH = 80

# Game messages
WELCOME_MESSAGE = (
    "🌟 Welcome, brave adventurer, to the RPG Adventure! 🌟\n"
    "Legends tell of heroes who rise against impossible odds—will you become one?"
)
INTRO_MESSAGE = (
    "🌟 IN A REALM SHROUDED IN DARKNESS AND PERIL... 🌟\n"
    "You, {player_name}, have been chosen by fate to restore balance to this troubled land.\n"
    "Two formidable foes stand in your way:\n"
    "The ferocious Goblin King and the enigmatic Dark Sorcerer.\n"
    "Your journey will test your courage, wit, and strength.\n"
    "Gather your resolve—the fate of this world rests in your hands!\n"
    "What will you do with this great responsibility?"
)

# Level messages
GOBLIN_KING_INTRO = (
    "🗡️ LEVEL 1: THE GOBLIN KING'S LAIR 🗡️\n"
    "You step into a dank, torch-lit cavern echoing with guttural laughter...\n"
    "The Goblin King, infamous for his brute strength and savage cunning, awaits!\n"
    "His eyes glow with malevolent intent as he brandishes his massive weapon.\n"
    "Steel yourself, {player_name}, for this battle will be fierce and unforgiving!\n"
    "The fate of the realm depends on your courage and skill!"
)
DARK_SORCERER_INTRO = (
    "🔮 LEVEL 2: THE DARK SORCERER'S TOWER 🔮\n"
    "With the Goblin King fallen, you ascend a spiraling staircase into a chamber pulsing with arcane energy...\n"
    "The Dark Sorcerer, master of forbidden spells and illusions, greets you with a sinister grin.\n"
    "His eyes burn with dark magic as he weaves his spells.\n"
    "Only true heroes survive his magic. Face your fears, {player_name}, and let your legend grow!\n"
    "The final battle begins..."
)

# Combat messages
VICTORY_MESSAGE = (
    "🏆 VICTORY! 🏆\n"
    "With a final, decisive blow, you have vanquished {enemy_name}!\n"
    "The air crackles with your newfound power as the path ahead becomes clear.\n"
    "You've proven your strength and courage! What will you do next?"
)
DEFEAT_MESSAGE = (
    "💀 DEFEAT... 💀\n"
    "You fought valiantly, but {enemy_name} has bested you in battle!\n"
    "Every setback is a lesson—rise again, stronger than before!\n"
    "Remember this defeat and use it to grow stronger for your next battle!"
)
GAME_WIN_MESSAGE = (
    "🎉 HEROIC VICTORY! 🎉\n"
    "All evil has been banished thanks to your bravery, {player_name}!\n"
    "The people rejoice, and songs will be sung of your deeds for generations to come!\n"
    "You are a true legend of the realm! What adventures await you next?"
)
GAME_OVER_MESSAGE = (
    "☠️ GAME OVER ☠️\n"
    "Though darkness prevails this day, the spirit of a true hero never fades!\n"
    "Rest and return, {player_name}—the world still needs you!\n"
    "Your next adventure awaits, with lessons learned and strength gained!"
)

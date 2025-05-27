"""Test script for the inventory system."""

from rpg_game.character import Character
from rpg_game.inventory import Potion, Key, Item

def test_inventory_system():
    """Test the inventory system functionality."""
    print("=== Testing Inventory System ===\n")
    
    # Create a character
    player = Character("TestHero", 100, 10, "Sword", 5)
    
    # Test adding items
    health_potion = Potion("Health Potion", "Restores 30 health", 30)
    mana_potion = Potion("Mana Potion", "Restores 20 mana", 20)
    key = Key("Rusty Key", "An old rusty key", "Dungeon Door")
    
    print("Adding items to inventory...")
    player.add_item(health_potion)
    player.add_item(mana_potion)
    player.add_item(key)
    
    # Test displaying inventory
    print("\nInventory after adding items:")
    player.display_inventory()
    
    # Test using an item
    print("\nUsing Health Potion...")
    print(player.use_item("Health Potion"))
    print(f"Player health after potion: {player.get_health()}")
    
    # Test inventory after using an item
    print("\nInventory after using Health Potion:")
    player.display_inventory()
    
    # Test adding gold
    print("\nAdding 100 gold...")
    player.add_gold(100)
    player.display_inventory()
    
    # Test removing gold
    print("\nRemoving 30 gold...")
    if player.remove_gold(30):
        print("Successfully removed 30 gold")
    else:
        print("Failed to remove gold")
    player.display_inventory()
    
    # Test trying to remove more gold than available
    print("\nTrying to remove 100 gold (only 70 available)...")
    if player.remove_gold(100):
        print("Successfully removed 100 gold")
    else:
        print("Failed to remove gold (as expected)")
    
    print("\n=== Inventory System Test Complete ===")

if __name__ == "__main__":
    test_inventory_system()

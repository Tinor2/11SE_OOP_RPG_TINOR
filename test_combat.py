"""
Combat stress test for the RPG game.

This script tests the combat system with various scenarios to ensure stability.
"""
import sys
import os
import random
import unittest
from typing import Tuple, Optional

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rpg_game.character import Character, Boss
from rpg_game.weapon import Weapon
from rpg_game.utils.logger import GameLogger

class TestCombat(unittest.TestCase):    
    def setUp(self):
        """Set up test fixtures."""
        self.logger = GameLogger(log_to_console=False)
        self.player = Character("Test Player", 100, 10, "Sword", 5)
        self.enemy = Character("Test Enemy", 100, 8, "Axe", 3)
        self.boss = Boss("Test Boss", 200, 15)
    
    def test_normal_combat(self):
        """Test normal combat between two characters."""
        # Player attacks enemy
        damage, is_critical = self.player.attack(self.enemy, self.logger)
        self.assertGreaterEqual(damage, 0)
        self.assertIsInstance(is_critical, bool)
        self.assertLessEqual(self.enemy.get_health(), 100 - (self.player.get_damage() + 5))
    
    def test_critical_hit(self):
        """Test critical hit functionality."""
        # Set crit chance to 100% for testing
        self.player._crit_chance = 1.0
        damage, is_critical = self.player.attack(self.enemy, self.logger)
        self.assertTrue(is_critical)
        self.assertGreaterEqual(damage, (self.player.get_damage() + 5) * 1.5)
    
    def test_boss_combat(self):
        """Test combat with boss special abilities."""
        original_health = self.player.get_health()
        damage, is_critical = self.boss.attack(self.player, self.logger)
        self.assertLessEqual(self.player.get_health(), original_health)
    
    def test_health_bounds(self):
        """Test that health never goes below 0."""
        weak_enemy = Character("Weak Enemy", 1, 1, "Stick", 0)
        self.player.attack(weak_enemy, self.logger)
        self.assertEqual(weak_enemy.get_health(), 0)
        
        # Attack again when already at 0 health
        self.player.attack(weak_enemy, self.logger)
        self.assertEqual(weak_enemy.get_health(), 0)
    
    def test_high_damage(self):
        """Test with very high damage values."""
        strong_player = Character("Strong Player", 1000, 1000, "God Sword", 1000)
        weak_enemy = Character("Weak Enemy", 1, 1, "Stick", 0)
        strong_player.attack(weak_enemy, self.logger)
        self.assertEqual(weak_enemy.get_health(), 0)
    
    def test_multiple_combats(self):
        """Test multiple combat rounds in sequence."""
        for _ in range(100):  # Run 100 combat rounds
            self.player.attack(self.enemy, self.logger)
            self.enemy.attack(self.player, self.logger)
        
        # At least one character should be defeated after many rounds
        self.assertTrue(self.player.get_health() <= 0 or self.enemy.get_health() <= 0)

    def test_boss_bonus_attack(self):
        """Test boss bonus attack functionality."""
        original_health = self.player.get_health()
        bonus_triggered = False
        
        # Try up to 100 times to trigger the 20% bonus attack
        for _ in range(100):
            self.boss.attack(self.player, self.logger)
            if self.player.get_health() < original_health - self.boss.get_damage() - 5:  # More than normal attack
                bonus_triggered = True
                break
            original_health = self.player.get_health()
        
        self.assertTrue(bonus_triggered, "Boss bonus attack should trigger within 100 attempts")

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    
    # Additional manual testing
    print("\n=== Manual Stress Test ===")
    print("Running extended combat simulation...")
    
    player = Character("Player", 1000, 10, "Sword", 5)
    boss = Boss("Final Boss", 2000, 20)
    
    round_count = 0
    while player.get_health() > 0 and boss.get_health() > 0 and round_count < 1000:
        round_count += 1
        print(f"\n--- Round {round_count} ---")
        
        # Player's turn
        player_damage, player_crit = player.attack(boss, GameLogger())
        print(f"Player hits for {player_damage} damage" + (" (CRITICAL!)" if player_crit else ""))
        print(f"Boss health: {boss.get_health()}")
        
        if boss.get_health() <= 0:
            print("Player wins!")
            break
            
        # Boss's turn
        boss_damage, boss_crit = boss.attack(player, GameLogger())
        print(f"Boss hits for {boss_damage} damage" + (" (CRITICAL!)" if boss_crit else ""))
        print(f"Player health: {player.get_health()}")
        
        if player.get_health() <= 0:
            print("Boss wins!")
            break
    
    print(f"\nCombat ended after {round_count} rounds")
    print(f"Final health - Player: {player.get_health()}, Boss: {boss.get_health()}")

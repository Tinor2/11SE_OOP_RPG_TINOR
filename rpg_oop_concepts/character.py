from .weapon import Weapon

class Character:
    """
    Represents a character in the game.
    Uses composition with the Weapon class.
    """
    def __init__(self, name, health, damage, weapon_name=None, weapon_damage=0):
        """
        Initialize a new character.
        
        Args:
            name (str): The character's name
            health (int): The character's health points
            damage (int): The character's base damage
            weapon_name (str, optional): Name of the weapon. Defaults to None.
            weapon_damage (int, optional): Damage bonus from weapon. Defaults to 0.
        """
        self.name = name
        self._health = health  # Private attribute by convention
        self.damage = damage
        # Create the weapon inside the Character constructor (strong composition)
        self.weapon = Weapon(weapon_name, weapon_damage) if weapon_name else None

    @property
    def health(self):
        """Get the character's current health."""
        return self._health
    
    @health.setter
    def health(self, new_health):
        """Set the character's health, ensuring it doesn't go below 0."""
        self._health = max(0, new_health)

    def attack(self, enemy, logger=None):
        """
        Attack an enemy.
        
        Args:
            enemy (Character): The enemy to attack
            logger (GameLogger, optional): Logger for combat events
            
        Returns:
            int: Total damage dealt
        """
        total_damage = self.damage + (self.weapon.damage_bonus if self.weapon else 0)
        enemy.health -= total_damage
        
        if logger:
            logger.log_combat(self, enemy, total_damage)
            
        return total_damage

    def display(self):
        """Display the character's information."""
        weapon_info = str(self.weapon) if self.weapon else 'No Weapon'
        print(f"Name: {self.name}\nHealth: {self.health}\n"
              f"Damage: {self.damage}\nWeapon: {weapon_info}")


class Boss(Character):
    """
    Represents a boss enemy in the game.
    Inherits from Character and overrides the attack method.
    """
    def __init__(self, name, health, damage):
        """
        Initialize a new boss.
        
        Args:
            name (str): The boss's name
            health (int): The boss's health points
            damage (int): The boss's base damage
        """
        super().__init__(name, health, damage, "Boss Weapon", 5)
        self.special_attack_damage = 1

    def attack(self, enemy, logger=None):
        """
        Perform a boss attack with additional special damage.
        
        Args:
            enemy (Character): The enemy to attack
            logger (GameLogger, optional): Logger for combat events
            
        Returns:
            int: Total damage dealt (base + special)
        """
        # Call parent's attack first
        total_damage = super().attack(enemy, logger)
        
        # Add special attack damage
        enemy.health -= self.special_attack_damage
        print(f"{self.name} uses a special attack! (+{self.special_attack_damage} Damage)")
        
        if logger:
            logger.log_combat(self, enemy, self.special_attack_damage)
            
        return total_damage + self.special_attack_damage

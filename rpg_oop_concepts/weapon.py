class Weapon:
    """
    Represents a weapon in the game.
    Used in composition with the Character class.
    """
    def __init__(self, name, damage_bonus):
        """
        Initialize a new weapon.
        
        Args:
            name (str): The name of the weapon
            damage_bonus (int): The damage bonus this weapon provides
        """
        self.name = name
        self.damage_bonus = damage_bonus
        
    def __str__(self):
        """Return a string representation of the weapon."""
        return f"{self.name} (+{self.damage_bonus} Damage)"

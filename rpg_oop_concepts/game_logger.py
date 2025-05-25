import datetime

class GameLogger:
    """
    Handles logging of game events, particularly combat actions.
    Demonstrates association relationship with the Game class.
    """
    def __init__(self, log_to_console=True):
        """
        Initialize the GameLogger.
        
        Args:
            log_to_console (bool): Whether to log messages to console
        """
        self.log_to_console = log_to_console
        
    def log_combat(self, attacker, defender, damage):
        """
        Log combat actions between characters.
        
        Args:
            attacker: The attacking character
            defender: The defending character
            damage: Amount of damage dealt
        """
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_message = f"[{timestamp}] COMBAT LOG: {attacker.name} attacked {defender.name} for {damage} damage"
        if self.log_to_console:
            print(log_message)
        # Future enhancement: could log to file, database, etc.

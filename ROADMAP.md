# RPG Lesson: Development Roadmap

## Educational Purpose

This document outlines the development plan for the RPG OOP demonstration project. The primary purpose is to create a clear, educational codebase that demonstrates object-oriented programming concepts for students learning Python.

## Educational Goals

1. **Clarity Over Complexity**: Prioritize code that is easy to understand over technically sophisticated solutions
2. **Demonstrate OOP Concepts**: Clearly show inheritance, polymorphism, encapsulation, and abstraction
3. **Simple Structure**: Maintain a straightforward project organization without unnecessary complexity
4. **Practical Examples**: Provide real-world examples of OOP principles that students can relate to
5. **Minimal Dependencies**: Avoid external libraries and complex setup requirements
6. **Self-Contained**: Ensure the project can run with minimal setup for classroom use
7. **Well-Documented**: Include clear comments and documentation for educational purposes

## Implementation Approach

The project uses a modular structure with separate files for different components:

1. **Main Game Logic** - `game.py` contains the Game class and main game flow
2. **Core Classes** - Separate files for game entities (Character, Boss, Weapon)
3. **Utility Modules** - Helper functions in the utils directory
4. **Constants** - Game configuration in constants.py
5. **Main Entry Point** - main.py as the entry point to run the game

This approach keeps the demonstration focused and easy to follow while still demonstrating professional coding practices.

## Implementation Steps

### 1. Organize Code Structure
- Group related functions and classes together with clear section comments
- Place utility functions at the top of the file
- Follow with core class definitions (Weapon, Character, Boss)
- Include the Game class for managing the game loop
- Keep the main execution block at the bottom

### 2. Improve Code Quality
- Add comprehensive docstrings to all classes and methods
- Ensure consistent code style throughout the file
- Add type hints for better code clarity
- Include error handling where appropriate

### 3. Enhance Documentation
- Document the purpose of each section
- Add comments explaining complex logic
- Include usage examples in docstrings
- Keep the README.md updated with usage instructions

### 4. Testing and Validation
- Test all game features thoroughly
- Verify that all OOP concepts work as expected
- Check for and fix any bugs or edge cases
- Ensure the game is user-friendly and provides clear feedback

## Educational Notes

### Utility Functions Section
- Demonstrates basic Python functions for console operations
- Shows platform-specific code handling (Windows vs Unix)
- Illustrates simple, reusable functions

### Weapon Class
- Shows a simple class with attributes and minimal methods
- Demonstrates composition (used by Character class)
- Illustrates a basic data structure
=======
```
rpg_game/
├── README.md           # Project documentation
├── main.py             # Entry point with if __name__ == "__main__"
├── game.py             # Game class definition
├── character.py        # Character class
├── boss.py             # Boss class (inherits from Character)
├── weapon.py           # Weapon class
├── game_logger.py      # GameLogger class
└── console_utils.py    # Console utility functions
```

## Implementation Steps

### 1. Create File Structure

- Create the files as outlined above
- No need for `__init__.py` files or package structure

### 2. Extract Utility Functions

- Move `clear_screen()`, `press_enter()`, and `print_border()` to `console_utils.py`
- Move `GameLogger` class to `game_logger.py`

### 3. Extract Game Entities

- Move `Weapon` class to `weapon.py`
- Move `Character` class to `character.py`
  - Add import for `Weapon` and `GameLogger`
- Move `Boss` class to `boss.py`
  - Add import for `Character`

### 4. Extract Game Logic
>>>>>>> e6aac784b800ffb903dea0ebae9f08e14495f1d2

### Character Class
- Demonstrates encapsulation with private attributes and getters/setters
- Shows composition by containing a Weapon object
- Illustrates class methods and instance variables

### Boss Class
- Demonstrates inheritance by extending Character
- Shows method overriding with `attack()`
- Illustrates the use of `super()` to call parent class methods

### Game Class
- Manages the main game loop and state
- Coordinates between different game entities
- Handles user input and game flow
- Demonstrates object interaction and state management

### main.py
- Shows a clean entry point
- Demonstrates minimal code in the main module

## UML Considerations

- Create a UML class diagram showing the relationships between classes
- Use the diagram to illustrate how the relationships are maintained across files
- Highlight how imports represent the relationships in the UML diagram

## Code Organization and Constants

### Recommended Project Structure
```
rpg_game/
│
├── main.py
├── utilities.py
├── weapon.py
├── character.py
├── boss.py
└── game.py
```

### Benefits of This Structure

1. **Modularity**
   - **Ease of Maintenance**: Each file contains a specific part of the functionality, making it easier to locate and fix bugs or make improvements.
   - **Reusability**: Components can be easily reused in other projects or parts of the application.

2. **Separation of Concerns**
   - **Organization**: Code is divided based on responsibilities, adhering to the principle of separation of concerns.
   - **Clarity**: Each file has a clear, single purpose, making the codebase more understandable.

3. **Scalability**
   - **Growth**: The project can grow without becoming unwieldy, with new features added to appropriate modules.
   - **Testing**: Easier to write and maintain unit tests for isolated components.

4. **Collaboration**
   - **Team Work**: Multiple developers can work on different files simultaneously with minimal conflicts.
   - **Version Control**: Changes are more granular and easier to track in version control.

5. **Encapsulation and Abstraction**
   - **Encapsulation**: Related data and methods are kept together, protecting data integrity.
   - **Abstraction**: Implementation details are hidden behind clear interfaces.

### Constants Management

We've implemented a `constants.py` file to centralize all configuration values. This approach offers several benefits:

1. **Improved Maintainability**: All game values can be adjusted in one place, making balancing easier
2. **Better Code Quality**: Eliminates "magic numbers" and hardcoded strings
3. **Reduced Duplication**: Values used in multiple places are defined once
4. **Enhanced Readability**: Code focuses on logic rather than specific values

Our implementation includes:

```python
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
WELCOME_MESSAGE = "Welcome to the RPG Adventure!"
# ... additional message constants
```

These constants are imported and used throughout the codebase, particularly in the `Game` class, to ensure consistency and make the code more maintainable.

## Future Enhancements

### 1. Game Features
- **Add an Inventory System**:
  - Track items and equipment for characters
  - Manage weapons, armor, and consumables

- **Expand Character Types**:
  - Add `Sidekick` and `Villain` classes
  - Implement unique abilities and behaviors

- **Game Progression**:
  - Add experience points and leveling
  - Implement a simple quest system

### 2. Code Quality
- **Add Type Hints**:
  - Improve code clarity and IDE support
  - Catch potential type-related bugs early

- **Enhance Error Handling**:
  - Add input validation
  - Provide clear error messages
  - Handle edge cases gracefully

### 3. Testing
- **Unit Tests**:
  - Test individual classes and methods
  - Ensure consistent behavior

- **Integration Tests**:
  - Test game flow and interactions
  - Verify win/lose conditions

### 4. Documentation
- **Code Comments**:
  - Add explanatory comments for complex logic
  - Document design decisions
          # Enhanced defence logic
          pass
  
  player = Player("Hero", 100, 10)
  sidekick = DefenderSidekick("Robin", 60, 5)
  sidekick.weapon = Weapon("Shield", 3)
  player.sidekick = sidekick
  ```
  - Update documentation and UML diagrams to show the new Sidekick class, its relationship with Player, and its specialised subclasses.

  - Create subclasses of `Weapon` (e.g., `Rock`, `Paper`, `Scissors`) and override a method (such as `use()` or `attack()`) in each subclass to implement unique behavior. This will explicitly show method overriding and polymorphism in action.
  
  **Example:**
  ```python
  class Weapon:
      def use(self, target):
          # Default weapon behaviour
          pass

  class Rock(Weapon):
      def use(self, target):
          # Rock-specific behaviour
          pass

  class Paper(Weapon):
      def use(self, target):
          # Paper-specific behaviour
          pass

  class Scissors(Weapon):
      def use(self, target):
          # Scissors-specific behaviour
          pass
  ```
  - Update documentation and UML diagrams to highlight this use of polymorphism.

  - For different kinds of bosses (e.g., FireBoss, IceBoss), create subclasses that inherit from the `Boss` class. Each boss type can have unique abilities or behaviors.
  - For regular enemies or villains (e.g., Goblin, Orc, Necromancer), create subclasses that inherit from `Character` or from a new `Villain` class (which itself inherits from `Character`).
  - Only special, powerful enemies should inherit from `Boss`. Regular enemies should not inherit from `Boss`.

  **Example class hierarchy:**
  ```python
  class Boss(Character):
      pass

  class FireBoss(Boss):
      pass

  class IceBoss(Boss):
      pass

  class Villain(Character):
      pass

  class Goblin(Villain):
      pass

  class Orc(Villain):
      pass
  ```

- Update UML diagrams and documentation to reflect the new class hierarchy when implemented.

1. **Configuration Files**: Add a `config.py` or JSON configuration
2. **Save/Load System**: Implement game state persistence
3. **Additional Entities**: Add more character types, weapons, etc.
4. **Unit Tests**: Add a `tests/` directory with unit tests for each class

## Learning Approach

1. Start with the single-file version (`rpg_oop_concepts.py`)
2. Introduce the concept of code organisation and modularity
3. Walk through the refactoring process step by step
4. Discuss the benefits and challenges of multi-file organisation
5. Use this as an opportunity to reinforce OOP concepts in a more realistic context

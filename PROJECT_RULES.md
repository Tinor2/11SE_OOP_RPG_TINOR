# RPG Project Guidelines

## Language and Style

- Use **Australian/British English** spelling:
  - colour, behaviour, organise, centre
  - licence (noun), license (verb)
  - practise (verb), practice (noun)
  - customise, analyse, defence, initialise

## Project Structure

### Documentation
- [README.md](README.md) - Project overview and setup
- [CHANGELOG.md](CHANGELOG.md) - Version history
- [ROADMAP.md](ROADMAP.md) - Future plans
- [UML_class_diagram.md](UML_class_diagram.md) - Class structure

## Code Quality

### Code Style
- Keep it simple and readable
- Break tasks into small functions (<30 lines)
- Use clear, descriptive names
  - Good: `player_health`, `calculate_damage()`
  - Bad: `x`, `foo()`, `temp`

### Code Style
- Follow PEP 8:
  - 4 spaces for indentation
  - Spaces around operators
  - Lowercase with underscores

### Comments
- Explain "why" not "what"
  ```python
  # Bad (what)
  x = x + 1  # Add 1 to x
  
  # Good (why)
  x = x + 1  # Compensate for zero-based indexing
  ```

## File Organization

- Single implementation file: `rpg_oop_concepts.py`
- Keep related code together
- Use clear section comments

## Git Workflow

### Commits
- Clear, concise messages (50 chars max)
- Present tense verbs:
  - "Add player movement"
  - "Fix combat damage"
  - "Update README"

### Branching
- Feature branches:
  ```
  git checkout -b feature/player-jump
  git checkout -b fix/combat-bug
  ```

## Documentation

### Code Documentation
- Docstrings for all functions and classes
  ```python
  def calculate_damage(attacker, defender):
      """
      Calculate damage dealt from attacker to defender.
      
      Args:
          attacker: The attacking character
          defender: The defending character
          
      Returns:
          int: The amount of damage dealt
      """
      # Function code here
  ```
- Update changelog for noticeable changes
- For removed features:
  - Delete entries for immediate removals
  - Mark as "Removed" for delayed removals

### Project Documentation
- Keep `README.md` updated with:
  - Installation and setup
  - Basic controls
  - Contribution guidelines

## Best Practices

- Don't overcomplicate things
- Ask questions if unsure
- Keep documentation updated
- Test changes before commits
- Write clear pull request descriptions
- Break big tasks into small, focused functions (try to keep functions under 30 lines)
- Use clear, descriptive names for variables and functions
  - Good: `player_health`, `calculate_damage()`
  - Bad: `x`, `foo()`, `temp`

### Code Style
- Follow basic [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines:
  - Use 4 spaces for indentation (not tabs)
  - Put spaces around operators (`x = 5 + 3`, not `x=5+3`)
  - Use lowercase with underscores for variable and function names (`player_name`, not `PlayerName` or `playername`)

### Comments
- Write comments to explain "why" not "what"
  ```python
  # Bad (explains what the code does - this is obvious)
  x = x + 1  # Add 1 to x
  
  # Good (explains why we're doing this)
  x = x + 1  # Compensate for zero-based indexing
  ```
- Keep comments up-to-date with the code

## 2. File Organization

Keep the implementation simple with a single file:

- `rpg_oop_concepts.py` - Contains all game logic and classes
- Keep related code together in logical sections
- Use clear section comments to separate different components

## 3. Git Basics

### Commits
- Write clear, short commit messages (50 chars or less)
- Start with a verb in present tense:
  - "Add player movement"
  - "Fix combat damage calculation"
  - "Update README with controls"

### Branching
- Create a new branch for each feature/fix:
  ```
  git checkout -b feature/player-jump
  git checkout -b fix/combat-bug
  ```

## 4. Documentation

### Code Documentation
- Write docstrings for all functions and classes:
  ```python
  def calculate_damage(attacker, defender):
      """
      Calculate damage dealt from attacker to defender.
      
      Args:
          attacker: The attacking character
          defender: The defending character
          
      Returns:
          int: The amount of damage dealt
      """
      # Function code here
  ```
- Consistently update the changelog, whenever any noticable changes are made.
- If you are asked to remove a change (i.e. a feature was implemented, but immeadiately after was removed), delete the entry with in the changelog. However if the change was not immeadiately removed, don't delete the entry, but instead mark it as "Removed". The point of this is to keep the changelog useful, as well as a method to provide context to any reader. By deleting any unnecesary entries, everything will be kept to be clean and consice.

### Project Documentation
- Keep `README.md` updated with:
  - How to install and run the game
  - Basic controls and gameplay
  - How to contribute
- Update `CHANGELOG.md` when making changes

## 5. Making Changes

1. Check for existing issues or create a new one
2. Create a new branch for your changes
3. Make small, focused changes
4. Test your changes
5. Submit a pull request with a clear description

## Remember

- Don't overcomplicate things
- Ask questions if you're unsure


---
Last Updated: 2025-05-23

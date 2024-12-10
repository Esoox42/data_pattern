import json

class Character:
    """RPG character with various attributes."""
    def __init__(self):
        self.race = None
        self.character_class = None
        self.skills = []
        self.weapons = []
        self.armor = None

    """Action add skill to character"""
    def add_skill(self, skill: str):
        self.skills.append(skill)

    """Action add weapon to character"""
    def add_weapon(self, weapon: str):
        self.weapons.append(weapon)

    """Action add armor to character"""
    def set_armor(self, armor: str):
        self.armor = armor
    
    """Action describe character"""
    def describe(self):
        print(f"Character Description:")
        print(f"- Race: {self.race}")
        print(f"- Class: {self.character_class}")
        print(f"- Skills: {', '.join(self.skills) if self.skills else 'None'}")
        print(f"- Weapons: {', '.join(self.weapons) if self.weapons else 'None'}")
        print(f"- Armor: {self.armor if self.armor else 'None'}")

    """Save the character's attributes to a JSON file."""
    def save_to_file(self, filename: str):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file, indent=4)
        print(f"Character saved to {filename}")
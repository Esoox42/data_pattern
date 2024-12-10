from abc import ABC, abstractmethod
from character import Character

class CharacterBuilder(ABC):
    """The Builder interface specifying steps to build a character."""
    @abstractmethod
    def set_race(self, race: str):
        pass

    @abstractmethod
    def set_class(self, character_class: str):
        pass

    @abstractmethod
    def add_skill(self, skill: str):
        pass

    @abstractmethod
    def add_weapon(self, weapon: str):
        pass

    @abstractmethod
    def set_armor(self, armor: str):
        pass

    @abstractmethod
    def get_result(self) -> Character:
        pass


class ConcreteCharacterBuilder(CharacterBuilder):
    """Concrete implementation of the CharacterBuilder."""
    def __init__(self):
        self.reset()

    def reset(self):
        self._character = Character()

    def set_race(self, race: str):
        self._character.race = race

    def set_class(self, character_class: str):
        self._character.character_class = character_class

    def add_skill(self, skill: str):
        self._character.add_skill(skill)

    def add_weapon(self, weapon: str):
        self._character.add_weapon(weapon)

    def set_armor(self, armor: str):
        self._character.set_armor(armor)

    def get_result(self) -> Character:
        character = self._character
        self.reset()
        return character


class CharacterDirector:
    """Director class to construct predefined character archetypes."""
    def __init__(self, builder: CharacterBuilder):
        self.builder = builder

    def create_warrior(self):
        self.builder.set_race("Human")
        self.builder.set_class("Warrior")
        self.builder.add_skill("Charge")
        self.builder.add_weapon("Sword")
        self.builder.add_weapon("Shield")
        self.builder.set_armor("Heavy Armor")

    def create_mage(self):
        self.builder.set_race("Elf")
        self.builder.set_class("Mage")
        self.builder.add_skill("Spellcasting")
        self.builder.add_skill("Alchemy")
        self.builder.add_weapon("Magic Staff")
        self.builder.set_armor("Robe")

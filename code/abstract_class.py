from abc import ABC, abstractmethod

class basicPokemon(ABC):
    def __init__(self, name):
        self.name = name
        self._level = 1

    @abstractmethod
    def main_attack(self):
        pass
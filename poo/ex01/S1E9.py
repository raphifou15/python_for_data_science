from abc import ABC, abstractmethod


class Character(ABC):
    """
    class Character
    first_name: str
    is_alive: bool
    """

    def __init__(self, first_name, is_alive=True):
        """Constructor class Character"""
        self.first_name = first_name
        self.is_alive = is_alive
        return

    @abstractmethod
    def die():
        pass


class Stark(Character):
    """class Stark, first_name: str, is_alive: bool"""

    def die(self):
        """Method die, set is_alive to False"""
        self.is_alive = False
        return

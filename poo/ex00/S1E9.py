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


def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)

    try:
        hodor = Character("hodor")
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()

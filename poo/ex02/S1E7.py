from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""

    def __init__(self, first_name, is_alive=True):
        """Constructor class Baratheon"""
        super().__init__(first_name, is_alive)
        params = [
            {"family_name": "Baratheon"},
            {"eyes": "brown"},
            {"hairs": "dark"},
        ]
        self.params = params
        return

    def __str__(self) -> str:
        """Return a string representation of the object"""
        return f"{self.first_name} {self.params}"

    def __repr__(self) -> str:
        """Return a string representation of the object"""
        return f"Vector ({self.params[0]['family_name']},\
 {self.params[1]['eyes']}, {self.params[2]['hairs']})"

    def die(self) -> None:
        """Method die, set is_alive to False"""
        self.is_alive = False
        return


class Lannister(Character):
    """Representing the Lannister family"""

    def __init__(self, first_name, is_alive=True):
        """Constructor class Lannister"""
        super().__init__(first_name, is_alive)
        params = [
            {"family_name": "Lannister"},
            {"eyes": "blue"},
            {"hairs": "light"},
        ]
        self.params = params
        return

    def __str__(self) -> str:
        """Return a string representation of the object"""
        return f"{self.first_name} {self.params}"

    def __repr__(self) -> str:
        """Return a string representation of the object"""
        return f"Vector ({self.params[0]['family_name']},\
 {self.params[1]['eyes']}, {self.params[2]['hairs']})"

    def die(self) -> None:
        """Method die, set is_alive to False"""
        self.is_alive = False
        return

    def create_lannister(name, is_alive=True) -> Character:
        """Factory method to create a Lannister"""
        return Lannister(name, is_alive)

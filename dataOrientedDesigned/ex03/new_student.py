import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random string of 15 characters"""
    return "".join(random.choices(string.ascii_lowercase, k=16))


@dataclass
class Student:
    """Student class with name, nickname, active, login and id"""

    name: str
    nickname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        self.login = self.name.upper()[0] + self.nickname.lower()
        self.id = generate_id()


# your code here


def main():
    # student = Student(name="Edward", nickname="agle")
    student = Student(name="Edward", nickname="agle", id="toto")
    print(student)
    return


if __name__ == "__main__":
    main()

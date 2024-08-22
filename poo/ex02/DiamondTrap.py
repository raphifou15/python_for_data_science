from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class"""

    def set_eyes(self, color):
        """Set the eyes"""
        self.params[0]["eyes"] = color

    def set_hairs(self, color):
        """Set the hairs"""
        self.params[0]["hairs"] = color

    def get_eyes(self):
        """Get the eyes"""
        return self.params[0]["eyes"]

    def get_hairs(self):
        """Get the hairs"""
        return self.params[0]["hairs"]


def main():
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)
    return


if __name__ == "__main__":
    main()

class calculator:
    def __init__(self, vector: dict) -> None:
        self.vector = vector
        return

    # your code here
    def __add__(self, object) -> None:
        self.vector = [(elem + object) for elem in self.vector]
        print(self.vector)
        return

    # your code here
    def __mul__(self, object) -> None:
        self.vector = [(elem * object) for elem in self.vector]
        print(self.vector)
        return

    # your code here
    def __sub__(self, object) -> None:
        self.vector = [(elem - object) for elem in self.vector]
        print(self.vector)
        return

    # your code here
    def __truediv__(self, object) -> None:
        if object == 0:
            print("Error: Division by zero")
            return
        self.vector = [(elem / object) for elem in self.vector]
        print(self.vector)
        return


def main():
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
    return


if __name__ == "__main__":
    main()

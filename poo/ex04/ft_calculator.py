class calculator:
    """This class is a calculator"""

    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """This function calculates the dot product of two vectors"""
        print(
            "Dot product is: \
{}".format(
                sum(V1 * V2 for V1, V2 in zip(V1, V2))
            )
        )
        return

    def add_vec(V1: list[float], V2: list[float]) -> None:
        """This function calculates the addition of two vectors"""
        print("Add Vector is : {}".format([V1 + V2 for V1, V2 in zip(V1, V2)]))
        return

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """This function calculates the subtraction of two vectors"""
        print("Sous Vector is: {}".format([V1 - V2 for V1, V2 in zip(V1, V2)]))
        return


a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a, b)
calculator.add_vec(a, b)
calculator.sous_vec(a, b)

def square(x: int | float) -> int | float:
    """Return the square of the input."""
    return x * x


# your code here
def pow(x: int | float) -> int | float:
    """Return the power of the input."""
    power = x**x
    return power


# your code here
def outer(x: int | float, function) -> object:
    """Return a function that will return the result of the function on x each time it is called."""
    count = 0

    def inner() -> float:
        nonlocal count
        count += 1
        nonlocal x
        x = function(x)
        return x

    return inner


def main():
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    main()

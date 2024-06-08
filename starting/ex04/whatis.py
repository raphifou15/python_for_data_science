import sys

try:
    assert len(sys.argv) == 2, "more than one argument is provided"
    assert sys.argv[1].isdigit(), "argument is not an integer"
    num = int(sys.argv[1])
    print("I'm Odd.") if num % 2 else print("I'm Even.")
except AssertionError as error:
    print(f"AssertionError: {error}")

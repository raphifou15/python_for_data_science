import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
}


def is_alpha_or_space(val: str):
    """
    Check if all characters in the input string are either alphabetic or whitespace.

    This function iterates through each character in the input string `val`. It returns `True` if every character
    in the string is either an alphabetic character (a-z, A-Z) or a whitespace character (e.g., spaces, tabs).
    If any character is not alphabetic or whitespace, it returns `False`.

    Args:
        val (str): The string to be checked.

    Returns:
        bool: `True` if all characters in the string are alphabetic or whitespace; `False` otherwise.

    Example:
        >>> is_alpha_or_space("Hello World")
        True
        >>> is_alpha_or_space("Hello123")
        False
        >>> is_alpha_or_space("Hello\tWorld")
        True
    """
    for elem in val:
        if not (elem.isalpha() or elem.isspace()):
            return False
    return True


def check_error():
    """
    Validate command-line arguments and check for errors.

    This function performs validation on command-line arguments:
    1. It checks if exactly one argument is provided (excluding the script
    name).
    2. It verifies if the provided argument consists only of alphabetic
    characters or whitespace.

    If any of these conditions are not met, the function prints an
    `AssertionError` message and returns `False`.
    If both conditions are satisfied, it returns `True`.

    Returns:
        bool: `True` if the arguments are valid; `False` otherwise.

    Example:
        If the script is executed with valid arguments:
            >>> check_error()
            True
        If the script is executed with invalid arguments:
            >>> check_error()
            AssertionError: the arguments are bad
            False
    """
    try:
        assert len(sys.argv) == 2, "AssertionError: the arguments are bad"
        assert is_alpha_or_space(
            sys.argv[1]
        ), "AssertionError: the arguments \
are bad"
    except AssertionError as error:
        print(error)
        return False
    return True


def main():
    if check_error() is False:
        return
    morse_to_print = ""

    for elem in sys.argv[1]:
        elemUpper = elem.upper()
        morse_to_print += NESTED_MORSE.get(elemUpper)
    morse_to_print = [*morse_to_print]
    morse_to_print.pop(len(morse_to_print) - 1)
    morse_to_print = "".join(morse_to_print)
    print(morse_to_print)
    return


if __name__ == "__main__":
    main()

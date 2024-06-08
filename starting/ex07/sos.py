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
    for elem in val:
        if not (elem.isalpha() or elem.isspace()):
            return False
    return True


def check_error():
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

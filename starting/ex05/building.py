import sys


def get_input():
    """
    Reads the user's input until Enter or Ctrl+D is pressed.

    Return :
       Str: The text entered by the user, with newlines added after each input.
    """
    try:
        print("What is the text to count?")
        val = sys.stdin.readline()
        return val
    except EOFError:
        print("Fin de l'entrée.")
    except KeyboardInterrupt:
        print("You cancelled the operation.")
    return ""


def calculation_string(str_to_count: str):
    """
    Counts the number of upper, lower, punctuation, space, digit, and total
    characters and displays them.

    Return :
        Void: This function does not return anything.
    """
    punctuations_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    punctuations_tab = [char for char in punctuations_chars]
    upper_case = 0
    lower_case = 0
    punctuation = 0
    digit = 0
    total = len(str_to_count)
    space = 0

    for character in str_to_count:
        if character.isupper():
            upper_case += 1
        elif character.islower():
            lower_case += 1
        elif character in punctuations_tab:
            punctuation += 1
        elif character.isdigit():
            digit += 1
        elif character.isspace():
            space += 1
    print(f"The text contains {total} characters:")
    print(f"{upper_case} upper letters")
    print(f"{lower_case} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")
    return


def main():
    """
    Starting function that processes command-line arguments or prompts the
    user for input,
    then calculates and displays the number of different types of characters.

    This function performs the following steps:
    1. Checks if more than one command-line argument is provided and raises an
    assertion error if true.
    2. If a single command-line argument is provided, it uses that as the
    string to be processed.
    3. If no command-line argument is provided, it prompts the user to input a
    string.
    4. Passes the obtained string to the `calculation_string` function to
    count and display the characters.

    Raises:
        AssertionError: If more than one command-line argument is provided.

    Returns:
        None: This function does not return anything.
    """
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return
    str_to_count = ""
    if len(sys.argv) == 2:
        str_to_count = sys.argv[1]
    while not str_to_count:
        str_to_count = get_input()

    calculation_string(str_to_count)


if __name__ == "__main__":
    main()

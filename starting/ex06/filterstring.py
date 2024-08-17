import sys
from ft_filter import ft_filter


def checkPunctuationAndInvisible(val: str):
    """
    Check if the input string contains any punctuation characters or invisible
    (non-printable) characters.

    This function iterates through each character in the input string `val` to
    determine if it contains any punctuation characters or invisible
    characters (characters with ASCII values less than 32 or equal to 127).It
    returns `False` if any such character is found; otherwise, it returns
    `True`.

    Args:
        val (str): The string to be checked.

    Returns:
        bool: `False` if the string contains any punctuation or invisible
        characters, `True` otherwise.

    Example:
        >>> checkPunctuationAndInvisible("HelloWorld")
        True
        >>> checkPunctuationAndInvisible("Hello, World!")
        False
        >>> checkPunctuationAndInvisible("Hello\x7fWorld")
        False
    """
    punctuations_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    punctuations_tab = [char for char in punctuations_chars if char]
    for elem in val:
        if elem in punctuations_tab:
            return False
        if ord(elem) < 32 or ord(elem) == 127:
            return False
    return True


def main():

    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert not sys.argv[1].isdigit(), "the arguments are bad"
        assert checkPunctuationAndInvisible(
            sys.argv[1]
        ), "the arguments are \
bad"
        assert sys.argv[2].isdigit(), "the arguments are bad"
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return

    tab = sys.argv[1].split(" ")
    num = int(sys.argv[2])
    res = list(ft_filter(lambda x: len(x) > num, tab))
    print(res)
    return 0


if __name__ == "__main__":
    main()

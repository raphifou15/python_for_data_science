import sys
from ft_filter import ft_filter


def checkPunctuationAndInvisible(val: str):
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
    res = list(ft_filter(lambda x: len(x) == num, tab))
    print(res)
    return 0


if __name__ == "__main__":
    main()

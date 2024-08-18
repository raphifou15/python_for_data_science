import numpy as np


def check_if_int(elem) -> bool:
    """
    Check if elem is an int or not

    Return: bool

        TRUE if elem is an int

        FALSE if elem is not an int
    """
    return isinstance(elem, int)


def check_if_list_number(elem) -> bool:
    """
    Check if elem is a list and if each elem of the list is a number

    Return: bool

        TRUE if elem is a list and each elements of the list are numbers

        FALSE other cases
    """
    if not isinstance(elem, list):
        return False
    return all(isinstance(item, (int, float)) for item in elem)


def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """
    calculate the bmi with the weight and height present in each list

    Return:
        list of bmi in number
        if one of the elem is not a list -> list empty
        if one of the list have other than a number -> list empty
        if the lists have not the same size -> list empty
    """
    try:
        assert check_if_list_number(height) and check_if_list_number(
            weight
        ), "Both height and weight must be lists of numbers."
        assert len(height) == len(
            weight
        ), "Both height and weight must have the same size"
        assert (
            len(height) > 0 and len(weight) > 0
        ), "Both height and weight must have a list none empty"
        bmi = np.divide(weight, np.square(height))
        return bmi.tolist()
    except AssertionError as error:
        print(error)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    check if the limit have been exceeded for each element

    Return:

        list of TRUE OR FALSE depending if limit has been exceeded
    """
    try:
        assert check_if_list_number(bmi), "bmi must be list of numbers."
        assert check_if_int(limit), "limit must be an int."
    except AssertionError as error:
        print(error)
        return []
    return [elem > limit for elem in bmi]


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
    return


if __name__ == "__main__":
    main()

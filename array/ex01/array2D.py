def check_if_list(elem) -> bool:
    """
    Check if elem is a list

    Return: bool

        TRUE if elem is a list

        FALSE other cases
    """
    if not isinstance(elem, list):
        return False
    return True


def check_if_list_number(elem) -> bool:
    """
    Check if elem is a list and if each elem of the list is a number

    Return: bool

        TRUE if elem is a list and each elements of the list are numbers

        FALSE other cases
    """
    if not check_if_list(elem):
        return False
    if not elem:
        return False
    return all(isinstance(item, (int, float)) for item in elem)


def check_if_int(elem) -> bool:
    """
    Check if elem is an int or not

    Return: bool

        TRUE if elem is an int

        FALSE if elem is not an int
    """
    return isinstance(elem, int)


def check_if_all_list_number(lst: list):
    """
    check if all elem are list and countain number

    Return : bool
    """
    if not lst:
        return False
    return all(check_if_list_number(elem) for elem in lst)


def check_if_all_list_same_size(lst: list):
    """
    check if all the list have the same size

    Return bool
    """
    first = len(lst[0])
    if first == 0:
        return False
    return all((len(elem) == first) for elem in lst)


def print_shape(lst: list, ms: int):
    """
    Print shape of list
    """
    res = (len(lst), len(lst[0]))
    if ms == 1:
        print(f"My shape is : {res}")
    elif ms == 2:
        print(f"My new shape is : {res}")


def slice_me(family: list, start: int, end: int) -> list:
    """
    retrieve par of array ask in function of start and end

    If error appen return empty array
    """
    try:
        assert check_if_list(family), "family must be a list"
        assert check_if_int(start), "start must be an int"
        assert check_if_int(end), "end must be an int"
        assert check_if_all_list_number(
            family
        ), "family must be a 2 dimensions list of numbers"
        assert check_if_all_list_same_size(
            family
        ), "all list mumbers must have the same size"
    except AssertionError as error:
        print(error)
        return []
    print_shape(family, 1)
    new_array = family[start:end]
    print_shape(new_array, 2)
    return new_array


def main():
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2],
    ]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()

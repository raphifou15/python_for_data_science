def ft_mean(args, value) -> float:
    """This function calculates the mean of a list of numbers"""
    if len(args) == 0:
        print("ERROR")
        return 0
    else:
        print(f"{value} : {sum(args) / len(args)}")
    return sum(args) / len(args)


def ft_median(args, value) -> None:
    """This function calculates the median of a list of numbers"""
    if len(args) == 0:
        print("ERROR")
    else:
        n_args = list(args)
        n_args.sort()
        length = len(n_args)
        if length % 2 == 0:
            print(f"{value} : {(n_args[length // 2])}")
        else:
            print(f"{value} : {n_args[len(n_args) // 2]}")
    return


def ft_quartile(args, value) -> None:
    """This function calculates the first and third quartile of a list
    of numbers"""
    if len(args) == 0:
        print("ERROR")
        return
    n_args = list(args)
    n_args.sort()
    length = len(n_args)
    list_quartile = []
    if length % 4 == 0:
        first_quartile = n_args[length // 4 - 1]
        list_quartile.append(first_quartile)
        third_quartile = n_args[length * 3 // 4 - 1]
        list_quartile.append(third_quartile)
    else:
        first_quartile = n_args[length // 4]
        list_quartile.append(first_quartile)
        third_quartile = n_args[length * 3 // 4]
        list_quartile.append(third_quartile)

    print(f"{value} : {list_quartile}")
    return


def ft_standard_deviation_and_variation(args, value) -> None:
    """This function calculates the standard deviation and the variance"""
    if len(args) == 0:
        print("ERROR")
        return
    mean = sum(args) / len(args)
    n_args = list(args)
    for i in range(len(n_args)):
        n_args[i] = (n_args[i] - mean) ** 2

    variance = sum(n_args) / len(n_args)

    if value == "var":
        print(f"{value} : {variance}")
        return
    standard_deviation = variance**0.5
    print(f"{value} : {standard_deviation}")

    return


def ft_statistics(*args, **kwargs) -> None:
    """This function calculates the mean, median, quartile, standard"""
    for value in kwargs.values():
        if value == "mean":
            ft_mean(args, value)
        elif value == "median":
            ft_median(args, value)
        elif value == "quartile":
            ft_quartile(args, value)
        elif value == "std" or value == "var":
            ft_standard_deviation_and_variation(args, value)

    return


def main():
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")
    return


if __name__ == "__main__":
    main()

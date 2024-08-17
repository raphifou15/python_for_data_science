def ft_filter(function, iterable):
    """
    Return an iterator that filters elements from iterable based on function.

    This function filters elements of `iterable` using `function`. The
    `function` is applied to each element, and if it returns `True`, the
    element is included in the result. If `function` is `None`, all elements
    that are `True` in a boolean context are included in the result.

    Args:
        function (callable or None): A function that returns a boolean value.
        iterable (iterable): The iterable to filter.

    Returns:
        iterator: An iterator yielding elements of `iterable` for which
        `function` returns `True`. If `function` is `None`, yields elements
        that are `True` in a boolean context.

    Example:
        >>> numbers = [1, 2, 3, 4, 5]
        >>> result = ft_filter(lambda x: x % 2 == 0, numbers)
        >>> list(result)
        [2, 4]
    """
    if function is None:
        return (elem for elem in iterable if elem)
    return (elem for elem in iterable if function(elem))

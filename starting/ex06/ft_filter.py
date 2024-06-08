def ft_filter(function, iterable):
    if function is None:
        for elem in iterable:
            if elem:
                yield elem
    for elem in iterable:
        if function(elem):
            yield elem

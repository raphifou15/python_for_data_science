def callLimit(limit: int):
    """Decorator to limit the number of calls to a function"""
    count = 0

    def callLimiter(function):
        """Encapsulates the limiting logic and returns a limited version
        of the target function"""

        def limit_function(*args, **kwds):
            """Inner function to limit the number of calls to a function"""
            nonlocal count
            count += 1
            try:
                if count > limit:
                    raise Exception("call too many times")
                return function(*args, **kwds)
            except Exception as e:
                print(e)
                return

        return limit_function

    return callLimiter


@callLimit(3)
def f():
    print("f()")


@callLimit(1)
def g():
    print("g()")


def main():
    for i in range(3):
        f()
        g()
    return


if __name__ == "__main__":
    main()

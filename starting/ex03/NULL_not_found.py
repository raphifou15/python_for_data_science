def NULL_not_found(object: any) -> int:
    a = True
    if object:
        a = True
    else:
        a = False
    if not a or object != object:
        name = type(object).__name__
        print(f"{name}: {object} {type(object)}")
        return 0
    print("Type not Found")
    return 1
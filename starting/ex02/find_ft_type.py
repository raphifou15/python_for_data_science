def all_thing_is_obj(object: any) -> int:
    tab = ["list", "tuple", "set", "dict"]
    name = type(object).__name__
    if name in tab:
        print(f"{name.capitalize()} : {type(object)}")
    elif name == "str":
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print("Type not found")
    return 42

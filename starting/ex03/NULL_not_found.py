def NULL_not_found(object: any) -> int:
    """
    Vérifie si l'objet passé en argument est valide ou non, et retourne un
    entier en conséquence.

    La fonction effectue les actions suivantes :
    1. Vérifie si l'objet passé en argument est évalué à True ou False.
    2. Si l'objet est None, un objet non valide, ou si l'objet n'est pas égal
    à lui-même (comme dans le cas d'un NaN),
       la fonction imprime le type de l'objet, sa valeur, et retourne 0.
    3. Si l'objet est considéré comme valide, la fonction imprime "Type not
    Found" et retourne 1.

    Args:
        object (any, optionnel): L'objet à tester. Par défaut, None.

    Returns:
        int: 0 si l'objet est None, non valide ou NaN; 1 sinon.
    """
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

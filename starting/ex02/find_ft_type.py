"""
Affiche le type de l'objet et retourne toujours 42.

Paramètres :
object (any) : L'objet dont le type doit être affiché.

Retourne :
int : Retourne toujours 42.

Comportement :
- Si l'objet est de type 'list', 'tuple', 'set' ou 'dict',
affiche le type de l'objet.
- Si l'objet est de type 'str', affiche un message personnalisé
avec le type de l'objet.
- Sinon, affiche 'Type not found'.
"""


def all_thing_is_obj(object: any) -> int:
    tab = ["list", "tuple", "set", "dict"]
    # extrait le nom du type d'un objet
    name = type(object).__name__
    if name in tab:
        print(f"{name.capitalize()} : {type(object)}")
    elif name == "str":
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print("Type not found")
    return 42

import sys


def check_if_string_is_int(string):
    """
    Vérifie si une chaîne de caractères peut être convertie en un entier.

    Cette fonction tente de convertir la chaîne passée en argument en un entier
    à l'aide de la fonction `int()`. Si la conversion réussit, la fonction
    retourne `True`. Si la conversion échoue en levant une exception
    `ValueError`,
    la fonction retourne `False`, indiquant que la chaîne ne peut pas être
    convertie en entier.

    Args:
        string (str): La chaîne de caractères à vérifier.

    Returns:
        bool: `True` si la chaîne peut être convertie en entier, `False` sinon.
    """
    try:
        int(string)
        return True
    except ValueError:
        return False


"""
Ce programme détermine si un argument fourni en ligne de commande est un
nombre pair ou impair,
et affiche un message correspondant. Il vérifie également certaines conditions
à l'aide d'assertions.

Fonctionnement :
1. Si aucun argument n'est fourni, le programme se termine immédiatement avec
un code de sortie 0.
2. Si plus d'un argument est fourni, une AssertionError est levée avec le
message "more than one argument is provided".
3. Si l'argument fourni n'est pas une chaîne convertible en entier, une
AssertionError est levée avec le message "argument is not an integer".
4. Si l'argument est un entier valide, il est converti en entier, puis le
programme détermine si ce nombre est pair ou impair :
   - Si le nombre est impair, le programme affiche "I'm Odd."
   - Si le nombre est pair, le programme affiche "I'm Even."

Gestion des erreurs :
- Si une assertion échoue, le programme capture l'AssertionError et affiche un
message avec la cause de l'erreur.
"""

try:
    if len(sys.argv) < 2:
        exit(0)
    assert len(sys.argv) == 2, "more than one argument is provided"
    assert check_if_string_is_int(sys.argv[1]), "argument is not an integer"
    num = int(sys.argv[1])
    print("I'm Odd.") if num % 2 else print("I'm Even.")
except AssertionError as error:
    print(f"AssertionError: {error}")

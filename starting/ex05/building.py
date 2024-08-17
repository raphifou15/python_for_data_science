import sys


def get_input():
    """
    Demande à l'utilisateur d'entrer un texte via l'entrée standard.

    Cette fonction affiche un message demandant à l'utilisateur de saisir un
    texte. Elle lit ensuite l'entrée de l'utilisateur
    depuis l'entrée standard (par exemple, le terminal) et retourne ce texte.
    Si l'utilisateur interrompt l'entrée avec
    `Ctrl+D` (EOFError) ou `Ctrl+C` (KeyboardInterrupt), la fonction gère ces
    exceptions de manière appropriée.

    Returns:
        str: Le texte entré par l'utilisateur. Si une interruption se produit,
        la fonction retourne une chaîne vide.
    """
    try:
        print("What is the text to count?")
        val = sys.stdin.readline()
        return val
    except EOFError:
        print("Fin de l'entrée.")
    except KeyboardInterrupt:
        print("You cancelled the operation.")
    return ""


def calculation_string(str_to_count: str):
    """
    Analyse une chaîne de caractères et compte différents types de caractères.

    Cette fonction prend une chaîne de caractères en entrée et compte le
    nombre de majuscules, minuscules,
    signes de ponctuation, chiffres, et espaces. Elle affiche ensuite un
    résumé détaillé des résultats,
    incluant le nombre total de caractères.

    Args:
        str_to_count (str): La chaîne de caractères à analyser.

    Prints:
        Résumé du nombre de chaque type de caractère dans la chaîne, incluant :
        - Nombre total de caractères.
        - Nombre de lettres majuscules.
        - Nombre de lettres minuscules.
        - Nombre de signes de ponctuation.
        - Nombre d'espaces.
        - Nombre de chiffres.

    Returns:
        None: La fonction ne retourne aucune valeur, elle se contente
        d'afficher les résultats.
    """
    punctuations_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    punctuations_tab = [char for char in punctuations_chars]
    upper_case = 0
    lower_case = 0
    punctuation = 0
    digit = 0
    total = len(str_to_count)
    space = 0

    for character in str_to_count:
        if character.isupper():
            upper_case += 1
        elif character.islower():
            lower_case += 1
        elif character in punctuations_tab:
            punctuation += 1
        elif character.isdigit():
            digit += 1
        elif character.isspace():
            space += 1
    print(f"The text contains {total} characters:")
    print(f"{upper_case} upper letters")
    print(f"{lower_case} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")
    return


def main():
    """
    Point d'entrée principal du programme.

    Cette fonction vérifie les arguments de la ligne de commande pour
    s'assurer qu'au plus un argument est fourni.
    Si un argument est fourni, il est utilisé comme texte à analyser. Sinon,
    la fonction demande à l'utilisateur
    d'entrer un texte via l'entrée standard. Le texte est ensuite analysé pour
    compter le nombre de majuscules,
    minuscules, signes de ponctuation, chiffres, et espaces, en utilisant la
    fonction `calculation_string`.

    Exceptions:
        AssertionError: Lancée si plus d'un argument est fourni via la ligne
        de commande.

    Returns:
        None: La fonction ne retourne aucune valeur, elle exécute simplement
        la logique du programme.
    """
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return
    str_to_count = ""
    if len(sys.argv) == 2:
        str_to_count = sys.argv[1]
    while not str_to_count:
        str_to_count = get_input()

    calculation_string(str_to_count)


if __name__ == "__main__":
    main()

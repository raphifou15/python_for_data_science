# python_for_data_science

## Table des Matières

1. [Introduction](#introduction)

<details>
  <summary>2. <a href="#syntaxe-de-base">Syntaxe de Base</a></summary>

- [Liste](#liste)
- [Tuple](#tuple)
- [Set](#set)
- [Les dictionnaires](#les-dictionnaires)
- [Import](#import)
- [def](#def)
- [in](#in)

</details>

<details>

<summary>3. <a href="starting">Starting</a></summary>

- [Exercice 0 : First python script](#exercice-0--first-python-script)
- [Exercice 1 : First use of package](#exercice-1--first-use-of-package)
- [Exercice 2 : First use of package](#exercice-2--first-function-python)
- [Exercice 3 : NULL not found](#exercice-3--null-not-found)
- [Exercice 4 : The Even and the Odd](#exercice-4--the-even-and-the-odd)
- [Exercice 5 : First standalone program python](#exercice-5--first-standalone-program-python)
- [Exercice 6 : Filter](#exercice-6--filter)
- [Exercice 7 : Dictionaries SoS](#exercice-7--dictionaries-sos)
</details>

## Introduction

- Bienvenue dans mon guide d'apprentissage de python_for_data_science. Ce document est destiné à capturer tout ce que j'apprends sur Python.
- Python 3.10 version

## Syntaxe de Base

### Liste

- **Liste** : Ce sont des structures de données qui permettent de stocker des éléments variés (nombres, chaînes de caractères, autres listes, objets, etc.)

  ```python
  # Liste mixte
  mixte = [1, "texte", 3.14, True]
  ```

### Tuple

- **Tuple** : Ce sont des structures de données qui permettent de stocker des éléments, mais contrairement aux listes, ils sont immuables.
  ```python
  # Tuple mixte
  mixte = (1, "texte", 3.14, True)
  ```

### Set

- **Set** : Ce sont des collections non ordonnées d'éléments uniques. Les doublons sont automatiquement supprimés.

  ```python
  # Set de nombres
  nombres = {1, 2, 3, 4, 5}

  # Set de chaînes de caractères
  fruits = {"pomme", "banane", "cerise"}

  # Set vide
  vide = set()
  ```

### Les dictionnaires

- **Les dictionnaires** : Ce sont des structures de données qui permettent de stocker des paires clé-valeur. Chaque clef dans un dictionnaire doit être unique et immuable.
  Les valeurs peuvent être de n'importe quel type et peuvent se répéter.

  ```python
  # Dictionnaire vide
  dictionnaire_vide = {}
  # Dictionnaire avec des valeurs initiales
  dictionnaire = {
     "nom": "Alice",
     "âge": 30,
     "profession": "Ingénieur"
  }
  ```

### Import

- **Import** est un mot clef utilisé pour inclure des modules ou des bibliothèques externes dans un script.(L'objectif principal de import est de rendre disponible dans un script les fonctions, classes, et variables définies dans d'autres modules ou bibliothèques.)

  - Importer un module entier. Accédez aux fonctions et classes

  ```python
  import math
  ```

  - Importer des éléments spécifiques d'un module. importe uniquement la fonction ou classe spécifique, permettant de l'utiliser directement sans préfixe.Mais peut causer des conflits de noms et rendre le code moins clair.

  ```python
  from math import sqrt
  ```

  - Utiliser un alias pour un module.

  ```python
  import numpy as np
  ```

### def

- **def** Ce mot clef indique à Python que vous définissez une nouvelle fonction.

  ```python
  def saluer(nom):
    print(f"Bonjour, {nom} !")
  ```

  Explication du code basique pour comprendre les fonctions en python

  - saluer : c'est le nom de la fonction
  - (nom) : Ce sont les paramètres de la fonction. ici il y en a un.
  - `:` : Le deux-points (:) indique la fin de l'en-tête de la fonction et le début du corps de la fonction.
  - Attention, en Python, il n'y a pas d'accolades : le code doit être indenté.
  - Réutilisabilité, Lisibilité, Modularité.

### in

- **in** L'opérateur in en Python permet de tester rapidement et facilement si une valeur est contenue dans une collection, comme une liste, un ensemble, ou un tuple. Cette méthode est efficace pour effectuer des recherches dans des collections de données.

  ```python
  # Définir un ensemble de types acceptés
  types_acceptes = {"list", "tuple", "set", "dict"}

  # Exemple de variable contenant le nom d'un type
  nom = "dict"

  # Vérifier si `nom` est dans l'ensemble `types_acceptes`
  if nom in types_acceptes:
      print(f"{nom} est dans l'ensemble.")
  else:
      print(f"{nom} n'est pas dans l'ensemble.")
  ```

## Starting

### Exercice 0 : First python script

**Objectif :** Vous devez modifier la chaîne de chaque objet de données pour afficher les salutations suivantes :
"Hello World", "Hello «pays de votre campus»", "Hello «ville de votre campus»", "Hello «nom de votre campus»". :

```python
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
#your code here
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
```

### Execute code

```bash
python3.10 "path"Hello.py
```

### Exercice 1 : First use of package

**Objectif :** Écrivez un script qui formate les dates de cette manière, bien sûr votre date ne sera pas la mienne comme dans l'exemple, mais elle doit être formatée de la même façon.

```bash
  $>python format_ft_time.py | cat -e
  Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
  Oct 21 2022$
  $>
```

### Execute code

```bash
python3.10 "path"format_ft_time.py
```

### Exercice 2 : First function python

**Objectif :**Écrivez une fonction qui affiche les types des objets et retourne 42.
</br>Voici comment elle devrait être prototypée:

```python
def all_thing_is_obj(object: any) -> int:
#your code here
```

Le testeur:

```python
from find_ft_type import all_thing_is_obj
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))
```

Résultat attendu:

```bash
$>python tester.py | cat -e
List : <class 'list'>$
Tuple : <class 'tuple'>$
Set : <class 'set'>$
Dict : <class 'dict'>$
Brian is in the kitchen : <class 'str'>$
Toto is in the kitchen : <class 'str'>$
Type not found$
42$
$>
```

### Execute code

```bash
python3.10 "path"tester.py "path"find_ft_type.py
```

### Exercice 3 : NULL not found

**Objectif :**Écrire une fonction qui affiche le type d'objet de tous les types de "Null". Retourner 0 si tout se passe correctement, ou 1 en cas d'erreur. Votre fonction doit afficher tous les types de "Null".
</br>Voici comment elle devrait être prototypée:

```python
def NULL_not_found(object: any) -> int:
#your code here
```

Le testeur:

```python
from NULL_not_found import NULL_not_found
Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
```

Résultat attendu:

```bash
$>python tester.py | cat -e
Nothing: None <class 'NoneType'>$
Cheese: nan <class 'float'>$
Zero: 0 <class 'int'>$
Empty: <class 'str'>$
Fake: False <class 'bool'>$
Type not Found$
1$
$>
```

### Exercice 4 : The Even and the Odd

**Objectif :**Créez un script qui prend un nombre en argument, vérifie s'il est impair ou pair, et affiche le résultat.
Si plus d'un argument est fourni ou si l'argument n'est pas un entier, affichez une AssertionError.
<br/>Résultat attendu:

```bash
$> python whatis.py 14
I'm Even.
$>
$> python whatis.py -5
I'm Odd.
$>
$> python whatis.py
$>
$> python whatis.py 0
I'm Even.
$>
$> python whatis.py Hi!
AssertionError: argument is not an integer
$>
$> python whatis.py 13 5
AssertionError: more than one argument is provided
$>
```

### Exercice 5 : First standalone program python

**Objectif :** Cette fois, vous devez créer un véritable programme autonome, avec une fonction main, qui prend un seul argument de type chaîne de caractères et affiche les sommes de ses caractères majuscules, minuscules, signes de ponctuation, chiffres et espaces.

- Si None ou rien n'est fourni, l'utilisateur est invité à fournir une chaîne de caractères.
- Si plus d'un argument est fourni au programme, afficher une AssertionError.
  <br/>Résultat attendu:

```bash
$>python building.py "Python 3.0, released in 2008, was a major revision that is not completely backwardcompatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
The text contains 171 characters:
2 upper letters
121 lower letters
8 punctuation marks
25 spaces
15 digits
$>
```

### Exercice 6 : Filter

Partie 1 : Recoder la fonction filter

Recoder votre propre fonction ft_filter ; elle doit se comporter comme la fonction intégrée originale (elle doit retourner la même chose que ce que renvoie print(filter.**doc**)). Vous devez utiliser des compréhensions de liste pour recoder votre ft_filter.

Partie 2 : Le programme
Créez un programme qui accepte deux arguments : une chaîne de caractères (S) et un entier (N). Le programme doit afficher une liste de mots extraits de S qui ont une longueur supérieure à N.

- Les mots sont séparés les uns des autres par des espaces.
- Les chaînes ne contiennent aucun caractère spécial (ponctuation ou caractères invisibles).
- Le programme doit contenir au moins une expression de compréhension de liste et une fonction lambda.
- Si le nombre d'arguments est différent de 2, ou si le type de l'un des arguments est incorrect, le programme affiche une erreur d'assertion (AssertionError).
  <br/>Résultat attendu:

```bash
$> python filterstring.py 'Hello the World' 4
['Hello', 'World']
$>
$> python filterstring.py 'Hello the World' 99
[]
$>
$> python filterstring.py 3 'Hello the World'
AssertionError: the arguments are bad
$>
$> python filterstring.py
AssertionError: the arguments are bad
$>

```

### Exercice 7 : Dictionaries SoS

Créez un programme qui prend une chaîne de caractères en argument et la code en code Morse.

- Le programme doit supporter les espaces et les caractères alphanumériques.
- Un caractère alphanumérique est représenté par des points . et des tirets -.
- Les caractères Morse complets sont séparés par un seul espace.
- Un caractère espace est représenté par une barre oblique /.
- Vous devez utiliser un dictionnaire pour stocker votre code Morse.

```python
NESTED_MORSE = { " ": "/ ",
"A": ".- ",
...
```

Si le nombre d'arguments est différent de 1, ou si le type de l'un des arguments est incorrect, le programme affiche une AssertionError.

```bash
$> python sos.py "sos" | cat -e
... --- ...$
$> python sos.py 'h$llo'
AssertionError: the arguments are bad
$>
```

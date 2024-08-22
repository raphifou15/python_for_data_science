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

<summary>3. <a href="#starting">Starting</a></summary>

- [Exercice 0 : First python script](#exercice-0--first-python-script)
- [Exercice 1 : First use of package](#exercice-1--first-use-of-package)
- [Exercice 2 : First use of package](#exercice-2--first-function-python)
- [Exercice 3 : NULL not found](#exercice-3--null-not-found)
- [Exercice 4 : The Even and the Odd](#exercice-4--the-even-and-the-odd)
- [Exercice 5 : First standalone program python](#exercice-5--first-standalone-program-python)
- [Exercice 6 : Filter](#exercice-6--filter)
- [Exercice 7 : Dictionaries SoS](#exercice-7--dictionaries-sos)
- [Exercice 8 : Loading](#exercice-8--loading)
- [Exercice 9 : My first package creation](#exercice-9--my-first-package-creation)
</details>

<details>

<summary>4. <a href="#array">Array</a></summary>

- [Exercice 0 : Give my BMI](#exercice-0--give-my-bmi)
- [Exercice 1 : 2D array](#exercice-1--2d-array)
- [Exercice 2 : load my image](#exercice-2--load-my-image)
- [Exercice 3 : zoom on me](#exercice-3--zoom-on-me)
- [Exercice 4 : rotate me](#exercice-4--rotate-me)
- [Exercice 5 : Pimp my image](#exercice-5--pimp-my-image)
</details>

<details>

<summary>5. <a href="#datatable">DataTable</a></summary>

- [Exercice 0 : Load my Dataset](#exercice-0--load-my-dataset)
- [Exercice 1 : Draw my country](#exercice-1--draw-my-country)
- [Exercice 2 : Compare my country](#exercice-2-compare-my-country)
- [Exercice 3 : Draw my year](#exercice-3-draw-my-year)

</details>

<details>

<summary>6. <a href="#oop">OOP</a></summary>

- [Exercice 0 : GOT S1E9](#exercice-0--got-s1e9)
- [Exercice 1 : GOT S1E7](#exercice-1--got-s1e7)
- [Exercice 2 : Now it’s weird!](#exercice-2---now-its-weird)
- [Exercice 3 : Calculate my vector](#exercice-3--calculate-my-vector)
- [Exercice 4 : Calculate my dot product](#exercice-4--calculate-my-dot-product)

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

### Exercice 8 : Loading

Alors, créons une fonction appelée ft_tqdm.
La fonction doit copier la fonction tqdm en utilisant l'opérateur yield
</br>Voici comment elle devrait être prototypée:

```python
def ft_tqdm(lst: range) -> None:
```

tester.py

```python
from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm
for elem in ft_tqdm(range(333)):
sleep(0.005)
print()
for elem in tqdm(range(333)):
sleep(0.005)
print()
```

Résultat attendu : (vous devez avoir une fonction aussi proche que possible de la version originale)

```bash
$> python tester.py
100%|[===============================================================>]| 333/333
100%| | 333/333 [00:01<00:00, 191.61it/s]
```

### Exercice 9 : My first package creation

Créez votre premier package en Python de la manière que vous souhaitez. Il apparaîtra dans la liste des packages installés lorsque vous tapez la commande pip list et affichera ses caractéristiques lorsque vous tapez pip show -v ft_package.

```bash
$>pip show -v ft_package
Name: ft_package
Version: 0.0.1
Summary: A sample test package
Home-page: https://github.com/eagle/ft_package
Author: eagle
Author-email: eagle@42.fr
License: MIT
Location: /home/eagle/...
Requires:
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
Entry-points:
$>
```

Le package sera installé via pip en utilisant l'une des commandes suivantes (les deux doivent fonctionner) :

- pip install ./dist/ft_package-0.0.1.tar.gz
- pip install ./dist/ft_package-0.0.1-py3-none-any.whl

<br/>Votre package doit pouvoir être appelé depuis un script comme celui-ci :

```bash
from ft_package import count_in_list
print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
```

## Array

### Exercice 0 : Give my BMI

**Objectif :** Votre fonction, give_bmi, prend en entrée 2 listes d'entiers ou de nombres à virgule flottante et renvoie une liste de valeurs de l'IMC (Indice de Masse Corporelle).

Votre fonction, apply_limit, accepte une liste d'entiers ou de nombres à virgule flottante et un entier représentant une limite comme paramètres. Elle renvoie une liste de booléens (True si le nombre dépasse la limite).

Vous devez gérer les cas d'erreur si les listes ne sont pas de la même taille, ne contiennent pas des entiers ou des nombres à virgule flottante, etc.
</br>Voici comment elle devrait être prototypée:

```python
def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
#your code here
def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
#your code here
```

testeur :

```python
from give_bmi import give_bmi, apply_limit
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
```

Résultat attendu :

```bash
$> python tester.py
[22.507863455018317, 29.0359168241966] <class 'list'>
[False, True]
$>
```

### Exercice 1 : 2D array

**Objectif :** Écrivez une fonction qui prend en paramètres un tableau 2D, affiche sa forme, et retourne une version tronquée du tableau en fonction des arguments de début et de fin fournis.
Vous devez utiliser la méthode de découpage (slicing).
Vous devez gérer les cas d'erreur si les listes ne sont pas de la même taille, ne sont pas une liste...
</br>Voici comment elle devrait être prototypée:

```python
def slice_me(family: list, start: int, end: int) -> list:
#your code here
```

testeur :

```python
from array2D import slice_me
family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
```

Résultat attendu :

```bash
$> python test_array2D.py
My shape is : (4, 2)
My new shape is : (2, 2)
[[1.8, 78.4], [2.15, 102.7]]
My shape is : (4, 2)
My new shape is : (1, 2)
[[2.15, 102.7]]
$>
```

### Exercice 2 : load my image

**Objectif :** Vous devez écrire une fonction qui charge une image, affiche son format et son contenu en pixels au format RGB.
Vous devez gérer, au moins, les formats JPG et JPEG.
Vous devez gérer toute erreur avec un message d'erreur clair.
</br>Voici comment elle devrait être prototypée:

```python
def ft_load(path: str) -> array: (you can return to the desired format)
#your code here
```

testeur :

```python
from load_image import ft_load
print(ft_load("landscape.jpg"))
```

Résultat attendu :

```bash
$> python tester.py
The shape of image is: (257, 450, 3)
[[[19 42 83]
[23 42 84]
[28 43 84]
...
[ 0 0 0]
[ 1 1 1]
[ 1 1 1]]]
$>
```

### Exercice 3 : zoom on me

**Objectif :** Créez un programme qui doit charger l'image "animal.jpeg", afficher certaines informations à son sujet et la montrer après l'avoir "agrandie".
• La taille en pixels sur les axes X et Y
• Le nombre de canaux
• Le contenu des pixels de l'image
• Afficher l'échelle sur les axes X et Y de l'image
Si quelque chose ne va pas, le programme ne doit pas s'arrêter brutalement et doit gérer toute erreur avec un message clair.

Résultat attendu :

```bash
$> python zoom.py
The shape of image is: (768, 1024, 3)
[[[120 111 132]
[139 130 151]
[155 146 167]
...
[120 156 94]
[119 154 90]
[118 153 89]]]
New shape after slicing: (400, 400, 1) or (400, 400)
[[[167]
[180]
[194]
...
[102]
[104]
[103]]]
$>
```

### Exercice 4 : rotate me

**Objectif :** Créez un programme qui doit charger l'image "animal.jpeg", découper une partie carrée de celle-ci, puis la transposer pour produire l'image ci-dessous. Le programme doit l'afficher, imprimer la nouvelle forme et les données de l'image après la transposition.

</br>Résultat attendu :

```bash
$> python rotate.py
The shape of image is: (400, 400, 1) or (400, 400)
[[[167]
[180]
[194]
...
[102]
[104]
[103]]]
New shape after Transpose: (400, 400)
[[167 180 194 ... 64 50 72]
...
[115 116 119 ... 102 104 103]]
$>
```

### Exercice 5 : Pimp my image

**Objectif** Tu dois développer 5 fonctions capables d'appliquer une variété de filtres de couleur aux images, tout en conservant la même forme pour l'image.

</br>Voici comment elles devraient être prototypée:

```python
def ft_invert(array) -> array:
#your code here
def ft_red(array) -> array:
#your code here
def ft_green(array) -> array:
#your code here
def ft_blue(array) -> array:
#your code here
def ft_grey(array)
```

Vous avez des opérateurs de restriction pour chaque fonction : (vous ne pouvez utiliser que ceux donnés, vous n'êtes pas obligé de tous les utiliser)

- invert : =, +, -, \*
- red : =, \*
- green : =, -
- blue : =
- grey : =, /"

testeur :

```bash
from load_image import ft_load
from pimp_image import ft_invert
...
array = ft_load("landscape.jpg")
ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)
print(ft_invert.__doc__)
```

</br>Résultat attendu :

```bash
$> python tester.py
The shape of image is: (257, 450, 3)
[[[19 42 83]
[23 42 84]
[28 43 84]
...
[ 0 0 0]
[ 1 1 1]
[ 1 1 1]]]
...
Inverts the color of the image received.
$>
```

## DataTable

### Exercice 0 : Load my Dataset

**Objectif** Créez une fonction qui prend un chemin en argument, écrit les dimensions de l'ensemble de données et les renvoie. Vous devez gérer les cas d'erreur et retourner None si le chemin est incorrect ou si le format est incorrect...

</br>Voici comment elle devrait être prototypée:

```python
def load(path: str) -> Dataset: (You have to adapt the type of return according to your library)
#your code here
```

testeur :

```python
from load_csv import load
print(load("life_expectancy_years.csv"))
```

</br>Résultat attendu :

```bash
$> python tester.py
Loading dataset of dimensions (195, 302)
country 1800 1801 1802 1803 ... 2096 2097 2098 2099 2100
Afghanistan 28.2 28.2 28.2 28.2 ... 76.2 76.4 76.5 76.6 76.8
...
$>
```

### Exercice 1 : Draw my country

**Objectif** Créez un programme qui appelle la fonction de chargement de l'exercice précédent, charge le fichier life_expectancy_years.csv, et affiche les informations du pays de votre campus. Votre graphique doit avoir un titre et une légende pour chaque axe.

### Exercice 2: Compare my country

**Objectif** Créez un programme qui appelle la fonction de chargement du premier exercice, charge le fichier population_total.csv, et affiche les informations sur le pays de votre campus par rapport à un autre pays de votre choix. Votre graphique doit avoir un titre, une légende pour chaque axe et une légende pour chaque courbe. Vous devez afficher les années de 1800 à 2050.

### Exercice 3: Draw my year

**Objectif** Créez un programme qui appelle la fonction de chargement du premier exercice, charge les fichiers income_per_person_gdppercapita_ppp_inflation_adjusted.csv et life_expectancy_years.csv, et affiche la projection de l'espérance de vie en relation avec le produit national brut de l'année 1900 pour chaque pays.
Votre graphique doit avoir un titre, une légende pour chaque axe, et une légende pour chaque courbe.
Vous devez afficher l'année 1900.

## OOP

### Exercice 0 : GOT S1E9

**Objectif** Créez une classe abstraite Character qui peut prendre un first_name comme premier paramètre, is_alive comme deuxième paramètre non obligatoire, par défaut à True, et qui peut changer l'état de santé du personnage avec une méthode qui passe is_alive de True à False.

Et une classe Stark qui hérite de Character.
</br>Voici comment elle devrait être prototypée:

```python
from abc import ABC, abstractmethod
class Character(ABC):
"""Your docstring for Class"""
@abstractmethod
#your code here
class Stark(Character):
"""Your docstring for C
```

testeur :

```python
from S1E9 import Character, Stark
Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)
```

</br>Résultat attendu :

```bash
$> python tester.py
{'first_name': 'Ned', 'is_alive': True}
True
False
Your docstring for Class
Your docstring for Constructor
Your docstring for Method
---
{'first_name': 'Lyanna', 'is_alive': False}
$>
```

testeur :

```python
from S1E9 import Character
hodor = Character("hodor")
```

</br>Résultat attendu :

```bash
TypeError: Can't instantiate abstract class Character with abstract method
```

### Exercice 1 : GOT S1E7

**Objectif** Créez deux familles qui héritent de la classe Character, que l'on peut instancier sans passer par la classe Character. Trouvez une solution pour que **str** et **repr** renvoient des chaînes de caractères et non des objets. Écrivez une méthode de classe pour créer des personnages en chaîne.

</br>Voici comment elle devrait être prototypée:

```python
from S1E9 import Character
class Baratheon(Character):
#your code here
class Lannister(Character):
#your code here
# decorator
def create_lannister(your code here):
```

testeur :

```python
from S1E7 import Baratheon, Lannister
Robert = Baratheon("Robert")
print(Robert.__dict__)
print(Robert.__str__)
print(Robert.__repr__)
print(Robert.is_alive)
Robert.die()
print(Robert.is_alive)
print(Robert.__doc__)
print("---")
Cersei = Lannister("Cersei")
print(Cersei.__dict__)
print(Cersei.__str__)
print(Cersei.is_alive)
print("---")
Jaine = Lannister.create_lannister("Jaine", True)
print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")
```

</br>Résultat attendu : (Les docstrings peuvent être différents)

```bash
$> python tester.py
{'first_name': 'Robert', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'brown', 'hairs': 'dark'}
<bound method Baratheon.__str__ of Vector: ('Baratheon', 'brown', 'dark')>
<bound method Baratheon.__repr__ of Vector: ('Baratheon', 'brown', 'dark')>
True
False
Representing the Baratheon family.
---
{'first_name': 'Cersei', 'is_alive': True, 'family_name': 'Lannister', 'eyes': 'blue', 'hairs': 'light'}
<bound method Lannister.__str__ of Vector: ('Lannister', 'blue', 'light')>
True
---
Name : ('Jaine', 'Lannister'), Alive : True
$>
```

### Exercice 2 - Now its weird

**Objectif**Dans cet exercice, vous allez créer un monstre : Joffrey Baratheon. C'est tellement risqué ! Il y a quelque chose d'incohérent avec ce nouveau « faux » roi. Vous devez utiliser les propriétés pour modifier les caractéristiques physiques de notre nouveau roi.

</br>Voici comment elle devrait être prototypée:

```python
from S1E7 import Baratheon, Lannister
class King(Baratheon, Lannister):
#your code here
```

testeur :

```python
from DiamondTrap import King
Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)
```

</br>Résultat attendu : (Les docstrings peuvent être différents)

```bash
$> python tester.py
{'first_name': 'Joffrey', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'brown', 'hair': 'dark'}
blue
light
{'first_name': 'Joffrey', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'blue', 'hairs': 'light'}
$>
```

### Exercice 3 : Calculate my vector

**Objectif**Écrivez une classe Calculatrice capable d'effectuer des calculs (addition, multiplication, soustraction, division) entre un vecteur et un scalaire.
</br>Voici comment elle devrait être prototypée:

```python
class calculator:
#your code here
def __add__(self, object) -> None:
#your code here
def __mul__(self, object) -> None:
#your code here
def __sub__(self, object) -> None:
#your code here
def __truediv__(self, object) -> None:
#your code here
```

testeur :

```python
from ft_calculator import calculator
v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5
Print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
Print("---")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 5
```

</br>Résultat attendu : (Les docstrings peuvent être différents)

```bash
$> python tester.py
[5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
---
[0.0, 5.0, 10.0, 15.0, 20.0, 25.0]
---
[5.0, 10.0, 15.0]
[1.0, 2.0, 3.0]
$>
```

### Exercice 4 : Calculate my dot product

**Objectif**Écrivez une classe de calculatrice capable d'effectuer des calculs (produit scalaire, addition, soustraction) sur 2 vecteurs. Les vecteurs auront toujours des tailles identiques, aucun traitement d'erreurs n'est requis.
À vous de trouver un décorateur qui vous permettra d'utiliser les méthodes de la classe de calculatrice sans instancier cette classe.

</br>Voici comment elle devrait être prototypée:

```python
class calculator:
#your code here
# decorator
def dotproduct(V1: list[float], V2: list[float]) -> None:
#your code here
# decorator
def add_vec(V1: list[float], V2: list[float]) -> None:
#your code here
# decorator
def sous_vec(V1: list[float], V2: list[float]) -> None:
#your code here
```

testeur :

```python
from ft_calculator import calculator
a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a,b)
calculator.add_vec(a,b)
calculator.sous_vec(a,b)

```

</br>Résultat attendu : (Les docstrings
peuvent être différents)

```
$> python tester.py
Dot product is: 56
Add Vector is : [7.0, 14.0, 5.0]
Sous Vector is: [3.0, 6.0, -1.0]
$>
```

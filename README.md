# python_for_data_science

## Table des Matières

1. [Introduction](#introduction)
2. [Syntaxe de Base](#syntaxe-de-base)
3. [Starting](#starting)
   - [Exercice 0 : First python script](#exercice-0--first-python-script)

## Introduction

- Bienvenue dans mon guide d'apprentissage de python_for_data_science. Ce document est destiné à capturer tout ce que j'apprends sur Python.
- Python 3.10 version

## Syntaxe de Base

- **Liste** : Ce sont des structures de données qui permettent de stocker des éléments variés (nombres, chaînes de caractères, autres listes, objets, etc.)

  ```python
  # Liste mixte
  mixte = [1, "texte", 3.14, True]
  ```

- **Tuple** : Ce sont des structures de données qui permettent de stocker des éléments, mais contrairement aux listes, ils sont immuables.
  ```python
  # Tuple mixte
  mixte = (1, "texte", 3.14, True)
  ```
- **Set** : Ce sont des collections non ordonnées d'éléments uniques. Les doublons sont automatiquement supprimés.

  ```python
  # Set de nombres
  nombres = {1, 2, 3, 4, 5}

  # Set de chaînes de caractères
  fruits = {"pomme", "banane", "cerise"}

  # Set vide
  vide = set()
  ```

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

# python_for_data_science

## Table des Matières

1. [Introduction](#introduction)
2. [Syntaxe de Base](#syntaxe-de-base)
3. [Starting](#starting)
   - [Exercice 0 : First python script](#exercice-0--first-python-script)

## Introduction

Bienvenue dans mon guide d'apprentissage de python_for_data_science. Ce document est destiné à capturer tout ce que j'apprends sur Python.

## Syntaxe de Base

## Starting

### Exercice 0 : First python script

**Objectif :** Modifier la chaîne de caractères de chaque objet de données pour afficher les salutations suivantes :

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

#### Solution

```python
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"
ft_tuple = ("Hello", "France!")
ft_set.update({"Paris!"})
ft_set.remove("tutu!")

ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
```

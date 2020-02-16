#!/usr/bin/env python3
"""
Corrigé de l'exercice 2 de la leçon 8.

IMPORTANT: il y a autant de façon de réaliser correctement l'exercice que de programmeurs ; ce n'est pas grave si vous
n'avez pas exactement le même code!

Dans ce corrigé on peut voir 3 méthodes différentes pour aboutir au même résultat. Il en existe d'autres!

Afficher:
coucou c'est gabriel
coucou c'est jean
coucou c'est paul

"""

# Début du programme

# création d'une liste de prénoms
prenoms = ["gabriel", "jean", "paul"]

# méthode 1
print("-- méthode 1 --")
# boucle sur tous les prénoms de la liste
for p in prenoms:
    # p contient un prénom, on l'affiche
    print(f"coucou c'est {p}")

# méthode 2
print("-- méthode 2 --")
# boucle de 0 à 2
for i in range(3):
    # i est un nombre entre 0 et 2, on peut l'utiliser comme indice dans la liste
    p = prenoms[i]
    # p contient un prénom, on l'affiche
    print(f"coucou c'est {p}")

# méthode 3
print("-- méthode 3 --")
# boucle de 0 à 2
indice = 0
while indice < 3:
    # indice est un nombre entre 0 et 2
    p = prenoms[indice]
    # p contient un prénom, on l'affiche
    print(f"coucou c'est {p}")
    # ajouter 1 à notre indice
    indice = indice + 1

# Fin du programme

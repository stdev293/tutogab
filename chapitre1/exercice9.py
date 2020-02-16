#!/usr/bin/env python3
"""
Corrigé de l'exercice leçon 9.

IMPORTANT: il y a autant de façon de réaliser correctement l'exercice que de programmeurs ; ce n'est pas grave si vous
n'avez pas exactement le même code!

"""


# Définition d'une fonction pour afficher un prénom et le nombre de jeux
def affiche_jeux(personne, n):
    """
    Arguments:
    personne: nom de la personne
    n: nombre de jeux qu'elle possède

    Cette fonction affiche:
    "Bob a 5 jeux vidéos. Quelle chance!" si n est 2 ou plus
    "Bob a 1 jeu vidéo." sinon
    """
    if n > 1:
        print(f"{personne} a {n} jeux vidéos. Quelle chance!")
    else:
        print(f"{personne} a {n} jeu vidéo.")


# Début du programme

# on met les valeurs de la consigne de l'exercice dans deux listes:
noms = ["Anna", "Eric", "Julie", "Terry"]
jeux = [1, 5, 8, 0]

# boucle sur un indice parcourant toute la longueur de la liste 'noms'
for ind in range(len(noms)):
    # on prend le nom et le nombre de jeux correspondant à notre indice
    nom = noms[ind]
    nombre = jeux[ind]
    # plus qu'à afficher, notre fonction s'en charge
    affiche_jeux(nom, nombre)

# Fin du programme

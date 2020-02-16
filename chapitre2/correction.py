#!/usr/bin/env python3

import pygame

# Paramètres de la grille

# Définition des textures pour les tuiles de la grille
TX_N = pygame.image.load('./chapitre2/textures/dirt.png')  # sol nu
TX_H = pygame.image.load('./chapitre2/textures/grass.png')  # herbe
TX_E = pygame.image.load('./chapitre2/textures/water.png')  # eau
TX_M = pygame.image.load('./chapitre2/textures/wall.png')  # mur
# Remplissage de la grille (6*4)
G_LARGEUR = 20  # largeur ou nombre de colonnes
G_HAUTEUR = 10  # hauteur ou nombre de lignes
TAILLE_T_PIX = 50  # Taille qu'on veut donner à chaque case de la grille, en pixels
GRILLE = [
    [TX_H, TX_H, TX_H, TX_H, TX_N, TX_N, TX_H, TX_H, TX_H, TX_H, TX_N, TX_N, TX_N, TX_H, TX_H, TX_H, TX_N, TX_N, TX_H, TX_M],
    [TX_H, TX_H, TX_H, TX_H, TX_N, TX_N, TX_H, TX_H, TX_H, TX_H, TX_N, TX_N, TX_N, TX_H, TX_H, TX_H, TX_N, TX_N, TX_H, TX_M],
    [TX_H, TX_H, TX_H, TX_H, TX_N, TX_N, TX_H, TX_H, TX_H, TX_E, TX_E, TX_E, TX_N, TX_N, TX_N, TX_H, TX_N, TX_N, TX_H, TX_M],
    [TX_H, TX_H, TX_H, TX_H, TX_N, TX_N, TX_H, TX_H, TX_N, TX_E, TX_E, TX_E, TX_E, TX_N, TX_H, TX_N, TX_N, TX_N, TX_H, TX_M],
    [TX_H, TX_H, TX_H, TX_H, TX_N, TX_N, TX_N, TX_E, TX_E, TX_E, TX_E, TX_E, TX_E, TX_E, TX_H, TX_N, TX_N, TX_N, TX_H, TX_M],
    [TX_H, TX_H, TX_H, TX_H, TX_H, TX_N, TX_N, TX_E, TX_E, TX_E, TX_E, TX_E, TX_E, TX_E, TX_N, TX_N, TX_N, TX_N, TX_H, TX_M],
    [TX_M, TX_H, TX_H, TX_H, TX_H, TX_N, TX_N, TX_N, TX_E, TX_E, TX_E, TX_E, TX_E, TX_E, TX_H, TX_N, TX_N, TX_N, TX_H, TX_M],
    [TX_M, TX_H, TX_H, TX_H, TX_H, TX_H, TX_N, TX_N, TX_H, TX_E, TX_E, TX_E, TX_E, TX_E, TX_H, TX_N, TX_N, TX_N, TX_H, TX_M],
    [TX_M, TX_H, TX_H, TX_H, TX_H, TX_H, TX_H, TX_H, TX_H, TX_E, TX_E, TX_E, TX_E, TX_E, TX_E, TX_N, TX_N, TX_N, TX_H, TX_M],
    [TX_M, TX_M, TX_M, TX_H, TX_H, TX_H, TX_H, TX_H, TX_H, TX_H, TX_E, TX_E, TX_E, TX_E, TX_H, TX_H, TX_N, TX_N, TX_H, TX_M],
]  # Cette grille représente un tableau. Dans chacune des 10 lignes on a mis 20 textures (une par colonne)

# Début du programme
# initialisation
pygame.init()
# on définit le titre de la fenêtre
pygame.display.set_caption("MON SUPER JEU!")

# initialiser l’affichage ici (voir le paragraphe suivant)
taille_ecran = (G_LARGEUR*TAILLE_T_PIX, G_HAUTEUR*TAILLE_T_PIX)
surface = pygame.display.set_mode(taille_ecran)

# boucle principale
game_over = False
while not game_over:
    # Remplir la grille
    for ligne in range(G_HAUTEUR):
        for colonne in range(G_LARGEUR):
            # calculer la position où doit s'afficher la texture
            position_texture = (colonne * TAILLE_T_PIX, ligne * TAILLE_T_PIX)
            # dessiner la bonne texture au bon endroit
            surface.blit(GRILLE[ligne][colonne], position_texture)

    # déplacer les personnages ici, etc.
    # ...

    # dire à pygame de mettre à jour l’écran
    pygame.display.update()

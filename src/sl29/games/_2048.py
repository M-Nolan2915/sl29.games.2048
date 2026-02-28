"""Module providing the logic of the 2048 game"""

import random
import copy
from typing import List, Tuple

TAILLE:int = 4


# ==========================================================
# 🎯 FONCTION PUBLIQUE (API POUR L’INTERFACE)
# ==========================================================

def nouvelle_partie() -> Tuple[List[List[int]], int]:
    """
    Crée une nouvelle partie du jeu 2048.

    :return: Une grille TAILLExTAILLE initialisée avec deux tuiles, ainsi que le score à 0.
    :rtype: Tuple[List[List[int]], int]
    """
    
    plateau =_creer_plateau_vide()
    plateau1=_ajouter_tuile(plateau)
    plateau2=_ajouter_tuile(plateau1)
    return (plateau2,0)

def jouer_coup(plateau: List[List[int]], direction: str) -> tuple[List[List[int]], int, bool]:
    """
    Effectuer un mouvement sur le plateau.

    :param plateau: Une grille TAILLExTAILLE du jeu.
    :type plateau: List[List[int]]
    :param direction: La direction du déplacement : 'g' (gauche), 'd' (droite), 'h' (haut), 'b' (bas).
    :type direction: str
    :return: Retourne un tuple (nouveau_plateau, points, est_fini).
    :rtype: tuple[List[List[int]], int, bool]
    """
    
    ancien_plateau = [ligne[:] for ligne in plateau]


    if direction == 'g':
        nouveau_plateau, points = _deplacer_gauche(plateau)
    elif direction == 'd':
        nouveau_plateau, points = _deplacer_droite(plateau)
    elif direction == 'h':
        nouveau_plateau, points = _deplacer_haut(plateau)
    elif direction == 'b':
        nouveau_plateau, points = _deplacer_bas(plateau)
    else:
        raise ValueError(f"Direction inconnue : {direction}")
    
    
    if nouveau_plateau != ancien_plateau:
        nouveau_plateau = _ajouter_tuile(nouveau_plateau)


    # Vérifier si le jeu est fini : aucun déplacement possible
    est_fini = True
    for d in ['g', 'd', 'h', 'b']:
        if d == 'g':
            p, _ = _deplacer_gauche(nouveau_plateau)
        elif d == 'd':
            p, _ = _deplacer_droite(nouveau_plateau)
        elif d == 'h':
            p, _ = _deplacer_haut(nouveau_plateau)
        else:
            p, _ = _deplacer_bas(nouveau_plateau)
        if p != nouveau_plateau:
            est_fini = False
            break

    return nouveau_plateau, points, est_fini
# ==========================================================
# 🔒 FONCTIONS PRIVÉES (LOGIQUE INTERNE)
# ==========================================================

def _creer_plateau_vide() -> List[List[int]]:
    """
    Crée une grille TAILLExTAILLE remplie de zéros.
    :return: Une grille vide.
    :rtype: List[List[int]]
    """
    
    return [[0 for _ in range(TAILLE)] for _ in range (TAILLE)]

    
def _get_cases_vides(plateau: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Retourne les coordonnées des cases vides sous forme d'une liste de coordonnées

    :param plateau: La grille actuelle.
    :type plateau: List[List[int]]
    :return: Une liste de coordonnées
    :rtype: List[Tuple[int,pip install -e .[dev,test,doc] int]]
    """
    result= []
    for i in range(len(plateau)):
        for j in range(len(plateau)):
            if plateau [i][j] == 0 :
                result.append((i,j))
    return result



def _ajouter_tuile(plateau: List[List[int]]) -> List[List[int]]:
    """
    Ajoute une tuile de valeur 2 sur une case vide.

    :param plateau: La grille actuelle.
    :type plateau: List[List[int]]
    :return: Une nouvelle grille avec une tuile ajoutée.
    :rtype: List[List[int]]
    """
   
    new_plateau=copy.deepcopy(plateau)
    cases_vides=_get_cases_vides(new_plateau)
    (i,j)=random.choice(cases_vides)
    new_plateau[i][j]=2
    return new_plateau
    

def _supprimer_zeros(ligne: List[int]) -> List[int]:
    """
    Supprime les zéros d'une ligne.

    :param ligne: Une ligne de la grille.
    :type ligne: List[int]
    :return: La ligne sans zéros.
    :rtype: List[int]
    """
    supprimer_zero =[ ]

    for valeur in ligne:
        if valeur != 0:
            supprimer_zero.append(valeur)
    return supprimer_zero

def _fusionner(ligne: List[int]) -> Tuple[List[int], int]:
    """
    Fusionne les valeurs identiques consécutives d'une ligne.

    :param ligne: Une ligne sans zéros.
    :type ligne: List[int]
    :return: La ligne après fusion, les points gagnés
    :rtype: Tuple[List[int], int]
    """
    liste_fusionnee = []
    i = 0
    score = 0
    while i < len(ligne):
        if i+1 < len(ligne)  and ligne [i]  == ligne [i+1]:
            fusion =ligne [i] +ligne [i+1]
            score = score +  fusion
            liste_fusionnee.append(fusion)
            i = i+2
        else :
            liste_fusionnee.append(ligne[i])
            i = i+1
    return liste_fusionnee,score


def _completer_zeros(ligne): # ajouter les annotations de type
    """
    D
    """
    while len(ligne) < TAILLE:
        ligne.append(0)
    return ligne





def _deplacer_gauche(plateau) : # ajouter les annotations de type
    """
    DOCSTRING À ÉCRIRE
    """
    nouveau_plateau5 = []
    nouveaux_points = 0.
    for ligne in plateau:
        ligne_sans_zeros = _supprimer_zeros(ligne)
        ligne_fusionnee,score = _fusionner(ligne_sans_zeros)
        nouveaux_points =  nouveaux_points+score
        ligne_finale = _completer_zeros(ligne_fusionnee)
        nouveau_plateau5.append(ligne_finale)
    return nouveau_plateau5,nouveaux_points
def _inverser_lignes(plateau): # ajouter les annotations de type
    """
    DOCSTRING À ÉCRIRE
    """
    result =[]
    for ligne in plateau:
        result.append(ligne[::-1])
    return result

def _deplacer_droite(plateau: List[List[int]]) -> Tuple[List[List[int]], int]:
    """
    Déplace les tuiles vers la droite en fusionnant les valeurs identiques.

    :param plateau: La grille actuelle du jeu.
    :type plateau: List[List[int]]
    :return: Un tuple contenant la nouvelle grille après déplacement et les points gagnés.
    :rtype: Tuple[List[List[int]], int]
    """
    
    plateau_inverser = _inverser_lignes(plateau)
    plateau_inverser_gauche,score= _deplacer_gauche(plateau_inverser)
    plateau_inverser_gauche_inverser = _inverser_lignes(plateau_inverser_gauche)
   
    return  plateau_inverser_gauche_inverser,score



def _transposer(plateau): # ajouter les annotations de type

    """
    Retourne la transposée du plateau.

    Le contenu de la case (i, j) devient
    le contenu de la case (j, i).


    """
    if not isinstance(plateau, list):
        raise ValueError("Le plateau doit être une liste de listes")
    for i, ligne in enumerate(plateau):
        if not isinstance(ligne, list):
            raise ValueError(f"La ligne {i} du plateau n'est pas une liste: {ligne}")
    
    transposed = []
    for colonne in zip(*plateau):
        nouvelle_ligne = list(colonne)
        transposed.append(nouvelle_ligne)
    
    return transposed

def _deplacer_haut(plateau: List[List[int]]) -> Tuple[List[List[int]], int]:
    """
    Déplace les tuiles vers le haut en fusionnant les valeurs identiques.

    :param plateau: La grille actuelle du jeu.
    :return: Un tuple contenant la nouvelle grille après déplacement et les points gagnés.
    """
    """Déplace toutes les tuiles vers le haut."""

   
    # 1️⃣ Transposer la grille pour traiter les colonnes comme des lignes
    plateau_transpose = _transposer(plateau)

    # 2️⃣ Déplacer chaque "ligne transposée" vers la gauche
    plateau_deplace, score = _deplacer_gauche(plateau_transpose)

    # 3️⃣ Re-transposer pour revenir à la grille originale
    plateau_final = _transposer(plateau_deplace) 

    return plateau_final, score

def _deplacer_bas(plateau: List[List[int]]) -> Tuple[List[List[int]], int]:
    """
    Déplace les tuiles vers le bas en fusionnant les valeurs identiques.

    :param plateau: La grille actuelle du jeu.
    :return: Un tuple contenant la nouvelle grille après déplacement et les points gagnés.
    """
     # 1️⃣ Transposer la grille pour traiter les colonnes comme des lignes
    plateau_transpose = _transposer(plateau)

    # 2️⃣ Déplacer chaque "ligne transposée" vers la gauche
    plateau_deplace, score = _deplacer_droite(plateau_transpose)

    # 3️⃣ Re-transposer pour revenir à la grille originale
    plateau_final = _transposer(plateau_deplace) 

    return plateau_final, score

def _partie_terminee(plateau: List[List[int]]) -> bool:
    """
   
    Détermine si la partie est terminée.

    Une partie est finie si :
    1. Il n'y a plus de cases vides dans la grille.
    2. Aucune fusion possible n'existe dans les lignes ou les colonnes.

    :param plateau: La grille du jeu (liste de listes d'entiers)
    :return: True si la partie est terminée, False sinon
    :rtype: bool
    """
    if _get_cases_vides(plateau):
        return False

    taille = len(plateau)

    # Vérifier les fusions horizontales
    for ligne in plateau:
        for i in range(taille - 1):
            if ligne[i] == ligne[i + 1]:
                return False

    # Vérifier les fusions verticales
    for j in range(taille):
        for i in range(taille - 1):
            if plateau[i][j] == plateau[i + 1][j]:
                return False

    return True
"""
Module data_utils : fonctions mathématiques et statistiques de base.

Toutes les fonctions sont écrites "à la main" (sans le module math ni
statistics) pour s'entraîner à manipuler les boucles et les listes.
"""

# --- Constantes -------------------------------------------------------------
PI = 3.141592653589793   # nombre pi
E = 2.718281828459045    # nombre d'Euler (base du logarithme népérien)


# --- Fonctions de base ------------------------------------------------------
def carre(x):
    """Renvoie le carré de x (x * x)."""
    return x * x


def cube(x):
    """Renvoie le cube de x (x * x * x)."""
    return x * x * x


def factorielle(n):
    """
    Renvoie la factorielle de n (n! = 1 * 2 * ... * n).

    Paramètre : n (int >= 0)
    Retour    : int (par convention, 0! = 1)
    """
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour un nombre négatif.")
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat


def valeur_absolue(x):
    """Renvoie la valeur absolue de x (x sans son signe)."""
    if x < 0:
        return -x
    return x


# --- Fonctions statistiques sur une liste -----------------------------------
def maximum(liste):
    """Renvoie le plus grand élément d'une liste non vide."""
    plus_grand = liste[0]
    for valeur in liste:
        if valeur > plus_grand:
            plus_grand = valeur
    return plus_grand


def minimum(liste):
    """Renvoie le plus petit élément d'une liste non vide."""
    plus_petit = liste[0]
    for valeur in liste:
        if valeur < plus_petit:
            plus_petit = valeur
    return plus_petit


def moyenne(liste):
    """Renvoie la moyenne arithmétique d'une liste non vide (somme / nombre d'éléments)."""
    total = 0
    for valeur in liste:
        total += valeur
    return total / len(liste)


def ecart_type(liste):
    """
    Renvoie l'écart-type (de population) d'une liste non vide :
    racine carrée de la moyenne des carrés des écarts à la moyenne.
    """
    m = moyenne(liste)
    somme_ecarts = 0
    for valeur in liste:
        somme_ecarts += (valeur - m) ** 2
    variance = somme_ecarts / len(liste)
    return variance ** 0.5   # puissance 0.5 = racine carrée


def mediane(liste):
    """
    Renvoie la médiane d'une liste non vide : la valeur centrale une fois
    la liste triée (ou la moyenne des deux valeurs centrales si la taille est paire).
    """
    triee = sorted(liste)          # sorted() ne modifie pas la liste d'origine
    n = len(triee)
    milieu = n // 2
    if n % 2 == 1:                 # nombre impair d'éléments
        return triee[milieu]
    return (triee[milieu - 1] + triee[milieu]) / 2

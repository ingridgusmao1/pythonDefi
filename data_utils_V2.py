"""
Module data_utils_V2 : nouvelle version du module data_utils.

Il reprend tout le contenu de data_utils (constantes et fonctions de base)
et ajoute de nouvelles fonctions de manipulation de listes et de dictionnaires.
"""

# On récupère tout ce qui existe déjà dans la V1 (PI, E, carre, cube, ...)
from data_utils import *


def somme_cumulee(liste):
    """
    Calcule la somme cumulée d'une liste de nombres.

    Paramètre : liste (list de nombres)
    Retour    : list, où chaque élément est la somme des éléments
                précédents + l'élément courant.
    Exemple   : [1, 2, 3, 4] -> [1, 3, 6, 10]
    """
    resultat = []
    total = 0
    for valeur in liste:
        total += valeur
        resultat.append(total)
    return resultat


def compter_occurrences(liste):
    """
    Compte le nombre d'apparitions de chaque élément d'une liste.

    Paramètre : liste (list)
    Retour    : dict {élément: nombre d'occurrences}
    Exemple   : [1, 2, 2, 3] -> {1: 1, 2: 2, 3: 1}
    """
    compteur = {}
    for element in liste:
        # get() renvoie 0 si la clé n'existe pas encore
        compteur[element] = compteur.get(element, 0) + 1
    return compteur


def inverser_dict(dictionnaire):
    """
    Inverse les clés et les valeurs d'un dictionnaire.

    Paramètre : dictionnaire (dict) dont les valeurs sont hachables et uniques
    Retour    : dict {valeur: clé}
    Exemple   : {'a': 1, 'b': 2} -> {1: 'a', 2: 'b'}
    Attention : si deux clés ont la même valeur, seule la dernière est conservée.
    """
    inverse = {}
    for cle, valeur in dictionnaire.items():
        inverse[valeur] = cle
    return inverse


def filtrer_pairs(liste):
    """
    Garde uniquement les nombres pairs d'une liste.

    Paramètre : liste (list d'entiers)
    Retour    : nouvelle list contenant les nombres pairs
    Exemple   : [1, 2, 3, 4] -> [2, 4]
    """
    pairs = []
    for nombre in liste:
        if nombre % 2 == 0:      # reste de la division par 2 nul => pair
            pairs.append(nombre)
    return pairs


def celsius_to_fahrenheit(celsius):
    """
    Convertit une température de degrés Celsius en degrés Fahrenheit.

    Paramètre : celsius (int ou float)
    Retour    : float, selon la formule F = C * 9/5 + 32
    Exemple   : 0 -> 32.0
    """
    return celsius * 9 / 5 + 32


def trouver_doublons(liste):
    """
    Trouve les éléments qui apparaissent plus d'une fois dans une liste.

    Paramètre : liste (list)
    Retour    : list des éléments en double (chacun une seule fois,
                dans l'ordre de leur première apparition)
    Exemple   : [1, 2, 2, 3, 3] -> [2, 3]
    """
    occurrences = compter_occurrences(liste)
    doublons = []
    for element, nombre in occurrences.items():
        if nombre > 1:
            doublons.append(element)
    return doublons


def calculer_moyenne_ponderee(valeurs, poids):
    """
    Calcule la moyenne pondérée d'une liste de valeurs.

    Paramètres : valeurs (list de nombres), poids (list de nombres, même longueur)
    Retour     : float = somme(valeur * poids) / somme(poids), arrondi à 2 décimales
    Exemple    : valeurs [3, 5], poids [1, 2] -> (3*1 + 5*2) / 3 = 4.33
    """
    if len(valeurs) != len(poids):
        raise ValueError("Les listes 'valeurs' et 'poids' doivent avoir la même longueur.")
    somme_ponderee = 0
    somme_poids = 0
    for v, p in zip(valeurs, poids):   # zip parcourt les deux listes en parallèle
        somme_ponderee += v * p
        somme_poids += p
    return round(somme_ponderee / somme_poids, 2)


# --- Partie bonus -----------------------------------------------------------
def analyser_texte(texte):
    """
    Analyse une chaîne de caractères.

    Paramètre : texte (str)
    Retour    : dict contenant :
        - 'nombre_mots'                : nombre total de mots
        - 'nombre_caracteres'          : nombre de caractères, espaces inclus
        - 'nombre_caracteres_sans_esp' : nombre de caractères, espaces exclus
        - 'mot_le_plus_long'           : le mot le plus long (sans ponctuation)
        - 'longueur_moyenne_mots'      : longueur moyenne des mots (2 décimales)
    """
    mots = texte.split()                                   # découpe sur les espaces
    # On retire la ponctuation collée aux mots (ex : "apprendre." -> "apprendre")
    mots_propres = [mot.strip(".,;:!?«»()\"") for mot in mots]

    mot_le_plus_long = ""
    total_lettres = 0
    for mot in mots_propres:
        total_lettres += len(mot)
        if len(mot) > len(mot_le_plus_long):
            mot_le_plus_long = mot

    return {
        "nombre_mots": len(mots),
        "nombre_caracteres": len(texte),
        "nombre_caracteres_sans_esp": len(texte.replace(" ", "")),
        "mot_le_plus_long": mot_le_plus_long,
        "longueur_moyenne_mots": round(total_lettres / len(mots), 2),
    }

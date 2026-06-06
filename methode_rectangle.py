# Bibliothèque permettant de manipuler efficacement
# les tableaux numériques.
import numpy as np

# Fonction utilisée pour calculer une valeur de référence
# très précise de l'intégrale.
from scipy.integrate import quad

# Bibliothèque permettant de mesurer
# les temps d'exécution.
import timeit

# Bibliothèque utilisée pour tracer
# les graphiques de convergence et de performance.
import matplotlib.pyplot as plt


# ==========================================================
# MÉTHODE DES RECTANGLES - PYTHON DE BASE
# ==========================================================

def rectangle_python_classique(p1, p2, p3, p4, a, b, n):

    # Calcul de la largeur de chaque rectangle.
    taille_intervalle = (b - a) / n

    # Liste utilisée pour stocker les valeurs de la fonction.
    valeur_y = []

    # Variable qui accumulera la valeur de l'intégrale.
    integrale = 0

    # Parcours de tous les rectangles.
    for i in range(n):

        # Calcul de la valeur de la fonction
        # au centre du rectangle.
        valeur_y.append(
            calculer_valeur_y(
                p1,
                p2,
                p3,
                p4,
                a + taille_intervalle / 2 + i * taille_intervalle
            )
        )

        # Hauteur du rectangle calculée au point milieu.
        hauteur_rectangle = calculer_valeur_y(
            p1,
            p2,
            p3,
            p4,
            a + taille_intervalle / 2 + i * taille_intervalle
        )

        # Aire du rectangle ajoutée à l'intégrale.
        integrale += hauteur_rectangle * taille_intervalle

    return integrale


# ==========================================================
# CALCUL DE LA VALEUR DU POLYNÔME
# ==========================================================

def calculer_valeur_y(p1, p2, p3, p4, x):

    # Évaluation du polynôme :
    # f(x) = p1 + p2*x + p3*x² + p4*x³
    return p1 + p2 * x + p3 * x**2 + p4 * x**3


# ==========================================================
# CALCUL DE L'ERREUR D'INTÉGRATION
# ==========================================================

def erreur_integration(p1, p2, p3, p4, a, b, n):

    # Calcul de la solution de référence avec SciPy.
    resultat_analytique, erreur = quad(
        lambda x: calculer_valeur_y(p1, p2, p3, p4, x),
        a,
        b
    )

    print(f"Le résultat analytique est de : {resultat_analytique}")

    # Calcul de l'erreur relative.
    erreur_integrale = abs(
        rectangle_numpy(
            p1,
            p2,
            p3,
            p4,
            a,
            b,
            n
        ) - resultat_analytique
    ) / resultat_analytique

    print(f"L'erreur est de {erreur_integrale}")

    return erreur_integrale
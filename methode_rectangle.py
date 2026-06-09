# Bibliothèque permettant de manipuler efficacement
# les tableaux numériques.
import numpy as np

# Bibliothèque permettant de mesurer précisément
# le temps d'exécution des fonctions.
import timeit

# Bibliothèque utilisée pour tracer les graphiques
# de convergence et de temps d'exécution.
import matplotlib.pyplot as plt


# ==========================================================
# 1. DÉFINITION DU POLYNÔME
# ==========================================================

def calculer_valeur_y(p1, p2, p3, p4, x):
    """
    Calcule la valeur du polynôme :
    f(x) = p1 + p2*x + p3*x² + p4*x³.
    """

    return p1 + p2 * x + p3 * x**2 + p4 * x**3


# ==========================================================
# 2. SOLUTION ANALYTIQUE EXACTE
# ==========================================================

def solution_analytique(p1, p2, p3, p4, a, b):
    """
    Calcule la solution exacte de l'intégrale
    en utilisant la primitive analytique du polynôme.

    La primitive de :
    f(x) = p1 + p2*x + p3*x² + p4*x³

    est :
    F(x) = p1*x + (p2/2)*x² + (p3/3)*x³ + (p4/4)*x⁴
    """

    def primitive(x):
        return (
            p1 * x
            + (p2 / 2) * x**2
            + (p3 / 3) * x**3
            + (p4 / 4) * x**4
        )

    return primitive(b) - primitive(a)


# ==========================================================
# 3. MÉTHODE DES RECTANGLES - PYTHON DE BASE
# ==========================================================

def rectangle_python_classique(p1, p2, p3, p4, a, b, n):
    """
    Calcule l'intégrale numérique avec la méthode
    des rectangles en Python de base.

    La fonction est évaluée au centre de chaque segment.
    """

    # Largeur de chaque segment.
    taille_intervalle = (b - a) / n

    # Variable qui accumule la somme des aires.
    integrale = 0.0

    # Parcours des n rectangles.
    for i in range(n):

        # Point milieu du rectangle courant.
        x_milieu = a + taille_intervalle / 2 + i * taille_intervalle

        # Hauteur du rectangle.
        hauteur_rectangle = calculer_valeur_y(
            p1,
            p2,
            p3,
            p4,
            x_milieu
        )

        # Aire du rectangle ajoutée à la somme totale.
        integrale += hauteur_rectangle * taille_intervalle

    return integrale


# ==========================================================
# 4. MÉTHODE DES RECTANGLES - VERSION NUMPY
# ==========================================================

def rectangle_numpy(p1, p2, p3, p4, a, b, n):
    """
    Calcule l'intégrale numérique avec la méthode
    des rectangles en utilisant NumPy.

    Cette version est vectorisée afin d'éviter une boucle Python.
    """

    # Largeur de chaque segment.
    taille_intervalle = (b - a) / n

    # Création des points milieux de tous les segments.
    x = np.linspace(
        a + taille_intervalle / 2,
        b - taille_intervalle / 2,
        n
    )

    # Calcul vectorisé de l'aire totale.
    integrale = np.sum(
        calculer_valeur_y(p1, p2, p3, p4, x) * taille_intervalle
    )

    return integrale


# ==========================================================
# 5. CALCUL DES ERREURS
# ==========================================================

def erreur_rectangle_python(p1, p2, p3, p4, a, b, n):
    """
    Calcule l'erreur absolue de la méthode
    des rectangles en Python de base.
    """

    exact = solution_analytique(p1, p2, p3, p4, a, b)
    numerique = rectangle_python_classique(p1, p2, p3, p4, a, b, n)

    return abs(exact - numerique)


def erreur_rectangle_numpy(p1, p2, p3, p4, a, b, n):
    """
    Calcule l'erreur absolue de la méthode
    des rectangles avec NumPy.
    """

    exact = solution_analytique(p1, p2, p3, p4, a, b)
    numerique = rectangle_numpy(p1, p2, p3, p4, a, b, n)

    return abs(exact - numerique)


# ==========================================================
# 6. ÉTUDE DE CONVERGENCE
# ==========================================================

def tracer_courbe_convergence_rectangle(p1, p2, p3, p4, a, b, valeur_n):
    """
    Trace la convergence de la méthode des rectangles.

    L'objectif est de vérifier que l'erreur diminue lorsque
    le nombre de segments augmente.
    """

    erreurs_python = []
    erreurs_numpy = []

    for n_test in valeur_n:

        erreurs_python.append(
            erreur_rectangle_python(p1, p2, p3, p4, a, b, n_test)
        )

        erreurs_numpy.append(
            erreur_rectangle_numpy(p1, p2, p3, p4, a, b, n_test)
        )

        print(f"La valeur de n est de {n_test}")

    plt.figure()

    plt.loglog(
        valeur_n,
        erreurs_python,
        "o-",
        label="Rectangle Python"
    )

    plt.loglog(
        valeur_n,
        erreurs_numpy,
        "s-",
        label="Rectangle NumPy"
    )

    plt.xlabel("Nombre de rectangles n")
    plt.ylabel("Erreur absolue")
    plt.title("Convergence de la méthode des rectangles")

    plt.grid(True)
    plt.legend()

    plt.show()


# ==========================================================
# 7. COMPARAISON DES TEMPS D'EXÉCUTION
# ==========================================================

def tracer_courbe_temps_execution(p1, p2, p3, p4, a, b, valeur_n):
    """
    Trace le temps d'exécution de la méthode des rectangles.

    Pour chaque valeur de n, on mesure le temps moyen
    d'exécution des versions Python et NumPy.
    """

    temps_python_classique = []
    temps_numpy = []

    for n_test in valeur_n:

        # Mesure du temps pour la version Python classique.
        temps_python_classique.append(
            timeit.timeit(
                lambda: rectangle_python_classique(
                    p1,
                    p2,
                    p3,
                    p4,
                    a,
                    b,
                    n_test
                ),
                number=10
            ) / 10
        )

        # Mesure du temps pour la version NumPy.
        temps_numpy.append(
            timeit.timeit(
                lambda: rectangle_numpy(
                    p1,
                    p2,
                    p3,
                    p4,
                    a,
                    b,
                    n_test
                ),
                number=10
            ) / 10
        )

        print(f"La valeur de n est de {n_test}")

    plt.figure()

    plt.loglog(
        valeur_n,
        temps_python_classique,
        "o-",
        label="Rectangle Python"
    )

    plt.loglog(
        valeur_n,
        temps_numpy,
        "s-",
        label="Rectangle NumPy"
    )

    plt.xlabel("Nombre de rectangles n")
    plt.ylabel("Temps d'exécution moyen (s)")
    plt.title("Temps d'exécution de la méthode des rectangles")

    plt.grid(True)
    plt.legend()

    plt.show()


# ==========================================================
# 8. PROGRAMME PRINCIPAL POUR TEST LOCAL
# ==========================================================

if __name__ == "__main__":

    # Paramètres du polynôme :
    # f(x) = 1 + 2x + 3x² + 4x³
    p1 = 1
    p2 = 2
    p3 = 3
    p4 = 4

    # Bornes d'intégration.
    a = 0
    b = 10

    # Nombre de segments pour le test principal.
    n = 10

    # Valeurs utilisées pour les graphiques.
    valeur_n = [10, 50, 100, 500, 1000, 5000]

    # Calcul de la solution exacte.
    resultat_exact = solution_analytique(p1, p2, p3, p4, a, b)

    # Calculs numériques.
    resultat_python = rectangle_python_classique(p1, p2, p3, p4, a, b, n)
    resultat_numpy = rectangle_numpy(p1, p2, p3, p4, a, b, n)

    # Affichage des résultats.
    print("Solution analytique :", resultat_exact)
    print("Méthode des rectangles Python :", resultat_python)
    print("Erreur Python :", erreur_rectangle_python(p1, p2, p3, p4, a, b, n))
    print("Méthode des rectangles NumPy :", resultat_numpy)
    print("Erreur NumPy :", erreur_rectangle_numpy(p1, p2, p3, p4, a, b, n))

    # Graphique de convergence.
    tracer_courbe_convergence_rectangle(
        p1,
        p2,
        p3,
        p4,
        a,
        b,
        valeur_n
    )

    # Graphique des temps d'exécution.
    tracer_courbe_temps_execution(
        p1,
        p2,
        p3,
        p4,
        a,
        b,
        valeur_n
    )

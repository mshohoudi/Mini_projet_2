import timeit
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

from methode_rectangle import rectangle_python_classique, rectangle_numpy, calculer_valeur_y
from trapeze import trapeze_base, trapeze_numpy, trapeze_scipy
from simpson import simpson_base, simpson_numpy, simpson_scipy


# Paramètres du polynôme :
# f(x) = p1 + p2*x + p3*x**2 + p4*x**3
p1 = 1
p2 = 2
p3 = 3
p4 = 4

# Bornes d'intégration
a = 0
b = 10

# Nombre de segments utilisé pour la comparaison principale
n = 100

# Liste de valeurs de n pour les graphiques de convergence
liste_n = [10, 50, 100, 500, 1000, 5000]


def solution_exacte(p1, p2, p3, p4, a, b):
    """Calcule la solution exacte de référence avec scipy.quad."""
    resultat, erreur = quad(lambda x: calculer_valeur_y(p1, p2, p3, p4, x), a, b)
    return resultat


def calcul_erreur(valeur_exacte, valeur_numerique):
    """Calcule l'erreur absolue."""
    return abs(valeur_exacte - valeur_numerique)


def afficher_resultats():
    """Affiche les résultats numériques et les erreurs pour n donné."""

    exact = solution_exacte(p1, p2, p3, p4, a, b)

    resultats = {
        "Rectangle Python": rectangle_python_classique(p1, p2, p3, p4, a, b, n),
        "Rectangle NumPy": rectangle_numpy(p1, p2, p3, p4, a, b, n),
        "Trapèze Python": trapeze_base(p1, p2, p3, p4, a, b, n),
        "Trapèze NumPy": trapeze_numpy(p1, p2, p3, p4, a, b, n),
        "Trapèze SciPy": trapeze_scipy(p1, p2, p3, p4, a, b, n),
        "Simpson Python": simpson_base(p1, p2, p3, p4, a, b, n),
        "Simpson NumPy": simpson_numpy(p1, p2, p3, p4, a, b, n),
        "Simpson SciPy": simpson_scipy(p1, p2, p3, p4, a, b, n),
    }

    print("Valeur exacte :", exact)
    print("\nComparaison des méthodes :")

    for nom, valeur in resultats.items():
        erreur = calcul_erreur(exact, valeur)
        print(f"{nom:20s} | Résultat = {valeur:.6f} | Erreur = {erreur:.6e}")


def tracer_convergence():
    """Trace l'erreur en fonction du nombre de segments."""

    exact = solution_exacte(p1, p2, p3, p4, a, b)

    erreurs_rectangle = []
    erreurs_trapeze = []
    erreurs_simpson = []

    for n_test in liste_n:
        erreurs_rectangle.append(
            calcul_erreur(exact, rectangle_numpy(p1, p2, p3, p4, a, b, n_test))
        )
        erreurs_trapeze.append(
            calcul_erreur(exact, trapeze_numpy(p1, p2, p3, p4, a, b, n_test))
        )
        erreurs_simpson.append(
            calcul_erreur(exact, simpson_numpy(p1, p2, p3, p4, a, b, n_test))
        )

    plt.figure()
    plt.loglog(liste_n, erreurs_rectangle, "o-", label="Rectangle NumPy")
    plt.loglog(liste_n, erreurs_trapeze, "s-", label="Trapèze NumPy")
    plt.loglog(liste_n, erreurs_simpson, "^-", label="Simpson NumPy")

    plt.xlabel("Nombre de segments n")
    plt.ylabel("Erreur absolue")
    plt.title("Convergence des méthodes d'intégration")
    plt.grid(True)
    plt.legend()
    plt.show()


def tracer_temps_execution():
    """Trace le temps d'exécution des méthodes pour 1000 appels."""

    methodes = {
        "Rect. Python": lambda: rectangle_python_classique(p1, p2, p3, p4, a, b, n),
        "Rect. NumPy": lambda: rectangle_numpy(p1, p2, p3, p4, a, b, n),
        "Trap. Python": lambda: trapeze_base(p1, p2, p3, p4, a, b, n),
        "Trap. NumPy": lambda: trapeze_numpy(p1, p2, p3, p4, a, b, n),
        "Trap. SciPy": lambda: trapeze_scipy(p1, p2, p3, p4, a, b, n),
        "Simp. Python": lambda: simpson_base(p1, p2, p3, p4, a, b, n),
        "Simp. NumPy": lambda: simpson_numpy(p1, p2, p3, p4, a, b, n),
        "Simp. SciPy": lambda: simpson_scipy(p1, p2, p3, p4, a, b, n),
    }

    noms = []
    temps = []

    for nom, fonction in methodes.items():
        noms.append(nom)
        temps.append(timeit.timeit(fonction, number=1000))

    plt.figure()
    plt.bar(noms, temps)
    plt.xlabel("Méthode")
    plt.ylabel("Temps pour 1000 appels (s)")
    plt.title("Comparaison des temps d'exécution")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    afficher_resultats()
    tracer_convergence()
    tracer_temps_execution()

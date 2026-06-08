# Module permettant de mesurer précisément
# le temps d'exécution des différentes méthodes.
import timeit
import os # Ajouté pour créer le dossier figures s'il n'existe pas

# Bibliothèque permettant de manipuler
# efficacement les tableaux numériques.
import numpy as np

# Bibliothèque utilisée pour tracer
# les graphiques de convergence et de performance.
import matplotlib.pyplot as plt

# Fonction permettant de calculer une valeur
# de référence très précise de l'intégrale.
from scipy.integrate import quad

# Importation des méthodes développées dans les autres fichiers.
from methode_rectangle import (
    rectangle_python_classique,
    rectangle_numpy,
    calculer_valeur_y,
    solution_analytique as solution_exacte,
)

from trapeze import (
    trapeze_base,
    trapeze_numpy,
    trapeze_scipy
)

from simpson import (
    simpson_base,
    simpson_numpy,
    simpson_scipy
)

# ==========================================================
# PARAMÈTRES DU PROBLÈME
# ==========================================================

# Coefficients du polynôme : f(x) = p1 + p2*x + p3*x² + p4*x³
p1 = 1
p2 = 2
p3 = 3
p4 = 4

# Tuple pour les fonctions de Simpson
mes_coeffs = (p1, p2, p3, p4)

# Bornes de l'intervalle d'intégration.
a = 0
b = 10

# Nombre de segments utilisé pour la comparaison principale.
n = 100

# Valeurs de n utilisées pour l'étude de convergence.
liste_n = [10, 50, 100, 500, 1000, 5000]

# ==========================================================
# CALCUL DE L'ERREUR ABSOLUE
# ==========================================================

def calcul_erreur(valeur_exacte, valeur_numerique):
    """
    Calcule l'erreur absolue entre la valeur exacte
    et la valeur obtenue numériquement.
    """
    return abs(valeur_exacte - valeur_numerique)


# ==========================================================
# COMPARAISON DES RÉSULTATS NUMÉRIQUES
# ==========================================================

def afficher_resultats():
    """
    Affiche les résultats obtenus avec chacune
    des méthodes numériques ainsi que leurs erreurs.
    """
    exact = solution_exacte(p1, p2, p3, p4, a, b)

    resultats = {
        "Rectangle Python": rectangle_python_classique(p1, p2, p3, p4, a, b, n),
        "Rectangle NumPy": rectangle_numpy(p1, p2, p3, p4, a, b, n),
        "Trapèze Python": trapeze_base(p1, p2, p3, p4, a, b, n),
        "Trapèze NumPy": trapeze_numpy(p1, p2, p3, p4, a, b, n),
        "Trapèze SciPy": trapeze_scipy(p1, p2, p3, p4, a, b, n),
        # Correction des paramètres pour Simpson (a, b, n, coeffs)
        "Simpson Python": simpson_base(a, b, n, mes_coeffs),
        "Simpson NumPy": simpson_numpy(a, b, n, mes_coeffs),
        "Simpson SciPy": simpson_scipy(a, b, n, mes_coeffs),
    }

    print("Valeur exacte :", exact)
    print("\nComparaison des méthodes :")

    for nom, valeur in resultats.items():
        erreur = calcul_erreur(exact, valeur)
        print(f"{nom:20s} | Résultat = {valeur:.6f} | Erreur = {erreur:.6e}")


# ==========================================================
# ÉTUDE DE CONVERGENCE
# ==========================================================

def tracer_convergence():
    """
    Trace l'évolution de l'erreur lorsque
    le nombre de segments augmente.
    """
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
        # Correction des paramètres pour Simpson
        erreurs_simpson.append(
            calcul_erreur(exact, simpson_numpy(a, b, n_test, mes_coeffs))
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
    plt.savefig("figures/convergence.png", dpi=300, bbox_inches="tight")
    plt.show()


# ==========================================================
# COMPARAISON DES TEMPS D'EXÉCUTION
# ==========================================================

def tracer_temps_execution():
    """
    Compare les temps d'exécution des différentes méthodes.
    Chaque méthode est exécutée 1000 fois afin d'obtenir
    une mesure plus stable.
    """
    methodes = {
        "Rect. Python": lambda: rectangle_python_classique(p1, p2, p3, p4, a, b, n),
        "Rect. NumPy": lambda: rectangle_numpy(p1, p2, p3, p4, a, b, n),
        "Trap. Python": lambda: trapeze_base(p1, p2, p3, p4, a, b, n),
        "Trap. NumPy": lambda: trapeze_numpy(p1, p2, p3, p4, a, b, n),
        "Trap. SciPy": lambda: trapeze_scipy(p1, p2, p3, p4, a, b, n),
        # Correction des paramètres pour Simpson
        "Simp. Python": lambda: simpson_base(a, b, n, mes_coeffs),
        "Simp. NumPy": lambda: simpson_numpy(a, b, n, mes_coeffs),
        "Simp. SciPy": lambda: simpson_scipy(a, b, n, mes_coeffs),
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

    plt.savefig("figures/temps_execution.png", dpi=300, bbox_inches="tight")
    plt.show()


# ==========================================================
# PROGRAMME PRINCIPAL
# ==========================================================

if __name__ == "__main__":
    # Création du dossier 'figures' s'il n'existe pas pour éviter les erreurs lors de la sauvegarde
    os.makedirs("figures", exist_ok=True)

    afficher_resultats()
    tracer_convergence()
    tracer_temps_execution()

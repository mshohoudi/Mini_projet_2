import math
import numpy as np
import timeit
from scipy.integrate import trapezoid


# ==========================================
# 1. Définition des fonctions et solution analytique
# ==========================================

def f_math(x):
    """Fonction à intégrer (pour Python de base)."""
    return 1 + math.sin(x) ** 2


def f_numpy(x):
    """Fonction à intégrer (pour NumPy, vectorisée)."""
    return 1 + np.sin(x) ** 2


def solution_analytique(a, b):
    """Calcule la solution exacte de l'intégrale de manière analytique."""

    def F(x):
        return 1.5 * x - 0.25 * math.sin(2 * x)

    return F(b) - F(a)


# ==========================================
# 2. Implémentation des trapèzes avec Python de base
# ==========================================

def trapeze_base(a, b, n):
    """Intégration numérique par la méthode des trapèzes (Python de base)."""
    dx = (b - a) / n
    integrale = 0.0

    for i in range(n):
        x_a = a + i * dx
        x_b = a + (i + 1) * dx

        # Application de la formule du trapèze pour chaque segment
        integrale += dx * (f_math(x_a) + f_math(x_b)) / 2.0

    return integrale


# ==========================================
# 3. Implémentation des trapèzes avec NumPy
# ==========================================

def trapeze_numpy(a, b, n):
    """Intégration numérique par la méthode des trapèzes (NumPy, sans boucle for)."""
    x = np.linspace(a, b, n + 1)
    dx = (b - a) / n

    # Évaluation de la fonction sur tous les points
    f_a = f_numpy(x[:-1])
    f_b = f_numpy(x[1:])

    # Somme vectorisée des aires des trapèzes
    integrale = np.sum(dx * (f_a + f_b) / 2.0)

    return integrale


# ==========================================
# 4. Comparaison avec la méthode pré-programmée
# ==========================================

def trapeze_scipy(a, b, n):
    """Intégration numérique en utilisant la méthode pré-programmée de SciPy."""
    x = np.linspace(a, b, n + 1)
    y = f_numpy(x)

    # Utilisation de scipy.integrate.trapezoid
    return trapezoid(y=y, x=x)


# ==========================================
# 5. Bloc principal pour les tests locaux
# ==========================================

if __name__ == "__main__":
    # Paramètres de test
    a = 0.0
    b = math.pi
    n = 100

    # Calculs
    val_exacte = solution_analytique(a, b)
    res_base = trapeze_base(a, b, n)
    res_numpy = trapeze_numpy(a, b, n)
    res_scipy = trapeze_scipy(a, b, n)

    # Affichage des erreurs
    print(f"Valeur exacte : {val_exacte}")
    print(f"Erreur (Python de base) : {abs(val_exacte - res_base)}")
    print(f"Erreur (NumPy) : {abs(val_exacte - res_numpy)}")
    print(f"Erreur (SciPy pré-programmée) : {abs(val_exacte - res_scipy)}")

    # Mesure du temps d'exécution
    t_base = timeit.timeit(lambda: trapeze_base(a, b, n), number=1000)
    t_numpy = timeit.timeit(lambda: trapeze_numpy(a, b, n), number=1000)
    t_scipy = timeit.timeit(lambda: trapeze_scipy(a, b, n), number=1000)

    print(f"\nTemps d'exécution (Python de base) : {t_base:.5f} s")
    print(f"Temps d'exécution (NumPy) : {t_numpy:.5f} s")
    print(f"Temps d'exécution (SciPy) : {t_scipy:.5f} s")
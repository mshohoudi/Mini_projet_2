import numpy as np
import timeit
from scipy.integrate import simpson, quad


# ==========================================
# 1. Définition de la fonction polynomiale
# ==========================================

def calculer_valeur_y(p1, p2, p3, p4, x):
    """Calcule la valeur du polynôme f(x)."""
    return p1 + p2 * x + p3 * x**2 + p4 * x**3


# ==========================================
# 2. Solution analytique avec SciPy quad
# ==========================================

def solution_analytique(p1, p2, p3, p4, a, b):
    """Calcule la solution exacte de l'intégrale avec la primitive analytique."""

    def primitive(x):
        return (
            p1 * x
            + (p2 / 2) * x**2
            + (p3 / 3) * x**3
            + (p4 / 4) * x**4
        )

    return primitive(b) - primitive(a)


# ==========================================
# 3. Méthode de Simpson avec Python de base
# ==========================================

def simpson_base(p1, p2, p3, p4, a, b, n):
    """Intégration numérique par la méthode de Simpson en Python de base."""
    dx = (b - a) / n
    integrale = 0.0

    for i in range(n):
        x_a = a + i * dx
        x_b = a + (i + 1) * dx
        x_mid = (x_a + x_b) / 2.0

        integrale += (dx / 6.0) * (
            calculer_valeur_y(p1, p2, p3, p4, x_a)
            + 4 * calculer_valeur_y(p1, p2, p3, p4, x_mid)
            + calculer_valeur_y(p1, p2, p3, p4, x_b)
        )

    return integrale


# ==========================================
# 4. Méthode de Simpson avec NumPy
# ==========================================

def simpson_numpy(p1, p2, p3, p4, a, b, n):
    """Intégration numérique par la méthode de Simpson avec NumPy."""
    dx = (b - a) / n
    x = np.linspace(a, b, n + 1)

    x_mid = x[:-1] + dx / 2.0

    f_a = calculer_valeur_y(p1, p2, p3, p4, x[:-1])
    f_mid = calculer_valeur_y(p1, p2, p3, p4, x_mid)
    f_b = calculer_valeur_y(p1, p2, p3, p4, x[1:])

    integrale = np.sum((dx / 6.0) * (f_a + 4 * f_mid + f_b))

    return integrale


# ==========================================
# 5. Méthode de Simpson avec SciPy
# ==========================================

def simpson_scipy(p1, p2, p3, p4, a, b, n):
    """Intégration numérique avec la fonction simpson de SciPy."""
    x = np.linspace(a, b, n + 1)
    y = calculer_valeur_y(p1, p2, p3, p4, x)

    return simpson(y=y, x=x)


# ==========================================
# 6. Bloc principal pour les tests locaux
# ==========================================

if __name__ == "__main__":
    p1 = 1
    p2 = 2
    p3 = 3
    p4 = 4

    a = 0
    b = 10
    n = 100

    val_exacte = solution_analytique(p1, p2, p3, p4, a, b)

    res_base = simpson_base(p1, p2, p3, p4, a, b, n)
    res_numpy = simpson_numpy(p1, p2, p3, p4, a, b, n)
    res_scipy = simpson_scipy(p1, p2, p3, p4, a, b, n)

    print(f"Valeur exacte : {val_exacte}")
    print(f"Résultat Simpson Python : {res_base}")
    print(f"Résultat Simpson NumPy : {res_numpy}")
    print(f"Résultat Simpson SciPy : {res_scipy}")

    print(f"\nErreur Python : {abs(val_exacte - res_base)}")
    print(f"Erreur NumPy : {abs(val_exacte - res_numpy)}")
    print(f"Erreur SciPy : {abs(val_exacte - res_scipy)}")

    t_base = timeit.timeit(lambda: simpson_base(p1, p2, p3, p4, a, b, n), number=1000)
    t_numpy = timeit.timeit(lambda: simpson_numpy(p1, p2, p3, p4, a, b, n), number=1000)
    t_scipy = timeit.timeit(lambda: simpson_scipy(p1, p2, p3, p4, a, b, n), number=1000)

    print(f"\nTemps d'exécution Python : {t_base:.5f} s")
    print(f"Temps d'exécution NumPy : {t_numpy:.5f} s")
    print(f"Temps d'exécution SciPy : {t_scipy:.5f} s")
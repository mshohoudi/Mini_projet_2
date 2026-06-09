import numpy as np
import timeit
from scipy.integrate import trapezoid


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
# 3. Méthode des trapèzes avec Python de base
# ==========================================

def trapeze_base(p1, p2, p3, p4, a, b, n):
    """Intégration numérique par la méthode des trapèzes en Python de base."""
    taille_intervalle = (b - a) / n
    integrale = 0.0

    for i in range(n):
        x_a = a + i * taille_intervalle
        x_b = a + (i + 1) * taille_intervalle

        integrale += taille_intervalle * (
            calculer_valeur_y(p1, p2, p3, p4, x_a)
            + calculer_valeur_y(p1, p2, p3, p4, x_b)
        ) / 2.0

    return integrale


# ==========================================
# 4. Méthode des trapèzes avec NumPy
# ==========================================

def trapeze_numpy(p1, p2, p3, p4, a, b, n):
    """Intégration numérique par la méthode des trapèzes avec NumPy."""
    taille_intervalle = (b - a) / n

    x = np.linspace(a, b, n + 1)

    y_gauche = calculer_valeur_y(p1, p2, p3, p4, x[:-1])
    y_droite = calculer_valeur_y(p1, p2, p3, p4, x[1:])

    integrale = np.sum(taille_intervalle * (y_gauche + y_droite) / 2.0)

    return integrale


# ==========================================
# 5. Méthode des trapèzes avec SciPy
# ==========================================

def trapeze_scipy(p1, p2, p3, p4, a, b, n):
    """Intégration numérique avec la fonction trapezoid de SciPy."""
    x = np.linspace(a, b, n + 1)
    y = calculer_valeur_y(p1, p2, p3, p4, x)

    return trapezoid(y=y, x=x)


# ==========================================
# 6. Calcul des erreurs
# ==========================================

def erreur_trapeze_base(p1, p2, p3, p4, a, b, n):
    """Calcule l'erreur absolue de la méthode des trapèzes Python."""
    exact = solution_analytique(p1, p2, p3, p4, a, b)
    numerique = trapeze_base(p1, p2, p3, p4, a, b, n)
    return abs(exact - numerique)


def erreur_trapeze_numpy(p1, p2, p3, p4, a, b, n):
    """Calcule l'erreur absolue de la méthode des trapèzes NumPy."""
    exact = solution_analytique(p1, p2, p3, p4, a, b)
    numerique = trapeze_numpy(p1, p2, p3, p4, a, b, n)
    return abs(exact - numerique)


def erreur_trapeze_scipy(p1, p2, p3, p4, a, b, n):
    """Calcule l'erreur absolue de la méthode des trapèzes SciPy."""
    exact = solution_analytique(p1, p2, p3, p4, a, b)
    numerique = trapeze_scipy(p1, p2, p3, p4, a, b, n)
    return abs(exact - numerique)


# ==========================================
# 7. Bloc principal pour les tests locaux
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

    res_base = trapeze_base(p1, p2, p3, p4, a, b, n)
    res_numpy = trapeze_numpy(p1, p2, p3, p4, a, b, n)
    res_scipy = trapeze_scipy(p1, p2, p3, p4, a, b, n)

    print(f"Valeur exacte : {val_exacte}")
    print(f"Résultat trapèzes Python : {res_base}")
    print(f"Résultat trapèzes NumPy : {res_numpy}")
    print(f"Résultat trapèzes SciPy : {res_scipy}")

    print(f"\nErreur Python : {abs(val_exacte - res_base)}")
    print(f"Erreur NumPy : {abs(val_exacte - res_numpy)}")
    print(f"Erreur SciPy : {abs(val_exacte - res_scipy)}")

    t_base = timeit.timeit(lambda: trapeze_base(p1, p2, p3, p4, a, b, n), number=1000)
    t_numpy = timeit.timeit(lambda: trapeze_numpy(p1, p2, p3, p4, a, b, n), number=1000)
    t_scipy = timeit.timeit(lambda: trapeze_scipy(p1, p2, p3, p4, a, b, n), number=1000)

    print(f"\nTemps d'exécution Python : {t_base:.5f} s")
    print(f"Temps d'exécution NumPy : {t_numpy:.5f} s")
    print(f"Temps d'exécution SciPy : {t_scipy:.5f} s")

import numpy as np
import timeit
from scipy.integrate import simpson


# ==========================================
# 1. Définition des fonctions et solution analytique
# ==========================================
def f_math(x, coeffs):
    """Fonction polynomiale du 3e ordre (Python de base)."""
    p1, p2, p3, p4 = coeffs
    return p1 + p2 * x + p3 * (x ** 2) + p4 * (x ** 3)


def f_numpy(x, coeffs):
    """Fonction polynomiale du 3e ordre (NumPy, vectorisée)."""
    p1, p2, p3, p4 = coeffs
    return p1 + p2 * x + p3 * (x ** 2) + p4 * (x ** 3)


def solution_analytique(a, b, coeffs):
    """Calcule la solution exacte de l'intégrale de manière analytique."""
    p1, p2, p3, p4 = coeffs

    def F(x):
        return p1 * x + (p2 / 2.0) * (x ** 2) + (p3 / 3.0) * (x ** 3) + (p4 / 4.0) * (x ** 4)

    return F(b) - F(a)


# ==========================================
# 2. Implémentation de Simpson avec Python de base
# ==========================================
def simpson_base(a, b, n, coeffs):
    """Intégration numérique par la méthode de Simpson (Python de base)."""
    dx = (b - a) / n
    integrale = 0.0
    for i in range(n):
        x_a = a + i * dx
        x_b = a + (i + 1) * dx
        x_mid = (x_a + x_b) / 2.0
        # Application de la formule de Simpson pour chaque segment
        integrale += (dx / 6.0) * (f_math(x_a, coeffs) + 4 * f_math(x_mid, coeffs) + f_math(x_b, coeffs))
    return integrale


# ==========================================
# 3. Implémentation de Simpson avec NumPy (vectorisée)
# ==========================================
def simpson_numpy(a, b, n, coeffs):
    """Intégration numérique par la méthode de Simpson (NumPy, sans boucle for)."""
    x = np.linspace(a, b, n + 1)
    dx = (b - a) / n

    # Trouver les points médians de tous les segments simultanément
    x_mid = x[:-1] + dx / 2.0

    # Évaluation de la fonction sous forme de tableaux (arrays)
    f_a = f_numpy(x[:-1], coeffs)
    f_mid = f_numpy(x_mid, coeffs)
    f_b = f_numpy(x[1:], coeffs)

    # Somme vectorisée
    integrale = np.sum((dx / 6.0) * (f_a + 4 * f_mid + f_b))
    return integrale


# ==========================================
# 4. Comparaison avec les méthodes pré-programmées
# ==========================================
def simpson_scipy(a, b, n, coeffs):
    """Intégration numérique en utilisant la méthode pré-programmée de SciPy."""
    x = np.linspace(a, b, n + 1)
    y = f_numpy(x, coeffs)
    # Utilisation de scipy.integrate.simpson
    return simpson(y=y, x=x)


# ==========================================
# 5. Bloc principal pour les tests locaux
# ==========================================
if __name__ == "__main__":
    # Paramètres de test
    a = 0.0
    b = 5.0
    n = 100

    # Définition des coefficients: p1, p2, p3, p4 pour f(x) = 1 + 2x + 3x^2 + 4x^3
    mes_coeffs = (1.0, 2.0, 3.0, 4.0)

    # Calculs
    val_exacte = solution_analytique(a, b, mes_coeffs)
    res_base = simpson_base(a, b, n, mes_coeffs)
    res_numpy = simpson_numpy(a, b, n, mes_coeffs)
    res_scipy = simpson_scipy(a, b, n, mes_coeffs)

    # Affichage des erreurs
    print(f"Valeur exacte : {val_exacte}")
    print(f"Erreur (Python de base) : {abs(val_exacte - res_base)}")
    print(f"Erreur (NumPy) : {abs(val_exacte - res_numpy)}")
    print(f"Erreur (SciPy) : {abs(val_exacte - res_scipy)}")
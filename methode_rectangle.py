import numpy as np
from scipy.integrate import quad
import timeit
import matplotlib.pyplot as plt

# ==========================================
# 1. Définition des fonctions et solution analytique
# ==========================================
def calculer_valeur_y(p1, p2, p3, p4, x):
    """Calcule la valeur du polynôme f(x)."""
    return p1 + p2 * x + p3 * x**2 + p4 * x**3

def solution_analytique(p1, p2, p3, p4, a, b):
    """Calcule la solution exacte avec la primitive mathématique."""
    def primitive(x):
        return p1 * x + (p2 / 2.0) * x**2 + (p3 / 3.0) * x**3 + (p4 / 4.0) * x**4
    return primitive(b) - primitive(a)

# ==========================================
# 2. Implémentations de la méthode des rectangles
# ==========================================
def rectangle_python_classique(p1, p2, p3, p4, a, b, n):
    """Méthode des rectangles avec point milieu (Python de base)."""
    taille_intervalle = (b - a) / n
    integrale = 0.0
    for i in range(n):
        x_milieu = a + (taille_intervalle / 2.0) + (i * taille_intervalle)
        integrale += calculer_valeur_y(p1, p2, p3, p4, x_milieu) * taille_intervalle
    return integrale

def rectangle_numpy(p1, p2, p3, p4, a, b, n):
    """Méthode des rectangles avec point milieu (NumPy vectorisé)."""
    taille_intervalle = (b - a) / n
    x = np.linspace(a + taille_intervalle / 2.0, b - taille_intervalle / 2.0, n)
    integrale = np.sum(calculer_valeur_y(p1, p2, p3, p4, x) * taille_intervalle)
    return integrale

# ==========================================
# 3. Calculs d'erreurs
# ==========================================
def erreur_integration(p1, p2, p3, p4, a, b, n):
    """Calcule l'erreur absolue par rapport à la solution mathématique exacte."""
    resultat_analytique = solution_analytique(p1, p2, p3, p4, a, b)
    resultat_numerique = rectangle_numpy(p1, p2, p3, p4, a, b, n)
    erreur_absolue = abs(resultat_numerique - resultat_analytique)
    return erreur_absolue

# ==========================================
# 4. Fonctions de tracé (Graphiques)
# ==========================================
def tracer_courbe_convergence_rectangle(p1, p2, p3, p4, a, b, valeur_n):
    erreurs = []
    for i in valeur_n:
        erreurs.append(erreur_integration(p1, p2, p3, p4, a, b, i))
    
    plt.figure()
    plt.loglog(valeur_n, erreurs, 'o-', label='Erreur Rectangles')
    plt.xlabel("Nombre de segments n")
    plt.ylabel("Erreur absolue")
    plt.title("Convergence de la méthode des rectangles")
    plt.grid(True)
    plt.legend()
    plt.show()

def tracer_courbe_temps_execution(p1, p2, p3, p4, a, b, valeur_n):
    temps_python_classique = []
    temps_numpy = []
    temps_scipy = []

    for i in valeur_n:
        # Correction du bogue : utilisation de 'i' au lieu de 100
        temps_python_classique.append(timeit.timeit(lambda: rectangle_python_classique(p1, p2, p3, p4, a, b, i), number=10) / 10)
        temps_numpy.append(timeit.timeit(lambda: rectangle_numpy(p1, p2, p3, p4, a, b, i), number=10) / 10)
        temps_scipy.append(timeit.timeit(lambda: quad(lambda x: calculer_valeur_y(p1, p2, p3, p4, x), a, b), number=10) / 10)

    plt.figure()
    plt.loglog(valeur_n, temps_python_classique, 'o-', label='Rectangle Python classique')
    plt.loglog(valeur_n, temps_numpy, 's-', label='Rectangle NumPy')
    plt.loglog(valeur_n, temps_scipy, '^-', label='SciPy (Quad)')
    plt.xlabel("Nombre de segments n")
    plt.ylabel("Temps d'exécution (s)")
    plt.title("Temps d'exécution de la méthode des rectangles")
    plt.grid(True)
    plt.legend()
    plt.show()

# ==========================================
# 5. Bloc principal pour les tests locaux
# ==========================================
if __name__ == "__main__":
    p1, p2, p3, p4 = 1, 2, 3, 4
    a, b = 0, 10
    n = 100

    print(f"Valeur exacte : {solution_analytique(p1, p2, p3, p4, a, b)}")
    print(f"Intégrale (Python) : {rectangle_python_classique(p1, p2, p3, p4, a, b, n)}")
    print(f"Intégrale (NumPy) : {rectangle_numpy(p1, p2, p3, p4, a, b, n)}")
    print(f"Erreur absolue (NumPy) : {erreur_integration(p1, p2, p3, p4, a, b, n)}")

    # Décommenter ces lignes pour tester les graphiques localement
    # tracer_courbe_convergence_rectangle(p1, p2, p3, p4, a, b, [10, 50, 100, 500, 1000, 5000])
    # tracer_courbe_temps_execution(p1, p2, p3, p4, a, b, [10, 50, 100, 500, 1000, 5000])

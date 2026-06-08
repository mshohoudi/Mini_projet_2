"""
Tests unitaires pour le Mini-Projet B.

Ce fichier vérifie que les principales méthodes d'intégration
retournent les résultats attendus pour le polynôme :

f(x) = 1 + 2x + 3x² + 4x³

sur l'intervalle [0, 10].

Pour lancer les tests, utiliser la commande :

    python -m pytest -v
"""

# Module permettant d'accéder aux chemins de fichiers.
from pathlib import Path

# Module permettant de modifier temporairement
# le chemin d'importation de Python.
import sys

# Comme ce fichier est placé dans le dossier tests/,
# Python ne trouve pas automatiquement les fichiers situés
# dans le dossier parent du projet.
#
# Cette ligne ajoute donc le dossier parent Mini_projet_2/
# au chemin de recherche de Python.
sys.path.insert(0, str(Path(__file__).parent.parent))

# Importation des fonctions à tester.
from methode_rectangle import rectangle_python_classique, rectangle_numpy
from trapeze import trapeze_base, trapeze_numpy, trapeze_scipy
from simpson import simpson_base, simpson_numpy, simpson_scipy


# ==========================================================
# PARAMÈTRES COMMUNS AUX TESTS
# ==========================================================

# Coefficients du polynôme :
# f(x) = p1 + p2*x + p3*x² + p4*x³
p1 = 1
p2 = 2
p3 = 3
p4 = 4

# Tuple contenant les coefficients pour la méthode de Simpson
mes_coeffs = (p1, p2, p3, p4)

# Bornes d'intégration.
a = 0
b = 10

# Nombre de segments utilisé pour les tests.
n = 10


# ==========================================================
# TESTS POUR LA MÉTHODE DES RECTANGLES
# ==========================================================

def test_rectangle_python_classique():
    """
    Vérifie que la méthode des rectangles en Python de base
    retourne la valeur attendue pour n = 10.
    """
    resultat = rectangle_python_classique(p1, p2, p3, p4, a, b, n)
    assert abs(resultat - 11057.5) < 1e-6


def test_rectangle_numpy():
    """
    Vérifie que la méthode des rectangles avec NumPy
    retourne la même valeur attendue pour n = 10.
    """
    resultat = rectangle_numpy(p1, p2, p3, p4, a, b, n)
    assert abs(resultat - 11057.5) < 1e-6


# ==========================================================
# TESTS POUR LA MÉTHODE DES TRAPÈZES
# ==========================================================

def test_trapeze_python():
    """
    Vérifie que la méthode des trapèzes en Python de base
    retourne la valeur attendue pour n = 10.
    """
    resultat = trapeze_base(p1, p2, p3, p4, a, b, n)
    assert abs(resultat - 11215.0) < 1e-6


def test_trapeze_numpy():
    """
    Vérifie que la méthode des trapèzes avec NumPy
    retourne la valeur attendue pour n = 10.
    """
    resultat = trapeze_numpy(p1, p2, p3, p4, a, b, n)
    assert abs(resultat - 11215.0) < 1e-6


def test_trapeze_scipy():
    """
    Vérifie que la méthode des trapèzes préprogrammée
    avec SciPy retourne la valeur attendue pour n = 10.
    """
    resultat = trapeze_scipy(p1, p2, p3, p4, a, b, n)
    assert abs(resultat - 11215.0) < 1e-6


# ==========================================================
# TESTS POUR LA MÉTHODE DE SIMPSON
# ==========================================================

def test_simpson_python():
    """
    Vérifie que la méthode de Simpson en Python de base
    retourne la solution exacte pour ce polynôme de degré 3.
    """
    # Correction des arguments pour correspondre à (a, b, n, coeffs)
    resultat = simpson_base(a, b, n, mes_coeffs)
    assert abs(resultat - 11110.0) < 1e-6


def test_simpson_numpy():
    """
    Vérifie que la méthode de Simpson avec NumPy
    retourne la solution exacte pour ce polynôme de degré 3.
    """
    # Correction des arguments
    resultat = simpson_numpy(a, b, n, mes_coeffs)
    assert abs(resultat - 11110.0) < 1e-6


def test_simpson_scipy():
    """
    Vérifie que la méthode de Simpson préprogrammée
    avec SciPy retourne la solution exacte pour ce polynôme.
    """
    # Correction des arguments
    resultat = simpson_scipy(a, b, n, mes_coeffs)
    assert abs(resultat - 11110.0) < 1e-6
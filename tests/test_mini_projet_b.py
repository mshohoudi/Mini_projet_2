"""Tests pour le Mini-Projet B.

Ce fichier contient les tests pour le Mini-Projet B.

Pour lancer les tests :
    pip install pytest
    pytest -v
"""
import sys
from pathlib import Path

# Permet d'importer main.py depuis le dossier parent
sys.path.insert(0, str(Path(__file__).parent.parent))


from methode_rectangle import (
    rectangle_python_classique,
)


def test_rectangle_classique_1_2_3_4_a0_b10_n10():
    assert rectangle_python_classique(1,2,3,4,0,10,10) == 11057.5
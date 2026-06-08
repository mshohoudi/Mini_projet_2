# Mini Projet B – Intégration numérique

## Auteurs

* Nicolas Allard
* Mohammad Shohoudimojdehi
* Ogechi Amajuoyi

---

## Description du projet

Ce projet consiste à implémenter et comparer différentes méthodes d'intégration numérique appliquées à une fonction polynomiale du troisième degré.

La fonction étudiée est :

$$f(x) = p_1 + p_2x + p_3x^2 + p_4x^3$$

avec :

* p1 = 1
* p2 = 2
* p3 = 3
* p4 = 4

sur l'intervalle :

[a,b] = [0,10]

L'objectif est de comparer la précision, la convergence et les performances des différentes méthodes numériques.

---

## Méthodes implémentées

### Méthode des rectangles

* Python de base
* NumPy

### Méthode des trapèzes

* Python de base
* NumPy
* SciPy

### Méthode de Simpson

* Python de base
* NumPy
* SciPy

---

## Répartition des tâches

### Nicolas Allard

* Développement de la méthode des rectangles
* Création des tests unitaires

### Ogechi Amajuoyi

* Développement de la méthode des trapèzes
* Intégration des méthodes dans le programme principal
* Génération des graphiques comparatifs
* Analyse des résultats

### Mohammad Shohoudimojdehi

* Développement de la méthode de Simpson
* Validation des résultats
* Révision finale du projet

---

## Bibliothèques utilisées

Le projet utilise les bibliothèques suivantes :

* NumPy
* SciPy
* Matplotlib
* Timeit

---

## Installation

Installer les dépendances requises :

pip install numpy scipy matplotlib

---

## Exécution

Pour exécuter le programme principal :

python main.py

Le programme :

1. Calcule la valeur exacte de l'intégrale.
2. Exécute les méthodes des rectangles, des trapèzes et de Simpson.
3. Calcule les erreurs absolues.
4. Compare les temps d'exécution.
5. Génère les graphiques de convergence.
6. Génère les graphiques de performance.

---

## Structure du projet

Mini_projet_2/

├── main.py

├── methode_rectangle.py

├── trapeze.py

├── simpson.py

├── README.md

│

├── figures/

│   ├── convergence_methodes_integration.png

│   └── comparaison_temps_execution.png

│

└── tests/

│   └── test_mini_projet_b.py

Le dossier figures contient les graphiques générés automatiquement par le programme.

Le dossier tests contient les tests unitaires permettant de valider les implémentations des méthodes des rectangles, des trapèzes et de Simpson.

---

## Résultats obtenus

Valeur exacte :

11110.0

| Méthode          | Résultat     | Erreur absolue |
| ---------------- | ------------ | -------------- |
| Rectangle Python | 11109.475000 | 5.25e-01       |
| Rectangle NumPy  | 11109.475000 | 5.25e-01       |
| Trapèze Python   | 11111.050000 | 1.05e+00       |
| Trapèze NumPy    | 11111.050000 | 1.05e+00       |
| Trapèze SciPy    | 11111.050000 | 1.05e+00       |
| Simpson Python   | 11110.000000 | 3.64e-12       |
| Simpson NumPy    | 11110.000000 | 1.82e-12       |
| Simpson SciPy    | 11110.000000 | 0.00e+00       |

---

## Analyse des résultats

Les résultats obtenus montrent que :

* La méthode de Simpson est la plus précise.
* Les erreurs diminuent lorsque le nombre de segments augmente.
* Les implémentations utilisant NumPy sont généralement plus rapides que les versions Python classiques.
* Les fonctions SciPy permettent de valider les résultats obtenus par les implémentations développées.

---

## Graphiques générés

Le programme génère automatiquement :

* un graphique de convergence des méthodes d'intégration ;
* un graphique comparant les temps d'exécution.

Ces graphiques permettent d'évaluer visuellement la précision et les performances de chaque méthode.

---

## Conclusion

Ce projet a permis d'implémenter et de comparer trois méthodes classiques d'intégration numérique.

Les résultats démontrent que la méthode de Simpson fournit la meilleure précision pour la fonction étudiée, tandis que l'utilisation de NumPy permet généralement d'améliorer les performances d'exécution.

L'étude met également en évidence l'importance de la convergence et du coût de calcul dans l'évaluation des méthodes numériques.

# Mini_Projet B : Intégration Numérique


## 1. Description du Projet
Ce projet a pour but d'implémenter et de comparer trois méthodes d'intégration numérique pour un polynôme du 3e ordre :
- Méthode des Rectangles
- Méthode des Trapèzes
- Méthode de Simpson

L'objectif est d'évaluer l'erreur absolue et le temps d'exécution (avec `timeit`) de chaque méthode par rapport à une solution analytique exacte, en utilisant le langage Python de base ainsi que les bibliothèques NumPy et SciPy.

## 2. Auteurs et Contributions
- **[Mohammad Shohoudimojdehi]** : Développement de la méthode de Simpson.
- **[Ogechi Amajuoyi]** : Développement de la méthode des Trapèzes..
- **[Nicolas Allard]** : Développement de la méthode des Rectangles.

## 3. Prérequis
Pour exécuter ce projet, vous avez besoin de Python 3 et des bibliothèques suivantes :
- `numpy`
- `scipy`
- `matplotlib`

## 4. Structure des Fichiers
- `main.py` : Fichier principal qui exécute les méthodes, compare les résultats et génère les graphiques d'erreur (convergence) et de temps d'exécution.
- `simpson.py` : Module contenant les calculs pour la méthode de Simpson.
- `trapeze.py` : Module contenant les calculs pour la méthode des trapèzes.
- `rectangle.py` : Module contenant les calculs pour la méthode des rectangles.

## 5. Comment exécuter le code
Ouvrez un terminal, placez-vous dans le dossier racine du projet et exécutez la commande suivante :
```bash
python main.py
import numpy as np
from scipy.integrate import quad
import timeit
import matplotlib.pyplot as plt


def rectangle_python_classique(p1,p2,p3,p4,a,b,n):
    taille_intervalle=(b-a)/n


    valeur_y = []
    integrale =0
    for i in range(n):
        valeur_y.append(calculer_valeur_y(p1,p2,p3,p4,a+taille_intervalle/2+i*taille_intervalle))
        #print (f"voici la liste des valeurs en y {valeur_y}")
        hauteur_rectangle=(calculer_valeur_y(p1, p2, p3, p4, a + taille_intervalle / 2 + i * taille_intervalle))
        integrale+=hauteur_rectangle*taille_intervalle
        #print (f"voici l'intgrale des valeurs en y {integrale}")
    return integrale

def calculer_valeur_y(p1,p2,p3,p4,x):
    return p1+p2*x+p3*x**2+p4*x**3


def erreur_integration (p1,p2,p3,p4,a,b,n):
    resultat_analytique, erreur = quad(lambda x: calculer_valeur_y(p1,p2,p3,p4,x), a, b)
    print (f"le résultat analytique est de : {resultat_analytique}")
    erreur_integrale = abs(rectangle_numpy(p1,p2,p3,p4,a,b,n) - resultat_analytique) / resultat_analytique
    print(f"l'erreur estd e {erreur_integrale}")
    return erreur_integrale

def rectangle_numpy(p1,p2,p3,p4,a,b,n):
    taille_intervalle = (b - a) / n

    x=np.linspace(a+taille_intervalle/2,b-taille_intervalle/2,n)

    integrale=np.sum(calculer_valeur_y(p1,p2,p3,p4,x)*taille_intervalle)
    return integrale

def tracer_courbe_convergence_rectangle(p1,p2,p3,p4,a,b,valeur_n):

    erreurs = []
    for i in valeur_n:
        erreurs.append(erreur_integration(p1,p2,p3,p4,a,b,i))
        print(f"la valeur de n est de {i}")
    print (f"les erreurs sont de : {erreurs}")

    plt.figure()

    plt.loglog(valeur_n, erreurs, 'o-')

    plt.xlabel("Nombre de rectangles n")
    plt.ylabel("Erreur absolue")
    plt.title("Convergence de la méthode des rectangles")
    plt.grid(True)

    plt.show()


def tracer_courbe_temps_execution(p1,p2,p3,p4,a,b,valeur_n):

    temps_python_classique = []
    temps_numpy = []
    temps_scipy = []

    for i in valeur_n:
        temps_python_classique.append(timeit.timeit(lambda : rectangle_python_classique(1,2,3,4,0,10,100),number=10)/10)
        temps_numpy.append(timeit.timeit(lambda: rectangle_numpy(1, 2, 3, 4, 0, 10, 100), number=10) / 10)
        temps_scipy.append(timeit.timeit(lambda: quad(lambda x: calculer_valeur_y(p1,p2,p3,p4,x), a, b), number=10) / 10)

        print(f"la valeur de n est de {i}")


    plt.figure()

    plt.loglog(valeur_n, temps_python_classique, 'o-', label='Rectangle python classique')
    plt.loglog(valeur_n, temps_numpy, 's-', label='Rectangle NUMPY')
    plt.loglog(valeur_n, temps_scipy, '^-', label='Scipy')

    plt.xlabel("Nombre de rectangles n")
    plt.ylabel("Temps d'exécution")
    plt.title("Temps d'exécution de la méthode des rectangles")
    plt.grid(True)
    plt.legend()
    plt.show()


print(f"Voici la réponse de l'intégrale : {rectangle_python_classique(1,2,3,4,0,10,10)}")
print(f"Voici la réponse de l'intégrale : {rectangle_numpy(1,2,3,4,0,10,10)}")
erreur_integration(1,2,3,4,0,10,10)

#temps_python=timeit.timeit(lambda : rectangle_python_classique(1,2,3,4,0,10,100),number=100)
#print(f"Temps d'integration python : {temps_python/100}")

#temps_numpy=timeit.timeit(lambda : rectangle_numpy(1,2,3,4,0,10,100),number=100)
#print(f"Temps d'integration numpy : {temps_numpy/100}")

tracer_courbe_temps_execution(1,2,3,4,0,10,[10,50,100,500,1000,5000])
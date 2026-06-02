import numpy as np
from scipy.integrate import quad



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




print(f"Voici la réponse de l'intégrale : {rectangle_python_classique(1,2,3,4,0,10,10)}")
print(f"Voici la réponse de l'intégrale : {rectangle_numpy(1,2,3,4,0,10,10)}")
erreur_integration(1,2,3,4,0,10,10)
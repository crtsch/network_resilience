#-----         IMPORTS         -----#


import graphe
import matrice

import matplotlib.pyplot as plt
import numpy as np





#-----         CALCULS         -----#


def beta_defaut(A):
    """
    Renvoie 1/w_moy pour la matrice d'adjacence A
    """
    somme = 0
    nb = 0
    n = len(A)
    for i in range(n):
        for j in range(i, n):
            if not np.isinf(A[i, j]):
                nb += 1
                somme += A[i, j]
    return nb/somme


def quicksort(l):
    """
    Applique l'algorithme de tri rapide à une liste
    """
    n = len(l)
    
    if (n == 0 or n == 1):
        return l
    
    pivot = l[n//2]

    gauche = [e for e in l if e < pivot]
    milieu = [e for e in l if e == pivot]
    droite = [e for e in l if e > pivot]

    return quicksort(gauche) + milieu + quicksort(droite)





#-----        METRIQUES        -----#


def centralite_non_normalisee(Delta, c, det_I_moins_Delta):
    """
    Renvoie la valeur de la centralité non normalisée du cycle c dans G de matrice d'adjacence Delta
    On passe en argument det(I_n - Delta)
    """
    Delta_c = np.copy(Delta)
    I = matrice.id(Delta.shape[0])
    n = len(c)
    for i in range(n-1):
        Delta_c[c[i]][c[i+1]] = 0.
        Delta_c[c[i+1]][c[i]] = 0.
    Delta_c[c[-1]][c[0]] = 0.
    Delta_c[c[0]][c[-1]] = 0.

    det_I_moins_Delta_c = matrice.det(I - Delta_c)

    if np.isclose(det_I_moins_Delta, 0.0):
        return 0.0

    return max(0.0, 1.0 - (det_I_moins_Delta_c / det_I_moins_Delta))


def centralites_normalisees(Delta, cycles=None):
    """
    Renvoie la liste des centralités normalisées des cycles fondamentaux du graphe de matrice d'adjacence Delta
    """
    if cycles == None:
        cycles = graphe.liste_cycles_fondamentaux(Delta)
    if len(cycles) == 0:
        return []
    det_I_moins_Delta = np.linalg.det(matrice.id(Delta.shape[0]) - Delta)
    centralites_non_norm = []
    somme_centralites = 0
    for cycle in cycles:
        centralite = centralite_non_normalisee(Delta, cycle, det_I_moins_Delta)
        centralites_non_norm.append(centralite)
        somme_centralites += centralite
    if np.isclose(somme_centralites, 0.0):
        return [1 / len(centralites_non_norm)] * len(centralites_non_norm)
    return [(1/somme_centralites)*c for c in centralites_non_norm]


def lorenz(Delta, filename="lorenz"):
    """
    Trace la courbe de Lorenz du graphe de matrice d'adjacence Delta
    Renvoie x et y les coordonnées des points du graphe, nécessaires pour calculer Gini
    """
    cycles = graphe.liste_cycles_fondamentaux(Delta)
    centralites = centralites_normalisees(Delta, cycles)
    n = len(centralites)

    if n == 0:
        x = [0.0, 1.0]
        y = [0.0, 1.0]
    else:
        centralites_triees = quicksort([max(0.0, c) for c in centralites])
        y = [0.0]
        for c in centralites_triees:
            y.append(y[-1] + c)

        total = y[-1]
        y = [val / total for val in y]
        x = [i / n for i in range(n+1)]

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_aspect("equal", "box")
    ax.plot(x, y, marker='.', color='purple')
    ax.plot([0,1], [0, 1], ":g")

    ax.set_xlabel(r'Proportion de cycles considérés')
    ax.set_ylabel(r'Somme des centralités')
    ax.set_title("Courbe de Lorenz")
    ax.set_facecolor("#fafafa")
    ax.grid(True)
    
    fname = f"exports/lorenz/{filename}.png"

    plt.savefig(fname, bbox_inches='tight', facecolor="#fafafa")
    plt.close(fig)
    return x, y


def gini(x, y):
    """
    Renvoie l'indice de Gini du graphe duquel on a calculé x et y dans lorenz
    """
    if len(x) < 3 or len(y) < 3:
        return 0.0
    g = 0
    for i in range(1,len(x)-1):
        g += (x[i+1]-x[i])*(y[i] + 0.5*(abs(y[i+1]-y[i])))
    return 1 - 2*g
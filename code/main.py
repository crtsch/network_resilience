#-----         IMPORTS         -----#


import graphe
import metriques

import random
import time





#-----    FONCTION DE TEST     -----#

start = time.time()

for i in range(1, 11):

    print(f"Génération du graphe {i}")
    
    n = random.randint(5, 30)
    d = random.randint(15, 40) / 100

    graphe.generer(n, d, f"graphe_{i}")

    print(f"Importation du graphe {i}")
    
    g = graphe.from_json(f"../exports/exemples/graphe_{i}")
    
    print(f"Calculs sur le graphe {i}")

    Delta_temp = graphe.matrice_adjacence(g)
    beta = metriques.beta_defaut(Delta_temp)
    
    Delta = graphe.matrice_adjacence(g, 1, beta)

    graphe.to_img(g, f"graphe_{i}")

    x, y = metriques.lorenz(Delta, f"lorenz_{i}")
    print(f"GINI {i} : {metriques.gini(x, y)}")

end = time.time()

print(f"Durée d'exécution : {end-start} secondes ({(end-start)/60} minutes)")
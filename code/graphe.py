#-----         IMPORTS         -----#


import metriques

import json
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
from collections import deque





#-----    FONCTIONS  GRAPHE    -----#


def from_json(fichier):
    """
    Convertit un fichier JSON en graphe NetwokX
    Le fichier doit être dans le dossier imports, sans l'extension ".json"
    """
    with open(f"imports/{fichier}.json", "r", encoding="utf-8") as f:
        data = json.load(f)
 
    G = nx.Graph()
 
    for arete in data.get("aretes", []):
        G.add_edge(
            arete["from"],
            arete["to"],
            w=arete.get("w", 1.0),
        )
 
    return G


def to_json(G, nom):
    """
    Convertit un graphe NetworkX en fichier JSON
    Le fichier sera dans le dossier exports
    """
    data = {
        "noeuds": list(G.nodes()),
        "aretes": [
            {"from": u, "to": v, "w": attrs.get("w", 1.0)}
            for u, v, attrs in G.edges(data=True)
        ],
    }
 
    with open(f"exports/{nom}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def to_img(G, filename="graphe", titre="", taille=(10, 7)):
    """
    Exporte un graphe en image
    Le fichier sera dans le dossier exports
    """
    fig, ax = plt.subplots(figsize=taille)
    pos = nx.spring_layout(G, seed=42)
 
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color="#4C72B0", node_size=600)
    nx.draw_networkx_labels(G, pos, ax=ax, font_color="white", font_weight="bold")
    nx.draw_networkx_edges(G, pos, ax=ax, width=1.5, alpha=0.7)
 
    poids_labels = {(u, v): f"{attrs.get('w', 1.0)}" for u, v, attrs in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=poids_labels, ax=ax, font_size=9, bbox=dict(color='#fafafa'))
 
    if titre != "":
        ax.set_title(titre, fontsize=14, fontweight="bold")
    ax.axis("off")
    plt.tight_layout()
    plt.savefig(f"exports/{filename}.png", facecolor="#fafafa", dpi=150, bbox_inches="tight")
    plt.close(fig)


def matrice_adjacence(G, etat=1, beta=1):
    """
    Renvoie la matrice d'adjacence de G
    - Si etat = 1 : matrice pondérée par e^{-beta*w_ij}
    - Si etat = 2 : matrice non pondérée (1 si l'arête existe, 0 sinon)
    - Sinon, matrice pondérée par w_ij
    """
    noeuds = list(G.nodes())
    n = len(noeuds)
    index = {noeud: i for i, noeud in enumerate(noeuds)}
 
    if etat == 1 or etat == 2:
        matrice = np.zeros((n, n), dtype=float)
    else:
        matrice = np.full((n, n), fill_value=np.inf, dtype=float)

    for u, v, attrs in G.edges(data=True):
        poids = attrs.get("w", 1.0)
        i, j = index[u], index[v]
        if etat == 1:
            poids = np.exp(-(beta * poids))
        elif etat == 2:
            poids = 1.0
        matrice[i, j] = poids
        matrice[j, i] = poids
 
    return matrice


def cycles_fondamentaux_sommet(Delta, s):
    """
    Renvoie la liste des cycles fondamentaux de G de matrice d'adjacences Delta à partir du sommet s
    L'arbre est construit par DFS
    """
    n = len(Delta)
    
    # 1. Arbre couvrant
    racine = s
    parent = {i: None for i in range(n)}
    profondeur = {i: 0 for i in range(n)}
    visites = {racine}
    file = deque([racine])
    aretes_arbre = []
    
    while file:
        i = file.popleft()
        for j in range(n):
            if not np.isinf(Delta[i, j]) and Delta[i, j] != 0 and j not in visites:
                visites.add(j)
                parent[j] = i
                profondeur[j] = profondeur[i] + 1
                file.append(j)
                aretes_arbre.append(tuple(metriques.quicksort((i, j))))

    # 2. Détermination des arêtes de G qui ne sont pas dans l'arbre
    aretes_hors_arbre = []
    set_arbre = set(aretes_arbre)
    for i in range(n):
        for j in range(i+1, n):
            if not np.isinf(Delta[i, j]) and Delta[i, j] != 0.:
                if tuple(metriques.quicksort((i, j))) not in set_arbre:
                    aretes_hors_arbre.append((i, j))
    
    # 3. Détermination des cycles pour chaque arête hors de l'arbre
    cycles_fonda = []
    for (i,j) in aretes_hors_arbre:
        path_i = [i]
        curr = i
        while parent[curr] is not None:
            curr = parent[curr]
            path_i.append(curr)
            
        path_j = [j]
        curr = j
        while parent[curr] is not None:
            curr = parent[curr]
            path_j.append(curr)
            
        ancetre_commun = None
        for node in path_i:
            if node in path_j:
                ancetre_commun = node
                break
        
        partie_i = path_i[:path_i.index(ancetre_commun) + 1]
        partie_j = path_j[:path_j.index(ancetre_commun) + 1]
        
        partie_j.reverse()

        cycle = partie_i + partie_j
        cycles_fonda.append(cycle)
    
    return cycles_fonda


def liste_cycles_fondamentaux(Delta):
    """
    Renvoie la liste des cycles fondamentaux de G de matrice d'adjacences Delta (ensemble des cycles à partir de tous les sommets)
    """
    n = len(Delta)
    liste = []
    for i in range(0, n-1):
        liste.append(cycles_fondamentaux_sommet(Delta, i))


def generer(n=20, d=0.3, filename="graphe"):
    """
    Génère un graphe à n sommets, une densité d'arêtes de d, et l'enregistre en json
    Dans filename, ne pas préciser le .json
    """
    edges = []
    edge_set = set()

    nodes = list(range(n))
    random.shuffle(nodes)
    for i in range(1, n):
        s = nodes[i]
        t = nodes[random.randint(0, i-1)]
        edges.append({"from": s, "to": t, "w": random.randint(1, 20)})
        edge_set.add((min(s, t), max(s, t))) 

    for s in range(n):
        for t in range(s + 1, n):
            if (s, t) in edge_set:
                continue
            if random.random() < d:
                edges.append({"from": s, "to": t, "w": random.randint(1, 20)})
                edge_set.add((s, t))

    with open(f"./exports/exemples/{filename}.json", "w", encoding="utf-8") as f:
        json.dump({"noeuds": list(range(n)), "aretes": edges}, f, indent=4)





#-----  ALIAS DE FONCTIONS NX  -----#

def nouveau():
    """Renvoie un graphe non orienté pondéré vide"""
    return nx.Graph()


def ajouter_arete(G, s, t, w):
    """
    Ajoute l'arête (s, t) à G avec la pondération w, modifie la pondération si elle existe déjà
    """
    if G.has_edge(s, t):
        G[s][t]["w"] = w
    else:
        G.add_edge(s, t, w=w)


def supprimer_arete(G, s, t):
    """
    Supprime l'arête (s, t) de G
    """
    if not G.has_edge(s, t):
        raise Exception("supprimer_arete : arête inexistante")
    G.remove_edge(s, t)


def sommets(G):
    """
    Renvoie la liste triée des sommets de G
    """
    try:
        return metriques.quicksort(G.nodes())
    except TypeError:
        return list(G.nodes())
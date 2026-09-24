#-----         IMPORTS         -----#


import numpy as np



#-----        FONCTIONS        -----#


def det(M):
    """
    Calcule le déterminant de M (par décomposition LU)
    """
    if M.ndim != 2 or M.shape[0] != M.shape[1]:
        raise Exception("det : matrice non carrée")
    return np.linalg.det(M)


def id(n):
    return np.eye(n, dtype=float)
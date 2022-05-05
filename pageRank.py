#===========================================================#
# Mathématiques Discrètes - Projet PageRank                 #
# Auteurs - Colla Quentin, Maes Gilles, Kheirallah Cédric   #
#===========================================================#
import numpy as np
import csv

def pageRankLinear(A, v, alpha = 0.9):
    """
    Algorithme de PageRank méthode linéaire
    :param A: matrice d’adjacence d’un graphe dirigé, pondéré et régulier nommé G (non-négative)
    :param v: vecteur de personnalisation unique (non-négatif)
    :param alpha: paramètre de téléportation α compris entre 0 et 1 (0.9 par défaut et pour les résultats à présenter)
    :return x: un vecteur contenant les scores d’importance des nœuds ordonnés dans le même ordre que la matrice d’adjacence.
    """
    x = np.copy(v)
    return x

def pageRankPower(A, v, alpha = 0.9):
    """
    Algorithme de PageRank 'power method'
    :param A: matrice d’adjacence d’un graphe dirigé, pondéré et régulier nommé G (non-négative)
    :param v: vecteur de personnalisation unique (non-négatif)
    :param alpha: paramètre de téléportation α compris entre 0 et 1, α ∈]0,1[ (0.9 par défaut et pour les résultats à présenter)
    :return x: un vecteur contenant les scores d’importance des nœuds ordonnés dans le même ordre que la matrice d’adjacence.
    """
    x = np.copy(v)
    return x


if __name__ == '__main__':
    file = open('Adjacency_matrix_A.csv')
    csvreader = csv.reader(file)
    A = np.zeros((10, 10))
    index = 0
    for row in csvreader:
        if index == 0: row[0] = row[0][-1]
        A[index] = row
        index += 1
    file.close()
    # #               A, B, C, D, E, F, G, H, I, J
    # A = np.matrix([[0, 5, 0, 3, 0, 0, 0, 0, 0, 0],  # A
    #                [3, 0, 2, 0, 1, 0, 4, 0, 0, 0],  # B
    #                [0, 0, 0, 4, 0, 3, 0, 0, 0, 0],  # C
    #                [1, 0, 0, 0, 0, 2, 0, 0, 0, 0],  # D
    #                [0, 0, 5, 0, 0, 0, 2, 0, 0, 0],  # E
    #                [0, 0, 0, 0, 4, 0, 0, 2, 0, 0],  # F
    #                [0, 0, 0, 0, 3, 0, 0, 3, 0, 0],  # G
    #                [0, 0, 0, 0, 0, 1, 0, 0, 0, 4],  # H
    #                [0, 0, 0, 3, 0, 5, 0, 0, 0, 2],  # I
    #                [0, 0, 0, 0, 0, 0, 5, 0, 4, 0]]) # J
    v = np.array([0.1427, 0.0996, 0.0957, 0.1161, 0.0111, 0.2162, 0.1438, 0.0513, 0.0565, 0.067])
    alpha = 0.9
    print("INPUTS :\n--------")
    print("A = \n", A, "\nv = ", v, "\nalpha = ", alpha, sep="")
    print("===========================================================================")
    print("OUTPUTS :\n---------")
    print("Linear:\n", pageRankLinear(A, v), sep="")
    print("Power:\n", pageRankPower(A, v), sep="")

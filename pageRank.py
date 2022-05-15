#===========================================================#
# Mathématiques Discrètes - Projet PageRank                 #
# Auteurs - Colla Quentin, Maes Gilles, Kheirallah Cédric   #
#===========================================================#
import numpy as np
import csv

def pageRankLinear(A, v, alpha=0.9):
    """
    Algorithme de PageRank méthode linéaire
    :param A: matrice d’adjacence d’un graphe dirigé, pondéré et régulier nommé G (non-négative)
    :param v: vecteur de personnalisation unique (non-négatif)
    :param alpha: paramètre de téléportation α compris entre 0 et 1 (0.9 par défaut et pour les résultats à présenter)
    :return x: un vecteur contenant les scores d’importance des nœuds ordonnés dans le même ordre que la matrice d’adjacence.
    """
    # Matrice de probabilités de transition P
    for i in range(len(A)):
        A[i] /= np.sum(A[i])
    P = A.T

    # Résoudre le système linéaire creux (I - alpha*P) . x = (1-alpha)*v
    I = np.eye(len(A), len(A))
    x = np.linalg.solve(I - (alpha*P), (1-alpha)*v)
    if verbose: print("Système linéaire :\n", I - (alpha*P), "\n", (1-alpha)*v, sep="")

    return x

def pageRankPower(A, v, alpha=0.9):
    """
    Algorithme de PageRank 'power method'
    :param A: matrice d’adjacence d’un graphe dirigé, pondéré et régulier nommé G (non-négative)
    :param v: vecteur de personnalisation unique (non-négatif)
    :param alpha: paramètre de téléportation α compris entre 0 et 1, α ∈]0,1[ (0.9 par défaut et pour les résultats à présenter)
    :return x: un vecteur contenant les scores d’importance des nœuds ordonnés dans le même ordre que la matrice d’adjacence.
    """
    if verbose: print("Matrice d'adjacence A =\n", A, sep="")

    # Matrice de probabilités de transition P
    for i in range(len(A)):
        A[i] /= np.sum(A[i])
    P = A.T
    if verbose: print("Matrice de probabilités de transition P =\n", P, sep="")

    # Itérer sur la matrice G
    x = v/sum(v)
    G = (alpha*P) + (1-alpha)/len(A)
    if verbose: print("Matrice Google G =\n", G, sep="")
    for i in range(200):
        x = G @ x
        if (i < 3) and verbose: print("Vecteur de scores à l'itération ", i + 1, " =\n", x, sep="")

    return x

if __name__ == '__main__':
    np.set_printoptions(linewidth=150)

    # Verbose, changez à True pour afficher les étapes demandées pour le projet
    verbose = True

    # Lecture de la matrice d'adjacence A à partir d'un fichier .csv
    file = open('Adjacency_matrix_A.csv')
    csvreader = csv.reader(file)
    A = np.zeros((10, 10))
    index = 0
    for row in csvreader:
        if index == 0: row[0] = row[0][-1]
        A[index] = row
        index += 1
    file.close()

    # Vecteur de personnalisation
    v = np.array([0.1427, 0.0996, 0.0957, 0.1161, 0.0111, 0.2162, 0.1438, 0.0513, 0.0565, 0.067])

    # Paramètre de téléportation (valeur par défaut = 0.9)
    alpha = 0.9

    print("pageRankLinear :")
    print("Vecteur de scores x =\n", pageRankLinear(np.copy(A), np.copy(v), alpha), sep="")
    print("===============================================================================================================")
    print("pageRankPower :")
    print("Vecteur de scores x =\n", pageRankPower(np.copy(A), np.copy(v), alpha), sep="")

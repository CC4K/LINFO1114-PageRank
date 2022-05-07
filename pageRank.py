#===========================================================#
# Mathématiques Discrètes - Projet PageRank                 #
# Auteurs - Colla Quentin, Maes Gilles, Kheirallah Cédric   #
#===========================================================#
import numpy as np
import csv

def printMatrixWithFloats(M):
    for i in range(len(M)):
        print("[[", end="")
        for j in range(len(M[i])):
            print("%.3f" % (M[i][j]), end=" ")
        print("]]")
def printVectorWithFloats(V):
    print("[", end="")
    for i in range(len(V)):
        print("%.4f" % (V[i]), end=" ")
    print("]")

def pageRankIteratif(A, v, alpha=0.9):
    """
    Algorithme de PageRank méthode linéaire
    :param A: matrice d’adjacence d’un graphe dirigé, pondéré et régulier nommé G (non-négative)
    :param v: vecteur de personnalisation unique (non-négatif)
    :param alpha: paramètre de téléportation α compris entre 0 et 1 (0.9 par défaut et pour les résultats à présenter)
    :return x: un vecteur contenant les scores d’importance des nœuds ordonnés dans le même ordre que la matrice d’adjacence.
    """
    def out_pointings(A_j):
        count = 0
        for j in range(len(A_j)):
            if A_j[j] != 0:
                count += A_j[j]
        return count
    x = np.copy(v)
    A_t = np.transpose(A)

    for iteration in range(len(x)):
        # formule : (1 – alpha) + alpha * ( (score lien X / nbr lien sortant de X) + ... + (score lien Z / nbr lien sortant de Z) )
        for i in range(len(x)):
            somme = 0
            for j in range(len(x)):
                if A_t[i][j] != 0:
                    somme += ((x[j] / out_pointings(A[j])) * A_t[i][j])
                    # print("somme += ((%f / %d) * %d)" % (x[j], out_pointings(A[j]), A_t[i][j]))
            x[i] = (1 - alpha) + alpha * somme
            # print("(%f) + %f * (%f) = %f" % (1-alpha, alpha, somme, x[i]))

    return x

def pageRankLinear(A, v, alpha=0.9):
    """
    Algorithme de PageRank méthode linéaire
    :param A_p: matrice d’adjacence d’un graphe dirigé, pondéré et régulier nommé G (non-négative)
    :param v: vecteur de personnalisation unique (non-négatif)
    :param alpha: paramètre de téléportation α compris entre 0 et 1 (0.9 par défaut et pour les résultats à présenter)
    :return x: un vecteur contenant les scores d’importance des nœuds ordonnés dans le même ordre que la matrice d’adjacence.
    """
    def out_pointings(A_j):
        count = 0
        for j in range(len(A_j)):
            if A_j[j] != 0:
                count += A_j[j]
        return count
    x = np.copy(v)
    A_p = np.copy(A)
    A_t = np.transpose(A)

    # Matrice d'adjacence transposée AKA de transition (correcte)
    for i in range(len(A_p)):
        A_p[i] /= out_pointings(A_p[i])
    P_t = np.transpose(A_p)
    # printMatrixWithFloats(P_t)

    # Vecteur des sommes par colonnes pondérés par somme total (jsp si utile vu qu'on nous donne un vecteur ¯\_(ツ)_/¯)
    tot = 0
    for i in range(len(A)):
        tot += sum(A[i])
    s = np.zeros(len(A_t))
    for i in range(len(A_t)):
        s[i] = sum(A_t[i]) / tot


    for iteration in range(100):
        x = P_t @ x

    # alpha il va où FOR F*CK SAKE ?!

    return x

def pageRankPower(A, v, alpha=0.9):
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
    v = np.array([0.1427, 0.0996, 0.0957, 0.1161, 0.0111, 0.2162, 0.1438, 0.0513, 0.0565, 0.067])
    alpha = 0.9
    print("A = \n", A, "\nv = ", v, "\nalpha = ", alpha, sep="")
    print("===========================================================================")
    print("Iteratif:")
    printVectorWithFloats(pageRankIteratif(A, v, alpha))
    print("\nLinear:")
    printVectorWithFloats(pageRankLinear(A, v, alpha))
    print("\nPower:")
    printVectorWithFloats(pageRankPower(A, v, alpha))

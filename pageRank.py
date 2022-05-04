# Projet Mathématiques Discrètes
import numpy as np

def pageRankLinear(A, v, alpha = 0.9):
    x = np.copy(v)
    return x

def pageRankPower(A, v, alpha = 0.9):
    x = np.copy(v)
    return x


if __name__ == '__main__':
    A = np.matrix([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
    v = np.array([0.1427, 0.0996, 0.0957, 0.1161, 0.0111, 0.2162, 0.1438, 0.0513, 0.0565, 0.067])
    alpha = 0.9
    print("A = \n", A, "\nv = ", v, "\nalpha = ", alpha, "\n", sep="")
    print("Linear:\n", pageRankLinear(A, v), sep="")
    print("Power:\n", pageRankPower(A, v), sep="")

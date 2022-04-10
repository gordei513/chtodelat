from numpy import array, concatenate
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box

a = array([
    [1, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4],
    [2.0, 1.0, 4.0, 3]
], dtype=float)
b = array([5, 6, 7, 8], dtype=float)

def vgauss(a, b):
    ab = concatenate((a, array([b]).T), axis=1)
    dim = len(ab)
    ab[0] = ab[0]/ab[0, 0]
    for k in range(1, dim):
        for i in range(k, dim):
            ab[i] = (ab[i] - ab[k-1] * ab[i, k-1])/ab[k-1, k-1]
            ab[i] = ab[i]/(ab[i, i])
    for i in range(dim - 1, -1, -1):
        for k in range(i-1, -1, -1):
            ab[k] = ab[k]-ab[i]*ab[k, i]
    x = ab[:, -1]
    return x
vgauss(a, b)
oob_solution = solve_out_of_the_box(a, b)
solution = vgauss(a, b)
print(solution)
print("Макс отклонение компоненты решения:", norm(solution-oob_solution, ord=1))

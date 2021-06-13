def mat_mul(matA, matB):
    matC = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                matC[i][j] = (matC[i][j] + (matA[i][k] * matB[k][j]) % (10**9+7))% (10**9+7)
    return matC

def mat_power(matA, k):
    if k == 0:
        return [[1, 0], [0, 1]]
    elif k == 1:
        return matA
    else:
        tmp = mat_power(matA, k//2)
        if k%2 == 1:
            return mat_mul(mat_mul(tmp, tmp), matA)
        else:
            return mat_mul(tmp, tmp)

n, k = [int(x) for x in input().split()]

matA = [[0, 1], [1, 1]]
matA = mat_power(matA, k*2)
print(((matA[0][0] + matA[0][1]) * n) % (10**9+7))
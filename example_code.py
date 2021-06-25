from .matrix.KroneckerProduct import Kronecker

matrix1 = [[1,2],[3,4],[1,0]]
matrix2 = [[0,5,2],[6,7,3]]

kron = Kronecker(matrix1,matrix2)

kron.multiply()
kron.display_result()



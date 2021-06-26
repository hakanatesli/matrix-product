# matrix-product

This package needed for Matrix Multiplication with Python.

## What matrix multiplications does it contain?

 * Kronecker Product
 * Hadamard Product
 * Frobenius Product
 * Khatri Rao Column Wise Product
 * Khatri Rapor Face Splitting Product
 
## Installation
 
 `pip install matrix-product`

## Example

```
    from matrix import Kronecker
    
    matrix1 = [[1,2],[3,4],[1,0]]
    matrix2 = [[0,5,2],[6,7,3]]

    kron = Kronecker(matrix1,matrix2)

    kron.multiply()
    kron.display_result()
```
 

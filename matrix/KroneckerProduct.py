from .Multiplication import Multiplication

class Kronecker(Multiplication):

    def __init__(self,matrix1,matrix2):
        super().__init__(self,matrix1,matrix2)
    
    def ismultiplyable(self):
        super().ismultiplyable()
    
    def multiply(self):

        if self.ismultiplyable():
            m = len(self.matrix1)
            n = len(self.matrix1[0])
            p = len(self.matrix2)
            r = len(self.matrix2[0])

            super().fill_result((m * p), (n * r))

            for i in range(0, m):
            
                for k in range(0, p):
        
                    for j in range(0, n):
        
                        for l in range(0, r):
        
                            self.result[i + l + 1][j + k + 1] = self.matrix1[i][j] * self.matrix2[k][l]
        else:
            print("Matrices are not multiplyable!")
                

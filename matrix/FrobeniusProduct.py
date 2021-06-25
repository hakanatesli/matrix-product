from .Multiplication import Multiplication

class Frobenius(Multiplication):
    """
    Wiki: https://en.wikipedia.org/wiki/Frobenius_inner_product
    """
    def __init__(self,matrix1,matrix2):
        super().__init__(self,matrix1,matrix2)
    
    def ismultiplyable(self):
        """
        INPUT: No Input
        OUTPUT: ismultiplyable : bool

        DESC: Can matrices be multiplied?
        """
        m = len(self.matrix1)
        n = len(self.matrix1[0])
        p = len(self.matrix2)
        r = len(self.matrix2[0])

        if super().ismultiplyable():
            if m == p and n == r:
                return True
        else:
            return False
        
    
    def multiply(self):
        """
        DESC: 
        """
        if self.ismultiplyable():
            m = len(self.matrix1)
            n = len(self.matrix1[0])
            p = len(self.matrix2)
            r = len(self.matrix2[0])

            self.result = 0

            for i in range(0, m): 
         
                for k in range(0, n):
                    self.result += self.matrix1[i][k] * self.matrix2[i][k]
        else:
            print("Matrices are not multiplyable!")
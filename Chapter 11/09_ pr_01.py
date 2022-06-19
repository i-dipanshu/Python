class C_2dVec:
    def __init__(self, i , j):
        self.icap = i
        self.jcap = j
    
    def __str__(self):
        return f"{self.icap}i, {self.jcap}j"
        
class C_3dVec(C_2dVec):
    def __init__(self, i , j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i, {self.jcap}j, {self.kcap}k"
       

v2d = C_2dVec(4, 8)
v3d = C_3dVec(2, 3, 5)
print(v2d)
print(v3d)

    




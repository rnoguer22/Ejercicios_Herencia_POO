class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def traslacion(self, u, v):
        self.x = self.x + u
        self.y = self.y + v
        return self.x, self.y

class Punto3D(Punto2D):
    def __init__(self, x, y, z):
        super().__init__(x,y)
        self.z = z
    def traslacion2(self ,a,b,c): 
        self.x = self.x + a
        self.y = self.y + b
        self.z = self.z + c
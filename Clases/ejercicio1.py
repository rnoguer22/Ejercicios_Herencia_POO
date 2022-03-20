class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def traslacion(self, u, v):
        self.x = self.x + u
        self.y = self.y + v
        return self.x, self.y
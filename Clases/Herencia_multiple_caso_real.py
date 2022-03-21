class Pared:
    #Constructor
    def __init__(self, orientacion):
        self.orientacion = orientacion
        
class Ventana(Pared):
    #Constructor
    def __init__(self, orientacion, superficie):
        super().__init__(orientacion)
        self.superficie = superficie
    
    def get_area(self):
        return self.superficie

class Casa(Ventana):
    #Constructor
    def __init__(self, paredes, orientacion, superficie):
        super().__init__(orientacion, superficie)
        self.paredes = paredes
    
    def superficie_acristalada(self):
        return sum(self.paredes.superficie)
class Ventana:
    #Constructor
    def __init__(self, ventana, superficie):
        self.ventana = ventana
        self.superficie = superficie
    
    def get_area(self):
        return self.superficie

class Pared:
    #Constructor
    def __init__(self, orientacion):
        Ventana.__init__(self)
        self.orientacion = orientacion


class Casa:
    #Constructor
    def __init__(self, paredes):
        Pared.__init__(self)
        self.paredes = paredes
    
    def superficie_acristalada(self):
        return sum(self.paredes.superficie)
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
        self.orientacion = orientacion


class Casa:
    #Constructor
    def __init__(self, paredes):
        self.paredes = paredes
    
    def superficie_acristalada(self):
        

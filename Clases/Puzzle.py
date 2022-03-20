#Define la clase padre
class Base: 
    #Define el constructor
    def __init__(self): 
        #Los atributos de la clase
        self.a = "a" 
        self.b = "b" 
        self.c = "c" 
    #Define los métodos de la clase
    def A(self): 
        print(self.a) #Imprime por pantalla el valor correspondiente a self.a
 
    def B(self): 
        print(self.b) #Imprime por pantalla el valor correspondiente a self.b
 
    def C(self): 
        print(self.c) #Imprime por pantalla el valor correspondiente a self.c

#Define la clase hijo 
class Derivada(Base): 
    #Define el constructor
    def __init__(self): 
        self.a = "aa" #Al definir este atributo antes de la herencia del método siguiente no tiene ningun efecto
        super().__init__() #Hereda el metodo __init__ de la clase padre
        self.c = "cc" #Cambia el atributo self.c del método heredado
 
    def A(self): 
        print(self.a) #Imprime por pantalla el valor de self.b
 
    def B(self): 
        self.b = "bb" #Cambia el atributo self.b definido en el constructor 
        super().B() #Hereda el método B de la clase padre 
        print(self.b) #Imprime por pantalla el valor de self.b
 

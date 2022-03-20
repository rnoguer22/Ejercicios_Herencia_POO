from Clases.ejercicio1 import *
from Clases.Puzzle import *

if __name__ == "__main__":
    
    #EJERCICIO 1
    punto1 = Punto2D(3,2)
    punto1.traslacion(1,1)
    print("El nuevo valor de punto1 es ({},{})".format(punto1.x,punto1.y))

    #EJERCICIO 2
    base = Base() #define base como objeto de la clase padre Base
    derivada = Derivada() #define derivada como objeto de la clase hijo Derivada
    base.A() #
    derivada.A() 
    print() 
    base.B() 
    derivada.B() 
    base.C() 
    derivada.C() 
    derivada = base 
    derivada.C() 
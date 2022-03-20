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
    base.A() #output: a, utiliza el método A de la clase padre 
    derivada.A() #output: a, utiliza el método A
    base.B() #output: b, utiliza el método B de la clase padre
    derivada.B() #output: bb, utiliza el método B de la clase hijo
    base.C() #output: c, utiliza el método C de la clase padre
    derivada.C() #output: cc, utiliza el método C de la clase hijo con sus atributos
    derivada = base #define derivada como el mismo objeto que base, por lo que será un objeto de la clase padre
    derivada.C() #output: c, utiliza el método C de la clase padre
from Clases.ejercicio1 import *
from Clases.Puzzle import *
from Clases.Herencia_multiple_caso_real import *

if __name__ == "__main__":
    
    #EJERCICIO 1
    punto1 = Punto2D(3,2)
    punto1.traslacion(1,1)
    print("El nuevo valor de punto1 es ({},{})".format(punto1.x,punto1.y))

    punto2 = Punto3D(1,1,1)
    punto2.traslacion2(1, 2, 3)
    print("El nuevo valor de punto2 es ({},{},{})".format(punto2.x,punto2.y,punto2.z))

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

    #EJERCICIO 3
    class A:
        def __init__(self,a):
            self.a = a
    class B(A):
        def __init__(self, b, a):
            self.b = b
            A.__init__(self, a)
            
    class C(A):
        def __init__(self, c, a):
            self.c = c
            A.__init__(self, a)
    class D(B, C):
        def __init__(self,d, a, b, c):
            self.d = d
            B.__init__(self, a, b)
            C.__init__(self, a, c)

    #EJERCICIO 4
    # Instanciación de las paredes 
    pared_norte = Pared("NORTE") 
    pared_oeste = Pared("OESTE") 
    pared_sur = Pared("SUR") 
    pared_este = Pared("ESTE") 
    # Instanciación de las ventanas 
    ventana_norte = Ventana(pared_norte, 0.5) 
    ventana_oeste = Ventana(pared_oeste, 1) 
    ventana_sur = Ventana(pared_sur, 2) 
    ventana_este = Ventana(pared_este, 1) 
    # Instanciación de la casa con las 4 paredes 
    casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este]) 
    print(casa.superficie_acristalada()) 
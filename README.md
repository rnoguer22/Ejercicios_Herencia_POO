# Ejercicios_Herencia_POO

# EJERCICIO1

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
            
<img width="233" alt="2022-03-20 (2)" src="https://user-images.githubusercontent.com/91720991/159174187-b7d7d416-4c28-4c0b-a9e5-46cc0836625f.png">

# EJERCICIO 2
```#Define la clase padre
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
```

![UML puzzle](https://user-images.githubusercontent.com/91722847/159286685-764df47a-a49b-46e4-a3df-a9e798f2c8ff.png)

# EJERCICIO 3



# EJERCICIO 4
```class Pared:
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
```


![UML Ejercicio 4](https://user-images.githubusercontent.com/91722847/159286626-3aa56d3b-6898-488f-a278-f6b4b3e51643.png)

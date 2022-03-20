class A:
    def __init__(self,a):
        self.a = a
class B(A):
    def __init__(self, b):
        self.b = b
        
class C(A):
    def __init__(self, c):
        self.c = c

class D(B, C):
    def __init__(self,d, a, b, c):
        self.d = d
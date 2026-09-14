from __future__ import annotations

class Fraction:
    def __init__(self,num:int , den:int):
        self.__num = num
        self.__den= den

    def get_fraccion(self):
        return self.__num, self.__den   

    def __str__(self) :
        return (f"{self.__num} / {self.__den} ")

    def gcd(self) :
        a= self.__num
        b = self.__den

        while b > 0 :
            a, b = b , a % b
        return  a

    def simplify(self) :
        gcd= self.gcd()
        self.__num  //= gcd
        self.__den  //= gcd


    def __add__(self, otro: Fraction) :

        fraccion = otro.get_fraccion()
        self.__num = self.__num * fraccion[1]  + fraccion[0] * self.__den
        self. __den *=  fraccion[1]
        self.simplify()


'''
hola = Fraction(25,30)
adios  = Fraction(40,45)   

hola+adios
print(hola)

'''




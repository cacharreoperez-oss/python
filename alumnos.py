'''
Ejercicio 1
Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno.
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
'''


class Estudiante:
    def __init__(self, nombre, apellido1, apellido2, nota):
        self.nombre = [nombre, apellido1, apellido2]
        self.nota = nota

    def __str__(self):
        return f'Nombre: {self.nombre[0]} {self.nombre[1]} {self.nombre[2]}, Nota: {self.nota}'

    def mostrar(self):
        print(self.__str__())

    def mensaje(self):
        if self.nota >= 5:
            estado = 'aprobado'
        else:
            estado = 'suspendido'
        nombre_completo = f'{self.nombre[0]} {self.nombre[1]} {self.nombre[2]}'
        return f'{nombre_completo} tiene una nota de {self.nota} y está {estado}.'


if __name__ == '__main__':
    alumno = Estudiante('Ana', 'García', 'López', 7)
    alumno.mostrar()
    print(alumno.mensaje())

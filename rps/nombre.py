'''
Ejercicio 3.6 Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior
 a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre
 por pantalla el grupo que le corresponde.
'''

nombre = input('Nombre: ')
sexo = input('Sexo: ').lower()
let_nom = nombre[0].lower()

if (sexo == 'm' and let_nom < 'm') or (sexo == 'h' and let_nom > 'n'):
    print('Grupo A')
else:
    print('Grupo B')
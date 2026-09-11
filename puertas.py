puertas=[1,0,0,1,0,2,0,2,2,1,0,0,3,0,0,0,3]
longitud = len(puertas)
contador = 0
indice = []
proceso = 0
puertas_obj = []
class Puerta:
    def __init__(self, id, frecuencia):
        self.id = id
        self.frecuencia = frecuencia
        self.estado = 1 if frecuencia > 0 else 0  

    def cambiar_estado(self, frecuencia):
        self.estado = 1 if frecuencia > 0 else 0 
        self.frecuencia = frecuencia

for door in puertas:
    pasillo = Puerta(contador, door)
    puertas_obj.append(pasillo)
    contador += 1
    print(f'Puerta {pasillo.id}: Estado: {pasillo.estado}, Frecuencia: {pasillo.frecuencia}')  

contador = 0
for door in puertas:
    if door > 0:
        indice.append(contador)
        proceso += 1
    if proceso == 2:
        if puertas[indice[0]] == puertas[indice[1]]:
            posiciones = indice[1] - indice[0] - 1
            for i in range(indice[0] + 1, indice[1]):
                pasillo = puertas_obj[i]
                pasillo.cambiar_estado(puertas[indice[0]])
            proceso = 0    
   
    contador += 1

print("\nPuertas del pasillo:")
for pasillo in puertas_obj:
    print(
        f"Puerta {pasillo.id}: "
        f"Estado: {pasillo.estado}, "
        f"Frecuencia: {pasillo.frecuencia}"
    )
    
       


    
                


    

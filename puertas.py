puertas=[1,0,0,1,0,2,0,2,2,1,0,0,3,0,0,0,3]
longitud = len(puertas)
contador = 0
class Puerta:
    def __init__(self, id, frecuencia):
        self.id = id
        self.frecuencia = frecuencia
        self.estado = 1 if frecuencia > 0 else 0  

        def cambiar_estado(self, frecuencia):
            self.estado = 1 if frecuencia > 0 else 0 
            self.frecuencia = frecuencia

for door in puertas:
    puerta = Puerta(contador, door)
    contador += 1
    print(f'Puerta {puerta.id}: Estado: {puerta.estado}, Frecuencia: {puerta.frecuencia}')  
    

    
                


    
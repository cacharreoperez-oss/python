# Frecuencia de cada puerta del pasillo.
puertas=[1,0,0,1,0,2,0,2,2,1,0,0,3,0,0,0,3]
longitud = len(puertas)
contador = 0
indice = []
proceso = 0
# Lista donde se guardan las instancias de Puerta.
puertas_obj = []

class Puerta:
    # Crea una puerta con su identificador y frecuencia inicial.
    def __init__(self, id, frecuencia):
        self.id = id
        self.frecuencia = frecuencia
        self.estado = 1 if frecuencia > 0 else 0  

    # Actualiza la frecuencia y activa o desactiva la puerta.
    def cambiar_estado(self, frecuencia):
        self.estado = 1 if frecuencia > 0 else 0 
        self.frecuencia = frecuencia

# Convierte cada frecuencia en un objeto Puerta.
for door in puertas:
    pasillo = Puerta(contador, door)
    puertas_obj.append(pasillo)
    contador += 1
    # se impñrime para ver si va bien y comprobar con el resultado final
    print(f'Puerta {pasillo.id}: Estado: {pasillo.estado}, Frecuencia: {pasillo.frecuencia}')  

contador = 0
# Guarda las posiciones de las puertas que tienen frecuencia.
indice = [i for i, frecuencia in enumerate(puertas) if frecuencia > 0]

# Compara cada pareja consecutiva de puertas activas.
for inicio, fin in zip(indice, indice[1:]):
    if puertas[inicio] == puertas[fin]:
        # Activa las puertas situadas entre las dos puertas coincidentes.
        for i in range(inicio + 1, fin):
            pasillo = puertas_obj[i]
            pasillo.cambiar_estado(puertas[inicio])

# Muestra el estado final de todas las puertas.
print("\nPuertas del pasillo:")
for pasillo in puertas_obj:
    print(
        f"Puerta {pasillo.id}: "
        f"Estado: {pasillo.estado}, "
        f"Frecuencia: {pasillo.frecuencia}"
    )
    
       


    
                


    

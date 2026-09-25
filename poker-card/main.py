# Here you have the suits symbols:
# ♣ ◆ ❤ ♠
from pathlib import Path

class InvalidCardError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Card:
    # Diccionario para almacenar los glifos cargados desde el archivo
    # Ejemplo de estructura: {'♣': ['🃑', '🃒', ...], '♠': ['🂡', ...]}
    _GLIFOS: dict[str, list[str]] = {}

    @classmethod
    def _cargar_glifos(cls, ruta_fichero: str = r"C:\Users\profesormanana\myproject\poker-card\data\glyphs.dat") -> None:
        """Carga el fichero glyphs.dat una sola vez en memoria."""
        if cls._GLIFOS:
            return  # Ya se cargaron previamente

        path = Path(ruta_fichero)
        if not path.exists():
            raise FileNotFoundError(f"No se encontró el fichero de glifos en: {ruta_fichero}")

        with open(path, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                palo_simbolo, cartas_csv = linea.split(":")
                cls._GLIFOS[palo_simbolo] = cartas_csv.split(",")

    def __repr__(self) -> str:
        """Devuelve el glifo Unicode de la carta."""
        # Obtenemos la lista de glifos asociada al palo
        lista_glifos = self._GLIFOS.get(self.suit)
        
        if not lista_glifos:
            return f"Carta({self.value}, {self.suit})"

        # Convertimos el valor (1..13) a índice base 0 (0..12)
        indice = self.value - 1
        
        if 0 <= indice < len(lista_glifos):
            return lista_glifos[indice]
        
        return f"Carta({self.value}, {self.suit})"

    def get_carta(self):
        return (self.value, self.suit)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return False 
        return self.get_carta() == other.get_carta()

    def __lt__(self, other):
        # Comparamos sólo el número
        if other.get_carta()[0] == 1  and self.value != 1:
            return True
        if self.value == 1:
            return False
        return self.value > other.get_carta()[0]

    def __gt__(self, other):
        # Comparamos sólo el número
        if other.get_carta()[0] == 1:
            return False
        if self.value == 1:
            return True
        return self.value < other.get_carta()[0]

    def __add__(self, other):
        # Suma valores
        self.value = self.value + other.get_carta()[0] if self.value + other.get_carta()[0] <= 13 else 1
        self.suit = self.suit if self.__eq__(other) else self.suit if self.__lt__(other) else other.get_carta()[1]

    def __init__(self, value: int | str, suit: str):            
        CARTAS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        PALOS = {'♣':'Treboles','◆':'Diamantes','❤':'Corazones','♠':'Picas' }
        # Aseguramos que los glifos estén cargados
        Card._cargar_glifos()
        if isinstance(value,int) and (value <1 or value > 13):
            raise InvalidCardError(f'{repr(value)} is not a supported value')
        if isinstance(value,str) and value not in CARTAS:
            raise InvalidCardError(f'{repr(value)} is not a supported symbol')
        if suit not in PALOS:
            raise InvalidCardError(f'{repr(suit)} is not a supported suit')
        # Crear atributos
        self.value = value if isinstance(value,int) else CARTAS.index(value) + 1
        self.suit = suit

carta1 = Card(10,'♠')
print(repr(carta1))
carta2 = Card('A','❤')
print(repr(carta2))
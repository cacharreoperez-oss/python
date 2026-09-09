jugador1='Tijera'
jugador2='Papel'

jugada=[jugador1,jugador2]
match jugada:
    case ['Piedra','Papel']:
        print('Gana jugador 2')
    case ['Papel','Piedra']:
        print('Gana jugador 1')
    case ['Piedra','Tijera']:
        print('Gana jugador 1')
    case ['Tijera','Piedra']:
        print('Gana jugador 2')
    case ['Papel','Tijera']:
        print('Gana jugador 2')
    case ['Tijera','Papel']:
        print('Gana jugador 1')
    case _:
        print('Empate')



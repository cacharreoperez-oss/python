def run(player1: str, player2: str) -> int:
    player1 = player1.lower()
    player2 = player2.lower()

    jugada = [player1, player2]
    match jugada:
        case ['rock', 'paper']:
            winner = 2
        case ['paper', 'rock']:
            winner = 1
        case ['rock', 'scissors']:
            winner = 1
        case ['scissors', 'rock']:
            winner = 2
        case ['paper', 'scissors']:
            winner = 2
        case ['scissors', 'paper']:
            winner = 1
        case _:
            winner = 0

    return winner


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

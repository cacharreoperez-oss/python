def run(items: list[int]) -> list[int]:
    # TODO
    if len(items) == 0:
        return []
    # Trocea la lista en dos partes
    mitad = len(items) // 2
    primer_parte = items[:mitad]
    segunda_parte = items[mitad:]

    # Revierte cada parte
    primer_parte.reverse()
    segunda_parte.reverse()

    # Combina las partes invertidas
    lista_invertida = primer_parte + segunda_parte

    # Imprime la lista invertida
    
    return lista_invertida


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

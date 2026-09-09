import queue
def run(letters: str) -> list[str]:
    # TODO

    cola_mayusculas = []
    cola_minusculas = []
    #queue = []

    for char in letters:
        if char == ' ':
            queue.extend(cola_mayusculas[::-1])
            queue.extend(cola_minusculas[::-1])
            cola_mayusculas.clear()
            cola_minusculas.clear()
        elif char.isupper():
            cola_mayusculas.append(char)
        elif char.islower():
            cola_minusculas.append(char)


    queue.extend(cola_mayusculas[::-1])
    queue.extend(cola_minusculas[::-1])

  
    return queue


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

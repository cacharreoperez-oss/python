def factorial(n):
    if n < 0:
        return None

    if n == 0:
        return 1

    resultado = 1
    for numero in range(1, n + 1):
        resultado *= numero

    return resultado


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(factorial)

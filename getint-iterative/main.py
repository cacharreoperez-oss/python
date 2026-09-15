# TODO
def getint():
    valor = None
    while True:
        try:
            valor = int(input('Give me an integer number: '))
        except ValueError:
            print('Not a valid integer. Try it again!')
        else:
            break
    return valor


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(getint)

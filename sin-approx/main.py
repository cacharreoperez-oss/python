def run(x: float) -> float:
    comun = 180 - x
    arriba = 4 * x * comun
    abajo = 40500 - x * comun
    sin = arriba / abajo
    return sin


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

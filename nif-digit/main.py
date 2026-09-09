def run(nif: str) -> str:
    # TODO
    letters = 'TRWAGMYFPDXBNJZSQVHLCKE'
    return f'{nif}{letters[int(nif) % 23]}'


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

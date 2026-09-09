def run(intcolor: int) -> str:
    # TODO
    hexcolor = format(intcolor, '06X')
    return f'#{hexcolor}'


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

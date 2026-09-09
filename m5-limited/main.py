def run(limit: int) -> None:
    # TODO
    n = 1
    while n < limit:
        if n % 5 == 0:
            print(n)
        n += 1


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

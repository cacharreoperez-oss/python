def run(u: list, v: list) -> float | None:
    if len(u) != len(v):
        return None

    dprod = 0
    for v1, v2 in zip(u, v):
        dprod += v1 * v2

    return dprod


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

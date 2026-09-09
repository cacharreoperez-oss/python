def run(arc_A: float) -> float:
    # area = arc_A ** 2
    PI = 3.14
    radius = (arc_A * 4) / (2 * PI)
    area = radius ** 2
    return area


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

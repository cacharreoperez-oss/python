import math

def run(a: int, b: int, c: int) -> tuple:
    
    discriminant = b**2 - 4*a*c
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    
    return x1, x2


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

def run(target_number: int) -> None:
    # TODO
    inten=0
    while True :
        my_num = input('Introduzca número: ')
        inten += 1
        if int(my_num) == target_number:
            print(f"Enhorabuena has encontrado el número en {inten} intentos ")
            break
        elif int(my_num) > target_number:
            print("Menor") 
        else :
            print("Mayor")   



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

import string


def run(input_path: str):
    with open(input_path, encoding='utf-8') as file:
        text = file.read().lower().replace('\n', ' ').replace('\r', ' ')

    palabras = [palabra.strip(string.punctuation) for palabra in text.split()]
    return max(palabras, key=len)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

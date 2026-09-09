def run(smb_path: str) -> tuple:
    # TODO
    host, path = smb_path[2:].split('/', 1)
    return host, f'/{path}'


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

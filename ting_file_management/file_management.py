import sys


def txt_importer(path_file):
    try:
        with open(path_file, "r") as file:
            data = file.read().split("\n")
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

    if not path_file.endswith(".txt"):
        return sys.stderr.write("Formato inválido\n")
    return data

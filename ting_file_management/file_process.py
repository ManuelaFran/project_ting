import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    process_exist = False
    for index in range(len(instance)):
        file = instance.search(index)
        if file["nome_do_arquivo"] == path_file:
            process_exist = not process_exist
            break

    if not process_exist:
        content = txt_importer(path_file)

        file_dict = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(content),
            "linhas_do_arquivo": content,
        }

        instance.enqueue(file_dict)
        return sys.stdout.write(f"{file_dict}\n")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""

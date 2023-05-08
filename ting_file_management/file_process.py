import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
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


def remove(instance: Queue):
    try:
        remove_file = instance.dequeue()
        file_name = remove_file["nome_do_arquivo"]
        return sys.stdout.write(
            f"Arquivo {file_name} removido com sucesso\n"
        )
    except IndexError:
        return sys.stdout.write("Não há elementos\n")


def file_metadata(instance: Queue, position):
    try:
        file = instance.search(position)
        return sys.stdout.write(f"{file}")
    except IndexError:
        return sys.stderr.write("Posição inválida")

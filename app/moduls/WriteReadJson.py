import json
import os

from project_conf import PATH_PROJECT


# Функция считывает данные с json файла
def read_json_file(name_file):
    """
    :param name_file:
    :return:
    """

    try:

        if os.path.exists(name_file):

            file = open(name_file, 'r', encoding='UTF-8')
            data = file.read()
            file.close()

            if len(data) == 0:
                return {}
            else:
                return dict(json.loads(data))

        else:
            file = open(name_file, 'w', encoding='UTF-8')
            file.close()

            return {}
    except Exception as e:
        return e


# Функция записывает данные в json файл
def write_json_file(name_file, data_json):
    """
    :param name_file:
    :param data_json:
    :return:
    """

    try:

        with open(name_file, 'w', encoding='UTF-8') as file:
            file.write(json.dumps(data_json))

    except Exception as e:
        return e


# Функция записывает и считывает данные c json файла
def write_read_json_file(name_file, *args):
    """
    :param name_file:
    :param args:
    :return:
    """

    path_file_json = os.path.join(PATH_PROJECT['base_path'], name_file)

    data = {args[0]: {'id': args[0], 'username': args[2], 'first_name': args[1], 'last_name': args[3]}}

    data_json = read_json_file(path_file_json)

    if data_json.get(str(args[0])) is None:

        data_json.update(data)
        write_json_file(path_file_json, data_json)




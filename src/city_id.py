import json


def receive_city_hh(path_hh, user_city):
    """
    поиск id городов по названию для hh.ru
    :param path_hh: путь к JSON файлу с id городов для hh
    :param user_city: города, указанные пользователем
    :return: id городов
    """
    with open(path_hh, "r", encoding="utf-8") as file:
        data_hh = json.load(file)
    city_id_hh = [city["id"] for area in data_hh for city in area["areas"] if city["name"].lower() in user_city]
    return city_id_hh


def receive_city_super_job(path_sj, user_city):
    """
    поиск id городов по названию для superjob.ru
    :param path_sj: путь к JSON файлу с id городов для superjob
    :param user_city: города, указанные пользователем
    :return: id городов
    """
    with open(path_sj, "r", encoding="utf-8") as file:
        data_sj = json.load(file)
    city_id_sj = [city["id"] for city in data_sj if city["title"].lower() in user_city]
    return city_id_sj

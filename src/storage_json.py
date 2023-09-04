import json
from abc import ABC, abstractmethod
from src.vacancy import Vacancy


class StarageJson(ABC):
    """
    Абстрактный класс для сохранения полученных вакансий
    """

    @abstractmethod
    def add_vacansies(self, vacansies_list):
        pass

    @abstractmethod
    def get_vacansies(self):
        pass

    @abstractmethod
    def remove_vacansies(self):
        pass


class VacansyJson(StarageJson):
    def __init__(self, path):
        """
        Класс для сохранения полученных вакансий в JSON файл
        :param path: путь для сохранения
        """
        self.path = path

    def add_vacansies(self, vacansies_list):
        """
        добавляет список вакансий по указанному пути в формате JSON
        :param vacansies_list: список вакансий
        """
        with open(self.path, "a", encoding="utf-8") as file:
            json.dump(vacansies_list, file, indent=4)

    def get_vacansies(self):
        """
        Сортирует список вакансий по значению зарплаты
        :return: отсортированный по зарплате список экземпляров класса Vacancy
        """
        with open(self.path, "r", encoding="utf-8") as file:
            parsed_vacansies = json.load(file)
        return sorted([Vacancy(**vac) for vac in parsed_vacansies], reverse=True)

    def remove_vacansies(self):
        """
        Удаляет все вакансии
        """
        empty_vacancies = ""
        with open(self.path, "w", encoding="utf-8") as file:
            file.write(empty_vacancies)

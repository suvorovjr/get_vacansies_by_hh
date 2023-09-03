import requests

from abc import ABC, abstractmethod


class Header(ABC):
    """
    Абстрактный класс для работы с сервисами по API
    """

    @abstractmethod
    def get_requests(self):
        pass

    @abstractmethod
    def get_vacancy(self):
        pass


class APIhhru(Header):
    """
    Класс для работы с hh.ru
    :keyword: ключевое слово для поиска вакансий
    """

    def __init__(self, keyword):
        self.keyword = keyword
        self.all_vacancies = []

    def get_requests(self):
        """
        парсит вакансии по ключевому слову, переданному при инициализации класса
        :return: список вакансий с сайта hh.ru
        """
        params = {
            "page": 0,
            "per_page": 100,
            "text": self.keyword,
            "only_with_salary": True
        }
        data = requests.get("https://api.hh.ru/vacancies", params=params).json()
        return data["items"]

    def get_vacancy(self):
        """
        перебирает вакансии из метода get_requests и приводит их к нужному формату
        :return: список словарей с обработанными вакансиями
        """
        data = self.get_requests()
        vacancies = [{
            "title": vacancy.get("name"),
            "url": vacancy.get("alternate_url"),
            "salary_from": vacancy.get("salary", {}).get("from"),
            "salary_to": vacancy.get("salary", {}).get("to"),
            "currency": vacancy.get("salary", {}).get("currency"),
            "area": vacancy.get("area", {}).get("name")
        } for vacancy in data]
        return vacancies


class SuperJobAPI(Header):
    """
    Класс для работы с superjob.ru
    :keyword: ключевое слово для поиска вакансий
    :api_key: API ключ для работы с superjob.ru
    """

    def __init__(self, keyword, api_key):
        self.keyword = keyword
        self.api_key = api_key
        self.all_vacancies = []

    def get_requests(self):
        """
        парсит вакансии по ключевому слову, переданному при инициализации класса
        :return: список вакансий с сайта superjob.ru
        """
        params = {
            "page": 0,
            "count": 100,
            "keyword": self.keyword,
            "archive": False
        }
        headers = {
            "X-Api-App-Id": self.api_key
        }
        data = requests.get("https://api.superjob.ru/2.0/vacancies/", params=params, headers=headers).json()
        return data['objects']

    def get_vacancy(self):
        """
        перебирает вакансии из метода get_requests и приводит их к нужному формату
        :return: список словарей с обработанными вакансиями
        """
        data = self.get_requests()
        self.all_vacancies = [{
            "title": vacancy.get("profession"),
            "url": vacancy.get("link"),
            "salary_from": vacancy.get("payment_from"),
            "salary_to": vacancy.get("payment_to"),
            "currency": vacancy.get("currency"),
            "area": vacancy.get("town", {}).get("title")
        } for vacancy in data]
        return self.all_vacancies

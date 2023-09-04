class Vacancy:
    def __init__(self, vacancy_id, title, url, salary_from, salary_to, currency, area):
        """
        Класс для каждой вакансии
        :param vacancy_id: id вакансии на платформе
        :param title: название вакансии
        :param url: ссылка для просмотра вакансии
        :param salary_from: минимальная зарплата
        :param salary_to: максимальная зарплата
        :param currency: валюта
        :param area:местоположение
        """
        self.vacansy_id = vacancy_id
        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.area = area

    def __repr__(self):
        return f"Vacancy(id={self.vacansy_id}, title={self.title}, url={self.url}, salary_from={self.salary_from}," \
               f"salary_to={self.salary_to}, currency={self.currency}, area={self.area})"

    def __str__(self):
        return f"{self.title} в г. {self.area}\n" \
               f"Заработная плата от {self.salary_from} {self.currency}\n" \
               f"Перейти по ссылке: {self.url}\n"

    def __lt__(self, other):
        if self.salary_from is None:
            self_salary_from = 0
        else:
            self_salary_from = self.salary_from

        if other.salary_from is None:
            other_salary_from = 0
        else:
            other_salary_from = other.salary_from

        if self_salary_from != other_salary_from:
            return self_salary_from < other_salary_from
        else:
            if self.salary_to is None:
                self_salary_to = float('inf')
            else:
                self_salary_to = self.salary_to

            if other.salary_to is None:
                other_salary_to = float('inf')
            else:
                other_salary_to = other.salary_to

            return self_salary_to < other_salary_to

    def __eq__(self, other):
        return (self.salary_from, self.salary_to) == (other.salary_from, other.salary_to)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

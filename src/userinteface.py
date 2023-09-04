class UserIntarface:
    @staticmethod
    def platform_choice():
        while True:
            print("Данное приложение позволяет получить открытые вакансии.")
            print("Откуда получить данные о вакансиях?")
            print("1 - с площадки hh.ru")
            print("2 - с площадки superjob.ru")
            user_input = input("3 - с обеих площадок\n")
            if user_input in ["1", "2", "3"]:
                return user_input
            else:
                print("Ввод неверный. Укажите валидный номер.")

    @staticmethod
    def cyties_choice():
        user_keyword = input("Укажите название вакансии или ключевое слово для поиска\n")
        user_cities = input("Укажите города для поиска (через запятую)\n").lower()
        return user_keyword, user_cities.split(",")

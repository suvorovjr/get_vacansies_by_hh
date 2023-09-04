from src.storage_json import VacansyJson
from src.userinteface import UserIntarface
from src.city_id import receive_city_hh, receive_city_super_job
from src.settings_paths import AREAS_HH, AREAS_SUPERJOB, API_KEY_SUPERJOB, VACANSIES_JSON
from src.job_api import APIhhru, SuperJobAPI


def main():
    save_json = VacansyJson(VACANSIES_JSON)
    save_json.remove_vacansies()

    user_platform = UserIntarface.platform_choice()
    user_keyword, user_cities = UserIntarface.cyties_choice()

    if user_platform == "1":
        hh_city_id = receive_city_hh(AREAS_HH, user_cities)
        api_hh = APIhhru(user_keyword, hh_city_id)
        vacansies_hh = api_hh.get_vacancy()
        save_json.add_vacansies(vacansies_hh)
        parsed_vacansies_hh = save_json.get_vacansies()
        [print(vacansy) for vacansy in parsed_vacansies_hh]
    elif user_platform == "2":
        sj_city_id = receive_city_super_job(AREAS_SUPERJOB, user_cities)
        api_sj = SuperJobAPI(user_keyword, API_KEY_SUPERJOB, sj_city_id)
        vacansies_sj = api_sj.get_vacancy()
        save_json.add_vacansies(vacansies_sj)
        parsed_vacansies_sj = save_json.get_vacansies()
        [print(vacansy) for vacansy in parsed_vacansies_sj]
    elif user_platform == "3":
        hh_city_id = receive_city_hh(AREAS_HH, user_cities)
        sj_city_id = receive_city_super_job(AREAS_SUPERJOB, user_cities)

        api_hh = APIhhru(user_keyword, hh_city_id)
        api_sj = SuperJobAPI(user_keyword, API_KEY_SUPERJOB, sj_city_id)

        vacansies_hh = api_hh.get_vacancy()
        vacansies_sj = api_sj.get_vacancy()

        save_json.add_vacansies(vacansies_hh + vacansies_sj)

        parsed_all_vacansies = save_json.get_vacansies()
        [print(vacansy) for vacansy in parsed_all_vacansies]


if __name__ == "__main__":
    main()

import requests


class HeadHunterAPI:
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies?employer_id="

    def get_company_vacancy(self, company_id: int) -> dict:
        """
        Функция получения словаря с данными о компании
        """
        try:
            company_vacancy = requests.get(f"{self.url}{company_id}", {"per_page": 100}).json()
            return company_vacancy
        except Exception as error:
            raise Exception(f"Возникла ошибка {error}")

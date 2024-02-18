import requests


class HeadHunterAPI:
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies?employer_id="

    def get_company_vacancy(self, company_id: int) -> dict:
        try:
            company_vacancy = requests.get(f"{self.url}{company_id}", {"per_page": 100}).json()
            return company_vacancy
        except Exception as error:
            raise Exception(f"Возникла ошибка {error}")


if __name__ == '__main__':
    hh = HeadHunterAPI()
    print(hh.get_company_vacancy(3093544))

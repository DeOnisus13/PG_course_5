import psycopg2

from classes.db_manager import DBManager
from classes.hh_api import HeadHunterAPI
from config import config
from src.utils import (
    create_database,
    create_vacancy_table,
    get_companies_from_json,
    insert_vacancy_data,
    postgresql_format,
)


def main():
    hh = HeadHunterAPI()
    db_name = "course_5"
    params = config()
    conn = None
    create_database(db_name, params)
    print(f"База {db_name} успешно создана")
    params.update({"dbname": db_name})
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                create_vacancy_table(cur)
                print("Таблица vacancies успешно создана")

                for company in get_companies_from_json():
                    company_info = hh.get_company_vacancy(company["id"])
                    company_info_sql = postgresql_format(company_info)

                    insert_vacancy_data(cur, company_info_sql)
                    print(f"Данные о {company['name']} в vacancies добавлены")

                database_class = DBManager()
                print("Общее количество вакансий у компании")
                print(database_class.get_companies_and_vacancies_count(cur))
                print("-" * 80)
                print("Все доступные вакансии")
                print(database_class.all_vacancies(cur))
                print("-" * 80)
                print("Средняя зарплата по всем вакансиям")
                print(database_class.avg_salary(cur))
                print("-" * 80)
                print("Список вакансий с зарплатой выше средней")
                print(database_class.get_vacancies_with_higher_salary(cur))
                print("-" * 80)
                keyword = input("Введите ключевое слово для поиска по вакансиям:\n")
                print(database_class.get_vacancies_with_keyword(cur, keyword))

    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    main()

import psycopg2

from classes.hh_api import HeadHunterAPI
from config import config
from src.utils import create_database, create_vacancy_table, get_companies_from_json, postgresql_format, \
    insert_vacancy_data


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

    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    main()

from configparser import ConfigParser
from pathlib import Path

ROOT_PATH = Path(__file__).parent
COMPANIES_JSON = Path.joinpath(ROOT_PATH, "data", "companies.json")
DATABASE_INI = Path.joinpath(ROOT_PATH, "database.ini")


def config(filename=DATABASE_INI, section="postgresql") -> dict:
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception("Section {0} is not found in the {1} file.".format(section, filename))
    return db

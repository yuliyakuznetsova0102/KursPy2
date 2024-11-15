import json

import pytest

from src.vacancy_job import Vacancy

with open("tests/data_test.json", "r", encoding="utf-8") as file:
    data = json.load(file)


@pytest.fixture
def valid():
    """Фикстура для метода валидации класса HH()"""
    test_vac = Vacancy("Разработчик", "Москва", 20000, data)

    return test_vac


@pytest.fixture
def city():
    """Фикстура для метода фильтрации по городу класса HH()"""
    test_vac = Vacancy("Разработчик", "Москва", 20000, data)

    return test_vac.filter_city()


@pytest.fixture
def difference():
    """Фикстура для метода фильтрации по заработной плате класса HH()"""
    test_vac = Vacancy("Разработчик", "Москва", 120000, data)

    city_1 = test_vac.filter_city()
    dif = test_vac.__le__(120000, city_1)
    return dif
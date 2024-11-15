import json

from src.vacancy_job import Vacancy

with open("tests/data_test.json", "r", encoding="utf-8") as file:
    data = json.load(file)



def test_filter_city(city):
    """Тестирование метода фильтрации по городу в классе HH()"""
    test_vac = Vacancy('Разработчик', 'Москва', 20000, data)

    assert test_vac.filter_city() == city

def test_difference(difference):
    """Тестирование метода фильтрации по заработной плате в классе HH()"""
    test_vac = Vacancy('Разработчик', 'Москва', 120000, data)
    city_1 = test_vac.filter_city()
    dif = test_vac.__le__(12000,city_1)
    return dif == difference
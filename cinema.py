from functools import wraps
import xlsxwriter as excel
import requests


def save_to_xlsx(func):
    @wraps(func)
    def wrapped(self, *args, **kwargs):
        workbook = excel.Workbook('movies_list.xlsx')
        worksheet = workbook.add_worksheet()
        for num, item in enumerate(func(self)):
            worksheet.write(num, 0, item.name)
            worksheet.write(num, 1, item.countries)
        workbook.close()
        return func(self)
    return wrapped


class Movie():
    def __init__(self, name, countries):
        self.name = name
        self.countries = countries

    def __repr__(self):
        return self.name


class MovieCollector:
    def __init__(self):
        self.json = requests.get('http://kinoafisha.ua/ajax/skoro_load').json()

    @save_to_xlsx
    def get_actual_movie_list(self):
        movie_list = []
        for movie in self.json['result']:
            list_element = Movie(movie['name'], movie['countries'])
            movie_list.append(list_element)
        return movie_list
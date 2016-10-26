import requests
from bs4 import BeautifulSoup


def sinoptik_temperature_current_kiev():
    html = requests.get('https://ua.sinoptik.ua/погода-київ').text
    parsed_html_document = BeautifulSoup(html, 'lxml')      # markup=html
    current_temp = parsed_html_document.find('p', class_='today-temp').text
    return current_temp


def sinoptik_max_temperature_current_day_kiev():
    html = requests.get('https://ua.sinoptik.ua/погода-київ').text
    parsed_html_document = BeautifulSoup(html, 'lxml')
    max_temp = parsed_html_document.find('div', class_='max').text
    return max_temp

print(sinoptik_temperature_current_kiev())
print(sinoptik_max_temperature_current_day_kiev())
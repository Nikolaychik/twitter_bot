import requests
from bs4 import BeautifulSoup


def sinoptik_temperature_current_kiev():
    html = requests.get('https://ua.sinoptik.ua/погода-київ').text
    parsed_html_document = BeautifulSoup(html, "lxml")
    current_temp = parsed_html_document.find('p', class_='today-temp').text
    return current_temp


def get_info_day_light_down_time():
    html = requests.get('https://ua.sinoptik.ua/погода-київ').text
    parsed_html_document = BeautifulSoup(html, "lxml")
    day_light_down_time = str(parsed_html_document.find('div', class_='infoDaylight').text).strip().split('Захід ')[1]
    return day_light_down_time


if __name__ == '__main__':
    print(sinoptik_temperature_current_kiev())
    print(get_info_day_light_down_time())

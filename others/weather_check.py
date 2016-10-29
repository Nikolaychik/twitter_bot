import requests
from bs4 import BeautifulSoup


def sinoptik_temperature_current_kiev():
    html = requests.get('https://ua.sinoptik.ua/погода-київ').text
    parsed_html_document = BeautifulSoup(html, "lxml")
    current_temp = parsed_html_document.find('p', class_='today-temp').text
    return current_temp


def sinoptik_info_day_light_down_time():
    html = requests.get('https://ua.sinoptik.ua/погода-київ').text
    parsed_html_document = BeautifulSoup(html, "lxml")
    day_light_down_time = str(parsed_html_document.find('div', class_='infoDaylight').text).strip().split('Захід ')[1]
    return day_light_down_time


def sinoptik_temperature_current_kiev_historyval():
    html = requests.get('https://ua.sinoptik.ua/погода-київ').text
    parsed_html_document = BeautifulSoup(markup = html)
    current_temp = parsed_html_document.find('p', class_='infoHistoryval').text.split(':')[2][:5]
    return  current_temp


def sinoptik_temperature_max_kiev():
    html = requests.get('https://ua.sinoptik.ua/погода-київ').text
    parsed_html_document = BeautifulSoup(markup=html)
    current_temp = parsed_html_document.find('p', class_='infoHistoryval').text
    return current_temp.split(" ")[2]


def sinoptik_max_temperature_current_day_kiev():
    html = requests.get('https://ua.sinoptik.ua/погода-київ').text
    parsed_html_document = BeautifulSoup(html, 'lxml')
    max_temp = parsed_html_document.find('div', class_='max').text
    return max_temp

def sinoptik_east_kiev():
    html = requests.get('https://ua.sinoptik.ua/погода-київ').text
    parsed_html_document = BeautifulSoup(markup=html)
    current_east = parsed_html_document.find(class_='infoDaylight').text
    return current_east


def sinoptik_today_min():
    html = requests.get('https://ua.sinoptik.ua/погода-київ').text
    parsed_html_document = BeautifulSoup(markup=html)
    today_min = parsed_html_document.find('div', class_='min').text

    return today_min


if __name__ == '__main__':
    sinoptik_temperature_current_kiev()
    sinoptik_info_day_light_down_time()
    sinoptik_today_min()
    sinoptik_temperature_max_kiev()
    sinoptik_temperature_current_kiev_historyval()


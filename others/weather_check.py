import requests
from bs4 import BeautifulSoup


class WeatherCollector:
    def __init__(self):
        html = requests.get('https://ua.sinoptik.ua/погода-київ').text
        self.parsed_html_document = BeautifulSoup(html, 'lxml')

    def sinoptik_current_weather(self):
        current_temp = self.parsed_html_document.find('p', class_='today-temp').text
        today_min = self.parsed_html_document.find('div', class_='min').text[-3:]
        max_temp = self.parsed_html_document.find('div', class_='max').text[-3:]
        day_light_down_time = str(self.parsed_html_document.find('div', class_='infoDaylight').text)\
                              .strip().split('Захід ')[1]
        return {
            'current_temp': current_temp,
            'today_min': today_min,
            'max_temp': max_temp,
            'day_light_down_time': day_light_down_time
        }

    def sinoptik_kiev_historyval(self):
        overall_min = self.parsed_html_document.find('p', class_='infoHistoryval').text.split(':')[2][1:7]
        overall_max = self.parsed_html_document.find('p', class_='infoHistoryval').text.split(':')[1][1:6]
        return {
            'overall_min': overall_min,
            'overall_max': overall_max
        }

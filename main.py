from twitter.api import TwitterBot
import configparser


config = configparser.ConfigParser()
config.read('example.ini')
credentials = {}
for section in config.sections():
    for key, value in config[section].items():
        credentials[key] = value

print(credentials)

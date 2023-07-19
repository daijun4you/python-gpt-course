import configparser
import os

cache = {}


def get(key: str, file: str = 'openai.ini', section: str = "default") -> str:
    if file not in cache:
        cache[file] = configparser.ConfigParser()
        cache[file].read(os.path.dirname(__file__) + "/" + file)

    return cache[file].get(section, key)

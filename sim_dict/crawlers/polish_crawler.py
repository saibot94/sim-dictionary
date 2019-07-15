import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from sim_dict.crawlers import Crawler
import logging

API_ROOT ="https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=pl&dt=t&{}"


class PolishCrawler(Crawler):
    
    def get_word(self, word: str):
        """
        Gets a word's translation from the Google translate API
        """
        url = API_ROOT.format(urlencode({"q": word}))
        print(url)
        response = requests.get(url)
        if not response.ok:
            logging.error("Could not get word {} from Google API".format(word))
            return []
        data = response.json()
        translated = data[0][0][0]
        return [translated.lower()]

crawler = PolishCrawler()
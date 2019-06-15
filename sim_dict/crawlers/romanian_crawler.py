import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from sim_dict.crawlers import Crawler
import logging

API_ROOT = "http://dictionare.com/enro40.php?field0={}"


class RomanianCrawler(Crawler):
    def extract_toplevel_text(self, element):
        words = "".join([t for t in element.contents if type(t) == NavigableString])
        return list(map(lambda s: s.strip(), words.split(";")))[0]

    def get_word(self, word: str):
        """
        Gets a word's definition from dictionare.com
        """
        url = API_ROOT.format(word)
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        centers = soup.find_all("center")
        if len(centers) != 7:
            logging.error("Not found!")
            return []
        all_list_items = centers[-3].td.find_all("li")
        all_items = map(lambda li: li.small, all_list_items)
        return list(map(lambda item: self.extract_toplevel_text(item), all_items))


crawler = RomanianCrawler()

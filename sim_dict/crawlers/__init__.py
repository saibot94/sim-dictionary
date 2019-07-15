from abc import ABCMeta, abstractmethod


class Crawler:
    """
    Abstract base class for all crawlers to implement
    """

    @abstractmethod
    def get_word(self, word: str):
        """
        Gets a word from some external dictionary, by crawling or web API or anything
        """
        return NotImplemented


from sim_dict.crawlers.romanian_crawler import crawler as romanian_crawler
from sim_dict.crawlers.polish_crawler import crawler as polish_crawler

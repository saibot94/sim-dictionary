from sim_dict.crawlers.polish_crawler import PolishCrawler

def test_potato_polish():
    crawler = PolishCrawler()
    potato = crawler.get_word("potato")
    assert potato == ["ziemniak"]
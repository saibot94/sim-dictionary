from sim_dict.crawlers.romanian_crawler import RomanianCrawler

def test_potato_romanian():
    crawler = RomanianCrawler()
    potato = crawler.get_word("potato")
    assert potato == ["cartof"]
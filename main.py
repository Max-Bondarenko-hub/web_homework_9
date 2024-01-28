import scrapy
from scrapy.crawler import CrawlerProcess
from my_scrapy.my_scrapy.spiders.authors import AuthorsSpider
from my_scrapy.my_scrapy.spiders.quotes import QuotesSpider

process = CrawlerProcess()
process.crawl(QuotesSpider)
process.crawl(AuthorsSpider)
process.start()
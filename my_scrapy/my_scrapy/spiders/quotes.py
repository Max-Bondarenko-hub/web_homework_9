import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]
    custom_settings = {"FEEDS": {r"json_files\quotes.json": {"format": "json", "encoding": "utf8", "indent": 4}}}

    def composed_info(self, next_quote):
        return {
            "tags": next_quote.xpath("div[@class='tags']/a/text()").getall(),
            "author": next_quote.xpath("span/small[@class='author']/text()").get(),
            "quote": next_quote.xpath("span[@class='text']/text()").get(),
        }

    def parse(self, response):
        quotes = response.xpath("/html//div[@class='quote']")
        for quote in quotes:
            yield self.composed_info(quote)

        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page is not None:
            yield scrapy.Request(url=self.start_urls[0] + next_page)

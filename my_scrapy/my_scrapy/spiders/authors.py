import scrapy


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]
    custom_settings = {"FEEDS": {r"json_files\authors.json": {"format": "json", "encoding": "utf8", "indent": 4}}}

    def parse(self, response):
        get_links = response.xpath("/html//div[@class='quote']/span/a/@href").extract()

        for link in get_links:
            yield scrapy.Request(url=self.start_urls[0] + link, callback=self.about_page)

        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page is not None:
            yield scrapy.Request(url=self.start_urls[0] + next_page)

    def about_page(self, response):
        yield {
            "fullname": response.xpath("/html//h3[@class='author-title']/text()").get(),
            "born_date": response.xpath("/html//span[@class='author-born-date']/text()").get(),
            "born_location": response.xpath("/html//span[@class='author-born-location']/text()").get(),
            "description": response.xpath("/html//div[@class='author-description']/text()").get(),
        }

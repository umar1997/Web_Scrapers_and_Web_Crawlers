from scrapy.spiders import CrawlSpider, rule
from scrapy.linkextractors import LinkExtractor

class BooksSpider(CrawlSpider):
    name = 'books_'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    rules = (Rule(LinkExtractor(), callback='parse_page', follow=True))
    # If follow = False then wont go to the next page

    def parse_page(self, response):
        yield {'URL': response.url}

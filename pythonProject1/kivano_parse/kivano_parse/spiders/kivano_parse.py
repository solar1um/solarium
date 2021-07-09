import scrapy
from ..items import KivanoParseItem

class KivanoSpider(scrapy.Spider):
    name = 'kivano'

    start_urls = [
            'https://www.kivano.kg/noutbuki-i-kompyutery?page=1',
            'https://www.kivano.kg/noutbuki-i-kompyutery?page=2'
            ]
    def parse(self, response):
        all_links = response.css('body.item product_listbox oh')
        urls = ['http://www.kivano.kg' + link for link in all_links]

        for url in urls:
            yield response.follow(url, callback = self.parse)

        items = KivanoParseItem()



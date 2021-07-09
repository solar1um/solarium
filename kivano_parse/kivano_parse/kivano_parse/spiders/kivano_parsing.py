import scrapy

class PostSpider(scrapy.Spider):
    name = 'kivanoparse'

    start_urls = [
        'https://www.kivano.kg/noutbuki-i-kompyutery?page=1',
        'https://www.kivano.kg/noutbuki-i-kompyutery?page=2'
    ]

    def parse(self, response):
        all_links = response.css('a.item product_listbox oh')
        print(all_links)
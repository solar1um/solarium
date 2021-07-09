# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NambafoodItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cafe_name = scrapy.Field()
    came_image = scrapy.Field
    afv_price = scrapy.Field
    restaurant_categories = scrapy.Field
    dishes = scrapy.Field

    pass

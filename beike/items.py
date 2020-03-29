# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BeikeItem(scrapy.Item):
    name = scrapy.Field()
    property = scrapy.Field()
    sales_status = scrapy.Field()
    position = scrapy.Field()
    house_type = scrapy.Field()
    area = scrapy.Field()
    average_price = scrapy.Field()
    total_price = scrapy.Field()

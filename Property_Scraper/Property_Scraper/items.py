# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PropertyScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # Urls = scrapy.Field()
    Title = scrapy.Field()
    Price = scrapy.Field()
    Phone_no = scrapy.Field()
    Address = scrapy.Field()
    # IMG_url = scrapy.Field()
    Agency = scrapy.Field()
    Description = scrapy.Field()

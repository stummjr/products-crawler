# -*- coding: utf-8 -*-
import scrapy


class ProductItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    category = scrapy.Field()

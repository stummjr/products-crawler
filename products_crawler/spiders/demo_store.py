# -*- coding: utf-8 -*-
import scrapy
from w3lib.html import remove_tags
from products_crawler.items import ProductItem


class DemostoreSpider(scrapy.Spider):
    name = "demostore"
    allowed_domains = ["demo.mv.cs-cart.com"]
    start_urls = [
        'http://demo.mv.cs-cart.com/',
    ]
    download_delay = 0.5

    def parse(self, response):
        for category_url in response.css('.ty-menu__submenu-link ::attr(href)').extract():
            yield scrapy.Request(category_url, callback=self.parse_category, meta={'page_number': '1'})

    def parse_category(self, response):
        for product_url in response.css('div.ty-grid-list__item-name > a.product-title ::attr(href)').extract():
            yield scrapy.Request(product_url, callback=self.parse_product)

    def parse_product(self, response):
        item = ProductItem()
        item['url'] = response.url
        item['title'] = response.css('.ty-product-block-title ::text').extract_first()
        item['description'] = remove_tags(response.css('#content_description *').extract_first() or '')
        yield item

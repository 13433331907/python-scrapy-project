# -*- coding: utf-8 -*-
import scrapy


class SunningBookSpider(scrapy.Spider):
    name = 'sunning_book'
    allowed_domains = ['sunning.com']
    start_urls = ['http://sunning.com/']

    def parse(self, response):
        pass

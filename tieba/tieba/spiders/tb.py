# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
import requests


class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/mo/q---1E1A44492752A8CFE48A31DB2C0BB8FE:FG=1--1-3-0--2--wapp_1536855175546_700/m?kw=李毅&lp=6012&pn=0&pinf=1']

    def parse(self, response):
        div_list = response.xpath("//div[contains(@class, 'i')]")
        for div in div_list:
            item = {}
            item["href"] = response.xpath("./a/@href").extract_first()
            item["title"] = response.xpath("./a/text()").extract_first()
            # item["img_list"] = []
            # if item["href"] is not None:
            #     item["href"] = urljoin(response.url, item["href"])
            #     yield scrapy.Request(
            #         item["href"],
            #         callback=self.parse_detail,
            #         meta={"item": "item"}
            #     )
            print(item)
            yield item
            # next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
            # if next_url is not None:
            #     yield scrapy.Request(
            #         next_url,
            #         callback=self.parse,
            #     )

    # def parse_detail(self, response):
    #     item = response.meta["item"]
    #     item["img_list"].extend(response.xpath("//div[@class=i]/a[text()='图']/@href").extract())
    #     next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
    #     if next_url is not None:
    #         next_url = urljoin(response.url, next_url)
    #         yield scrapy.Request(
    #             next_url,
    #             callback=self.parse_detail,
    #             meta={"item": "item"}
    #         )
    #     else:
    #         # item["img_list"] = [requests.utils.unquote(i).split("src=")[-1] for i in item["image_list"]]
    #         print(item)

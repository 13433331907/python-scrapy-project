# -*- coding: utf-8 -*-
import scrapy
from yangguang.items import YangguangItem


class YaSpider(scrapy.Spider):
    name = 'ya'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/html/top/town.shtml']

    def parse(self, response):
        tr_list = response.xpath("//div[@class='pagecenter']/table[2]/tr/td/table/tr")
        for tr in tr_list:
            item = YangguangItem()
            item["title"] = tr.xpath("./td[2]/a[@class='news14]/@title").extract_first()
            item["href"] = tr.xpath("./td[2]/a[@class='news14]/@href").extract_first()
            item["publish_date"] = tr.xpath("./td[last()]/text()").extract_first()

            yield scrapy.Request{
                item["href"]
                callback = self.parse_detail(meta)
                meta = {"item": item}
            }

    def parse_detail(self, response): # 处理详情页
        item = response.meta["item"]
        item[content] = response.xpath
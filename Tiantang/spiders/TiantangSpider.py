# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TiantangItem
from scrapy.pipelines.images import ImagesPipeline


class TiantangspiderSpider(CrawlSpider):
    name = 'Tiantang'
    allowed_domains = ['photo.67.com']
    start_urls = ['http://photo.67.com/']

    rules = (
        Rule(LinkExtractor(allow=r'http://photo.67.com/gqxz/\d+/\d+/\d+/\d+\w\d+.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'http://photo.67.com/gqxz/\d+/\d+/\d+/\d+.html'), follow=True),
        Rule(LinkExtractor(allow=r'http://photo.67.com/index_\d+.html'),  follow=True),
    )

    def parse_item(self, response):
        item = TiantangItem()
        item['image_urls'] = response.xpath('.//div[@class="imgCon"]//div[@id="imgContent"]/img/@src').extract()
        #print(response.url,'***************')
        yield item
        #i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #return i

# -*- coding: utf-8 -*-
import scrapy
import sys

sys.path.append("../")

from ..items import BeikeItem


class BeikeSpider(scrapy.Spider):
    name = 'beike'
    allowed_domains = ['xa.fang.ke.com']
    start_urls = ['https://xa.fang.ke.com/loupan/pg' + str(x) for x in range(1, 101, 1)]

    # start_urls = ['https://xa.fang.ke.com/loupan/pg1']

    def parse(self, response):
        # ul = response.css('.resblock-desc-wrapper')
        # self.logger.debug(ul)
        # for li in ul:
        #     item = BeikeItem()
        #     item['name'] = li.css('.resblock-desc-wrapper .resblock-name a::text').extract_first()  # 楼盘名称
        #     item['property'] = li.css('.resblock-name span:last-of-type::text').extract_first()  # 物业类型（住宅、商业）
        #     item['sales_status'] = li.css('.resblock-name span:first-of-type::text').extract_first()  # 销售状态（在售、未开盘）
        #
        #     item['position'] = li.css('.resblock-location::text')[1].extract()  # 位置
        #     self.logger.debug(li.css('.resblock-location').extract_first())
        #     yield item

        line = response.xpath('/html/body/div[6]/ul[2]/li')

        for li in line:
            # self.logger.debug(li.xpath('./div/a[1]/text()'))
            item = BeikeItem()
            item['name'] = li.xpath('./div/div[1]/a/text()').extract_first()
            item['sales_status'] = li.xpath('./div/div[1]/span[1]/text()').extract_first()
            item['property'] = li.xpath('./div/div[1]/span[2]/text()').extract_first()
            item['position'] = li.xpath('./div/a[1]/text()').extract()[1]
            item['house_type'] = li.xpath('./div/a[2]/span[2]/text()').extract_first() + '/' + li.xpath(
                './div/a[2]/span[3]/text()').extract_first()
            # item['area'] = li.xpath('./div/a[2]/span[4]/text()').extract_first()
            item['average_price'] = li.xpath('./div/div[4]/div/span/text()').extract_first()
            item['total_price'] = li.xpath('./div/div[4]/div[2]/text()').extract_first()
            yield item

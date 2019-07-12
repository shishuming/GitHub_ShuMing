# -*- coding: utf-8 -*-
import scrapy
from douBanBook.items import *

class DoubanspiderSpider(scrapy.Spider):
    name = 'DouBanSpider'
    allowed_domains = ['book.douban.com']
    start_urls = ['http://book.douban.com/']

    def parse(self, response):
        # 使用xpath将最受关注图书榜的内容解析出来并存储到item中（8分）
        book = response.xpath('//*[@id="content"]/div/div[1]/div[4]/div[2]/ul/li')
        # print(book,'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        for div in book:
            # 获取标题
            title = div.xpath('.//h4[@class="title"]/a/text()').extract()[0]
            print(title,'>>>')
            # 获取连接
            url = div.xpath('.//h4[@class="title"]/a/@href').extract()[0]
            print(url, '>>>')
            # 获取作者
            author = div.xpath('.//p[@class="author"]/text()').extract()[0]
            print(author, '>>>')

            item = DoubanbookItem()
            item['title'] = title
            item['url'] = url
            item['author'] = author

            yield item
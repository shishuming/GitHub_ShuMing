# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanbookItem(scrapy.Item):
    # define the fields for your item here like:
    # (5)定义图书item，包括（图书标题、图书链接、图书作者）（8分）
    title = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanbookPipeline(object):

    def process_item(self, item, spider):
        with open('Doubanbook.txt','a',encoding='utf-8') as a:
            a.write('标题:'+item['title']+'\t'+item['author']+'\n链接:'+item['url']+'\n')
        return item

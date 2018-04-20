# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from sched import scheduler

import scrapy
from twisted.names.test.test_rfc1982 import serialNumber2


class TestscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field();
    novelurl = scrapy.Field();
    author = scrapy.Field();
    serialstatus = scrapy.Field();
    serialNumber = scrapy.Field();
    category = scrapy.Field();
    name_id = scrapy.Field();



class DcontentItem(scrapy.Item):

    id_name = scrapy.Field()
    #小说编号
    chaptercontent = scrapy.Field()
    # 章节内容
    num = scrapy.Field()
    # 用于绑定章节顺序
    chapterurl = scrapy.Field()
    # 章节地址
    chaptername = scrapy.Field()
    # 章节名字
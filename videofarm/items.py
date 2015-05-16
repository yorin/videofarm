# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VideofarmItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    youtubetitle = scrapy.Field()
    urlstream = scrapy.Field()
    mainurl = scrapy.Field()
    source = scrapy.Field()
    id = scrapy.Field()
    mm = scrapy.Field()
    itag = scrapy.Field()
    nh = scrapy.Field()
    ratebypass = scrapy.Field()
    initcwndbps = scrapy.Field()
    ip = scrapy.Field()
    key = scrapy.Field()
    expire = scrapy.Field()
    sver = scrapy.Field()
    fexp = scrapy.Field()
    ms = scrapy.Field()
    mv = scrapy.Field()
    mt = scrapy.Field()
    dur = scrapy.Field()
    sparams = scrapy.Field()
    requiressl = scrapy.Field()
    upn = scrapy.Field()
    mime = scrapy.Field()
    signature = scrapy.Field()

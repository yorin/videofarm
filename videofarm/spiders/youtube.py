# -*- coding: utf-8 -*-
import scrapy
from videofarm.items import VideofarmItem
from scrapy.spider import BaseSpider
import urllib

#from scrapy.selector import HtmlXPathSelector
#from scrapy.selector import Selector
import re
import urllib 
"""
 http://users.ohiohills.com/fmacall/ytcrack.txt
 
"""
class YoutubeSpider(scrapy.Spider):
    name = "youtube"
    allowed_domains = ["youtube.com"]
    def __init__(self, query=None, *args, **kwargs):
#    start_urls = (
#        'https://www.youtube.com/watch?v=kP15m8PbGGE',
#        'https://www.youtube.com/watch?v=rs39FWDhzDs',
#    )
      self.start_urls = ['https://www.youtube.com/watch?v=%s' % query]

    def parse(self, response):
        itemstreams = []
        link = response.xpath('//script/text()').re(r'0026url=(.*?)\\u')
        for stream in link:
            itemstream = VideofarmItem()
            if ('mime%3Dvideo%252Fmp4') in stream:
                stream = stream
                if ('itag%3D18') in stream:
                    stream = urllib.unquote(stream).decode('utf8')
                    itemstream['urlstream'] = stream
                    itemstreams.append(itemstream)
        return itemstreams

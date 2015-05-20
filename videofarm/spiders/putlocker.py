# -*- coding: utf-8 -*-
import scrapy
from videofarm.items import VideofarmItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
#from scrapy.selector import HtmlXPathSelector

#http://mherman.org/blog/2012/11/08/recursively-scraping-web-pages-with-scrapy/#.VVyEv_mqqko
#http://doc.scrapy.org/en/0.7/topics/selectors.html

class PutlockerSpider(scrapy.Spider):
    name = "putlocker"
    allowed_domains = ["putlocker.is"]
    def __init__(self, query=None, *args, **kwargs):
       self.start_urls = ['http://www.putlocker.is/%s' % query]
       self.rules = (Rule(SgmlLinkExtractor()),)

    def parse(self, response):
        itemstreams = []
        itemstream = VideofarmItem()
        #filebody = response.xpath('//td[@class="entry"]/a/@href')
        filebody = response.xpath('//td[@class="entry"]/a[contains(@href, "promptfile")]/@href')
        #itemstream['urlstream'] = filebody.xpath("a/@href").extract()[0].strip()
        itemstream['urlstream'] = filebody.extract()
        itemstreams.append(itemstream)
        return itemstreams

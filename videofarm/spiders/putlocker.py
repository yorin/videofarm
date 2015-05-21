# -*- coding: utf-8 -*-
import scrapy
from videofarm.items import VideofarmItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
#from scrapy.selector import HtmlXPathSelector

#http://mherman.org/blog/2012/11/08/recursively-scraping-web-pages-with-scrapy/#.VVyEv_mqqko
#http://doc.scrapy.org/en/0.7/topics/selectors.html
itemstreams = []

class PutlockerSpider(scrapy.Spider):
    name = "putlocker"
    allowed_domains = ["putlocker.is", "promptfile.com"]

    def __init__(self, query=None, *args, **kwargs):
       self.start_urls = ['http://www.putlocker.is/%s' % query]
       self.rules = (Rule(SgmlLinkExtractor()),)

    def parse(self, response):
        itemstream = VideofarmItem()
        #filebody = response.xpath('//td[@class="entry"]/a/@href')
        urlone = response.xpath('//td[@class="entry"]/a[contains(@href, "promptfile")]/@href').extract()[0]
        #print filebody
        #itemstream['urlstream'] = urlone.xpath("a/@href").extract()[0].strip()
        itemstream['urlstream'] = urlone
        itemstreams.append(itemstream)
        yield itemstreams
        yield scrapy.Request(url=urlone, callback=self.secondparse)
        #for url in itemstreams:
        #    yield url
    def secondparse(self, response):
        itemstream = VideofarmItem()
        urltwo = response.xpath('//div[@id="confirmbox"]/form')
        #itemstream['urlstream'] = urltwo.extract()
        #itemstreams.append(itemstream)
        #return itemstreams
        itemstream['cfname'] = urltwo.xpath('//input/@name').extract()
        itemstream['cfvalue'] = urltwo.xpath('//input/@value').extract()
        itemstreams.append(itemstream)
        return itemstreams


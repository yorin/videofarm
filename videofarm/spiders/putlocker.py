# -*- coding: utf-8 -*-
import scrapy
from videofarm.items import VideofarmItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
#from scrapy.selector import HtmlXPathSelector

#http://mherman.org/blog/2012/11/08/recursively-scraping-web-pages-with-scrapy/#.VVyEv_mqqko
#http://doc.scrapy.org/en/0.7/topics/selectors.html

class PutlockerSpider(scrapy.Spider):
    cfurl = 0
    name = "putlocker"
    allowed_domains = ["putlocker.is", "promptfile.com"]

    def __init__(self, query=None, *args, **kwargs):
       self.start_urls = ['http://www.putlocker.is/%s' % query]
       self.rules = (Rule(SgmlLinkExtractor()),)

    def parse(self, response):
        #itemstream = VideofarmItem()
        #filebody = response.xpath('//td[@class="entry"]/a/@href')
        urlone = response.xpath('//td[@class="entry"]/a[contains(@href, "promptfile")]/@href').extract()[0].strip()
        global cfurl
        cfurl = urlone
        #print filebody
        #itemstream['urlstream'] = urlone.xpath("a/@href").extract()[0].strip()
        #itemstream['urlstream'] = urlone
        #itemstreams.append(itemstream)
        #yield itemstreams
        yield scrapy.Request(url=urlone, callback=self.secondparse)
        #for url in itemstreams:
        #    yield url
    def secondparse(self, response):
        itemstreams = []
        itemstream = VideofarmItem()
        urltwo = response.xpath('//div[@id="confirmbox"]/form')
        #itemstream['urlstream'] = urltwo.extract()
        #itemstreams.append(itemstream)
        #return itemstreams
        #itemstream['urlstream'] = cfurl
        itemstream['urlstream'] = cfurl
        #itemstream['cfname'] = urltwo.xpath('//input/@name').extract()
        cfname = urltwo.xpath('//input/@name').extract()[0]
        #itemstream['cfvalue'] = urltwo.xpath('//input/@value').extract()
        cfvalue = urltwo.xpath('//input/@value').extract()[0]
        #itemstreams.append(itemstream)
        #return itemstreams
        yield scrapy.FormRequest(url=cfurl,formdata={cfname: cfvalue},callback=self.after_post)

    def after_post(self, response):
        itemstreams = []
        itemstream = VideofarmItem()
        itemstream['streamtitle'] = response.xpath('//div[@id="view_header"]/span/text()').extract()[0]
        itemstream['urlstream'] = response.xpath('//a[@class="view_dl_link"]/@href').extract()[0]
        itemstreams.append(itemstream) 
        return itemstreams

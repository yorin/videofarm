# -*- coding: utf-8 -*-

# Scrapy settings for videofarm project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'videofarm'

SPIDER_MODULES = ['videofarm.spiders']
NEWSPIDER_MODULE = 'videofarm.spiders'
#ITEM_PIPELINES = {'scrapy.pipelines.media': 1}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'videofarm (+http://www.yourdomain.com)'

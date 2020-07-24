#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 18:24:43 2020

@author: sonalgupta
"""



from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from datetime import datetime

class MySpider(scrapy.Spider):
    name = "spider_values"
    
    def start_requests(self):
        company = ['refineries/relianceindustries/RI','mediaentertainment/zeeentertainmententerprises/ZEE']
       # urls =['https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI',
              # 'https://www.moneycontrol.com/india/stockpricequote/mediaentertainment/zeeentertainmententerprises/ZEE']
        for url in company:
            
            yield scrapy.Request(url = 'https://www.moneycontrol.com/india/stockpricequote/'+url, callback = self.parse)
            
    def parse(self,response):
        keys = response.css('div.value_txtfl::text').extract() #list
        values = response.css('div.value_txtfr::text').extract() #list
        
        dateTimeObj = datetime.now()
        req_values['company'] = response
        
        req_values['Timestamp'] = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
        
        for i in range(0,11):
            req_values[ keys[i] ] = values[i]
        
        print(req_values)
        
        
req_values = dict()
configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner()

d = runner.crawl(MySpider)
d.addBoth(lambda _: reactor.stop())
reactor.run() # the script will block here until the crawling is finished



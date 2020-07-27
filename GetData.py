#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:39:07 2020

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
        company = ['http://hisarbazar.com/search.php?CATID=118&rpp=200']
      
        for url in company:
            
            yield scrapy.Request(url, callback = self.parse)
            
    def parse(self,response):
        values = response.css("div:nth-child(3)>div>table td>::text").extract()
        b = len(values)
        print(b)

    
        c = 4
        
        while (c  <= 340) :
            
            keys = response.css("div:nth-child(3)>div:nth-child("+str(c)+")>table td>strong::text").extract()
            values = response.css("div:nth-child(3)>div:nth-child("+str(c)+")>table td::text").extract()
            c+=2
            s = " "
            s = s.join(values)
            
            k = "NA"
            k = k.join(keys)
            
            req_values[k] = s
            #print(keys[0])
            #print(s)
        print(req_values)
        
        
        #req_values['Timestamp'] = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
        
        
        #print(req_values)
        
        
req_values = dict()
configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner()

d = runner.crawl(MySpider)
d.addBoth(lambda _: reactor.stop())
reactor.run() # the script will block here until the crawling is finished
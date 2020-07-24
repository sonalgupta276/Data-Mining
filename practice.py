#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:04:52 2020

@author: sonalgupta
"""
# import scrapy
# from scrapy.crawler import CrawlerProcess
# from multiprocessing import Process, Queue
# from twisted.internet import reactor

# class SpiderClassFetch(scrapy.Spider):
#     name = "spider_values"
    
#     def start_requests(self):
#         urls =['https://www.datacamp.com/courses/all']
#        # urls = ['http://quotes.toscrape.com/tag/humor/']
#         for url in urls:
#             yield scrapy.Request(url = url, callback=self.parse)
            
#     def parse(self,response):
#         #for quote in response.css('div.quote'):
#          #   print(quote.css('span.text::text').extract_first())
#         links = response.css('div.dc-global-search-result__content>h4::text').extract()
#         filepath = 'DC_linkss.txt'
        
#         # for link in links:
#         #     print(link)
#         #     courses.append(link)
#         # print(courses)
#         # html_file = "DC_courses.html"
#         with open(filepath,'w') as f:
#             f.writelines([link + '/n' for link in links])
        
# print("Sonal")

    
# process = CrawlerProcess()
# process.crawl(SpiderClassFetch)
# process.start()






# import scrapy
# import scrapy.crawler as crawler
# from multiprocessing import Process, Queue
# from twisted.internet import reactor

# # your spider
# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = ['http://quotes.toscrape.com/tag/humor/']

#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             print(quote.css('span.text::text').extract_first())


# # the wrapper to make it run more times
# def run_spider(spider):
#     def f(q):
#         try:
#             runner = crawler.CrawlerRunner()
#             deferred = runner.crawl(spider)
#             deferred.addBoth(lambda _: reactor.stop())
#             reactor.run()
#             q.put(None)
#         except Exception as e:
#             q.put(e)

#     q = Queue()
#     p = Process(target=f, args=(q,))
#     p.start()
#     result = q.get()
#     p.join()

#     if result is not None:
#         raise result

# print('first run:')
# run_spider(QuotesSpider)

# -*- coding: utf-8 -*-
import scrapy
import json
import re
#from site import Site
#from scrapy.exporters import JsonItemExporter

class Site(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    keyword = scrapy.Field()
    num_of_xpaths = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()

class NewsSpider(scrapy.Spider):
    name = "news"
    site = []
    
        
    def start_requests(self):
        with open('setting.json') as f:
            dict = json.load(f)

        if not len(dict):
            print("File input error, check json setting.")
        else:
            start_urls = []
            count = 0
            for key in sorted(dict.keys()):
                s = dict[key]
                self.site = Site( 
                    {
                        'name': s['name'],
                        'url': s['url'],
                        'keyword': s['keyword'],
                        'num_of_xpaths': s['num_of_xpaths'],
                        'title': s['title'],
                        'description': s['description'],
                        'link': s['link']
                    })
                start_urls.append(s['url'])
                count += 1
                
            for url in start_urls:
                yield scrapy.Request(url=url, callback=self.parse)
         

    def parse(self, response):
        titles = response.xpath('' + self.site['title']).extract()
        for i in range(len(titles)):
            if re.search(r''+ self.site['keyword'], titles[i]):
                yield {
                    'title': response.xpath('' + self.site['title'])[i].extract(),
                    'description': response.xpath('' + self.site['description'])[i].extract(),
                    'link': response.xpath('' + self.site['link'])[i].extract()
                }
        
        #with open('news.json', 'wb') as fin:
        #    self.exporter = JsonItemExporter(fin, encoding='utf-8', ensure_ascii=False)
        #    self.exporter.start_exporting()
        #    fin.write(response.xpath('' + self.site['title']).extract_first().encode('utf-8'))
        #    fin.write(response.xpath('' + self.site['description']).extract_first().encode('utf-8'))
        #    fin.write(response.xpath('' + self.site['link']).extract_first().encode('utf-8'))
        pass

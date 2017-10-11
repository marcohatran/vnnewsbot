import scrapy

class Site(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    keyword = scrapy.Field()
    num_of_xpaths = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()
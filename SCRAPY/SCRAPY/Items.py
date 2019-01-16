import scrapy


class News(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()

import scrapy


class StackOverflowSpider(scrapy.Spider):
    name = 'baiduNews'

    # 利用-a 命令传入参数
    def __init__(self, url=None, *args, **kwargs):
        super(StackOverflowSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['%s' % url]

    def parse(self, response):
        from SCRAPY.SCRAPY.Items import News
        for li in response.xpath('//div[@class="hotnews"]/ul/li'):
            news = News()
            news['title'] = li.xpath('./strong/a/text()').extract()[0]
            news['link'] = li.xpath('./strong/a/@href').extract()[0]
            yield news

    # def parse_news(self, response):
    #     yield {
    #         'title': response.xpath('./strong/a/text()').extract()[0],
    #         'link': response.xpath('./strong/a/@href').extract()[0],
    #     }

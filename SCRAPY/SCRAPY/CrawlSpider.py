import scrapy


class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow'

    # 利用-a 命令传入参数
    def __init__(self, url=None, *args, **kwargs):
        super(StackOverflowSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['%s' % url]

    # 利用自定义命令传入参数 未成功
    # def __init__(self, *args, **kwargs):
    #     super(StackOverflowSpider, self).__init__(*args, **kwargs)
    #     self.start_urls = [self.settings['start_urls']]

    # start_urls = ['http://stackoverflow.com/questions?sort=votes']

    def parse(self, response):
        for href in response.css('.question-summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        yield {
            'title': response.css('h1 a::text').extract()[0],
            'votes': response.css('.question .vote-count-post::text').extract()[0],
            'body': response.css('.question .post-text').extract()[0],
            'tags': response.css('.question .post-tag::text').extract(),
            'link': response.url,
        }

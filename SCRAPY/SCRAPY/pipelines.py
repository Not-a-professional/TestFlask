# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors
import datetime

class ScrapyPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='106.15.185.93',  # 数据库地址
            port=3306,  # 数据库端口
            db='clouddb01',  # 数据库名
            user='root',  # 数据库用户名
            passwd='happyforeversy.',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        if spider.name == 'stackoverflow':
            return item
        elif spider.name == 'baiduNews':
            dtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.cursor.execute("""Insert into news(title, link, date) values (%s, %s, %s)""",
                                (
                                    item['title'],
                                    item['link'],
                                    dtime
                                ))

            self.connect.commit()
            return item
        else:
            return item

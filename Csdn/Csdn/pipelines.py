# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from . import settings

class CsdnPipeline(object):
    def process_item(self, item, spider):
        print("=======================")
        print(item["name"])
        print(item["time"])
        print(item["number"])
        print("=======================")
        return item

class CsdnMysqlPipeline(object):
    def __init__(self):
        user = settings.MYSQL_USER
        host = settings.MYSQL_HOST
        pwd = settings.MYSQL_PWD
        dbName = settings.MYSQL_DB

        self.db = pymysql.connect(user=user,host=host,password=pwd,database=dbName,charset='utf8')
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        insert = 'insert into csdnmatter values(%s,%s,%s);'
        L = [
            item["name"],
            item["time"],
            item["number"]
        ]
        self.cursor.execute(insert,L)

        self.db.commit()
        print('存入数据库成功')
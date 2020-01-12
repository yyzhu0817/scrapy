# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql
from . import settings

class DaomuPipeline(object):
    def process_item(self, item, spider):
        print('='*30)
        print(item["bookName"])
        print(item["bookTitle"])
        print(item["chapter"])
        print(item["count"])
        print(item["link"])
        print('='*30)

class DaomumongoPipeline(object):
    def __init__(self):
        host = settings.MONGODB_HOST
        port = settings.MONGODB_PORT

        #创建数据库连接对象，库对象，集合对象
        conn = pymongo.MongoClient(host=host,port=port)
        db = conn.daomudb
        self.myset = db.daomubiji

    def process_item(self, item, spider):
        # 把item转化为字典
        bookIndo = dict(item)
        self.myset.insert(bookIndo)
        print('存入数据库成功')


class DaomumysqlPipeline(object):
    def __init__(self):
        host = settings.MYSQL_HOST
        user = settings.MYSQL_USER
        pwd = settings.MYSQL_PWD
        dbName = settings.MYSQL_DB
        self.db = pymysql.connect(host=host,user=user,password=pwd,database=dbName,charset='utf8')
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        insert = 'insert into daomubiji values (%s,%s,%s,%s,%s);'
        L = [item["bookName"],
             item["bookTitle"],
             item["chapter"],
             item["count"],
             item["link"]]
        self.cursor.execute(insert,L)
        self.db.commit()

        # self.cursor.close()
        # self.db.close()
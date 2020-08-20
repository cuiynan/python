
# -*- coding: utf-8 -*-

from scrapy.conf import settings
import pymysql
# from openpyxl import Workbook
# import redis

# 数据保存mysql
class MysqlPipeline(object):

    def open_spider(self, spider):
        self.host = settings.get('MYSQL_HOST')
        self.port = settings.get('MYSQL_PORT')
        self.user = settings.get('MYSQL_USER')
        self.password = settings.get('MYSQL_PASSWORD')
        self.db = settings.get(('MYSQL_DB'))
        self.table = settings.get('TABLE')
        self.client = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port, db=self.db, charset='utf8')

    def process_item(self, item, spider):
        item_dict = dict(item)
        cursor = self.client.cursor()
        values = ','.join(['%s'] * len(item_dict))
        keys = ','.join(item_dict.keys())
        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=self.table, keys=keys, values=values)
        try:
            if cursor.execute(sql, tuple(item_dict.values())):  # 第一个值为sql语句第二个为 值 为一个元组
                print('---------------------------------------------------成功---------------------------------------------------')
                self.client.commit()
        except Exception as e:
            print(e)
            print('---------------------------------------------------失败---------------------------------------------------')
            self.client.rollback()
        return item

    def close_spider(self, spider):
        self.client.close()
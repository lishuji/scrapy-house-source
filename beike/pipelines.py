# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.utils.project import get_project_settings

settings = get_project_settings()


class BeikePipeline(object):
    def __init__(self):
        # 链接数据库
        client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        self.db = client[settings['MONGO_DB']]  # 获得数据库的句柄
        self.coll = self.db[settings['MONGO_COLL']]  # 获得collection的句柄
        # 数据库登录需要帐号密码的话
        # self.db.authenticate(settings['MONGO_USER'], settings['MONGO_PSW'])

    def process_item(self, item, spider):
        postItem = dict(item)  # 把item转化成字典形式
        self.coll.insert(postItem)  # 向数据库插入一条记录
        return item  # 会在控制台输出原item数据，可以选择不写

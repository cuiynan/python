
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 企查查企业信息字段
class QichachaItem(scrapy.Item):
    legal_person = scrapy.Field()  # 法人
    telephone = scrapy.Field()  # 电话
    email = scrapy.Field()  # 邮箱
    registration_number = scrapy.Field()  # 工商注册号
    credit_code = scrapy.Field()  # 统一社会信用代码
    registered_capital = scrapy.Field()  # 注册资本
    establishment_data = scrapy.Field()  # 成立日期
    enterprise_type = scrapy.Field()  # 企业类型
    management = scrapy.Field()  # 经营范围
    address = scrapy.Field()  # 公司住所
    term = scrapy.Field()  # 营业期限
    status = scrapy.Field()  # 企业状态
    company_name = scrapy.Field()  # 公司名称
    search_name = scrapy.Field()  # 搜索名称
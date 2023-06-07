# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 租房字段
class AjkItem_zufang(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()  #租房标题
    price = scrapy.Field() #租房价格
    link = scrapy.Field() #详情链接
    city_name = scrapy.Field()  # 城市名的

# 二手房字段
class AjkItem_ershoufang(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()  #二手房标题
    price = scrapy.Field() #二手房价格
    link = scrapy.Field()  # 详情链接
    city_name = scrapy.Field()  # 城市名


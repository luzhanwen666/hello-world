# -*- coding:utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from Ajk.items import AjkItem_ershoufang,AjkItem_zufang
import json
import os



# 保存二手房信息
class AjkPipeline_ershoufang:
    if not os.path.exists('二手房'):
        os.makedirs('二手房')
    def process_item(self, item, spider):
        if isinstance(item, AjkItem_ershoufang):  # 选择要传送的数据建模类
            data = dict(item)
            print("二手房data信息",data)
            # 存入“二手房”文件夹下 以城市名命名json文件
            self.file = open('二手房/{}-二手房信息.json'.format(item['city_name']), 'a')
            json_data = json.dumps(data, ensure_ascii=False) + ',\n'
            self.file.write(json_data)
            self.file.flush()
        return item


# 保存租房信息
class AjkPipeline_zufang:
    if not os.path.exists('租房'):
        os.makedirs('租房')
    def process_item(self, item, spider):
        if isinstance(item, AjkItem_zufang):  # 选择要传送的数据建模类
            data = dict(item)
            print("data信息：",data)
            # 存入“租房”文件夹下 以城市名命名json文件
            self.file = open('租房/{}-租房信息.json'.format(item['city_name']), 'a')
            json_data = json.dumps(data, ensure_ascii=False) + ',\n'
            self.file.write(json_data)
            self.file.flush()
        return item


# -*- coding:utf-8 -*-
import scrapy
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from scrapy import cmdline
from Ajk.items import AjkItem_ershoufang,AjkItem_zufang
import pypinyin  # 将汉字转为拼音
'''
思路：
经分析每个城市的租房和二手房链接的组成都内含城市名对应的拼音
    -- 租房链接含城市名的简拼
         比如北京的租房链接为 https://bj.zu.anjuke.com/fangyuan/p1/
         
    -- 二手房链接含城市名的全拼
            比如北京的二手房链接为 https://beijing.anjuke.com/sale/p1/

所有开发步骤如下：
    1.获取全部城市名字，因全部城市接口我们只需要请求一次，所以单独交给spider.py文件单独爬取
        -- spider.py文件负责抓取城市接口信息，得到所有城市汉字
        -- 将汉字转为全拼和简拼，一并保存进文本文档中
        
    2.实现单个城市的二手房和租房板块的信息爬取
    3.在单个城市基础之上实现不同城市的二手房和租房信息抓取：
        -- 3.1 scrapy框架爬虫只负责不断从"城市拼音信息.txt"文件中不断获取不同城市信息，从而可爬取到对应城市的二手房+租房信息
    
'''

class AjkSpiderSpider(scrapy.Spider):

    name = 'ajk_spider'
    allowed_domains = ['anjuke.com']
    # 二手房链接
    start_urls = 'https://{}.anjuke.com/sale/p{}/'

    # 租房链接
    zufang_urls = 'https://{}.zu.anjuke.com/fangyuan/p{}/'


    def start_requests(self):
        # 1.从本地文件读取出城市名，城市名全拼，城市名简拼
        f = open('城市拼音信息.txt', 'r')
        # 2.以列表形式读取 方便后续提取
        a = f.readlines()
        # print(a)
        # 3. 遍历取值时分别将城市名，城市名全拼，城市名简拼单独取出
        for i in a:
            # 3.1 实例化租房item类 便于后续写入简拼信息
            zufang_item = AjkItem_zufang()
            # 3.2 实例化二手房item类 便于后续写入全拼信息
            ershou_item = AjkItem_ershoufang()
            all_city = i.strip()  # 去掉换行
            name = all_city.split(":")[0] # 取出城市中文名
            pinyin_name = all_city.split(":")[1] # 取出城市全拼
            j_name = all_city.split(":")[2] # 取出城市简拼
            print("城市名为{}，全拼为{},简拼为{}".format(name,pinyin_name,j_name))
            # 3.3 写入到对应的item类中，便于管道文件存储时给不同城市的JSON文件命名
            zufang_item['city_name'] = name
            ershou_item['city_name'] = name

            # 3.4 二手房 举例爬取3页
            for i in range(1, 4):
                # 拼接每个城市的二手房链接 且打包成请求对象给引擎
                ershou_city_url = self.start_urls.format(pinyin_name, i)
                print("当前正在下载{}的二手房的第{}页，完整链接为：{}".format(name, i, ershou_city_url))
                yield scrapy.Request(url=ershou_city_url, method='GET', callback=self.parse,
                                     meta={'item': zufang_item})

            # 3.5 租房翻页 举例爬取3页
            for i in range(1,4):
                # 拼接每个城市的租房链接，且打包成请求对象给引擎
                zufang_city_url = self.zufang_urls.format(j_name,i)
                print("当前正在下载{}的租房的第{}页，完整链接为：{}".format(name,i,zufang_city_url))
                yield scrapy.Request(url=zufang_city_url, method='GET', callback=self.zufang_parse,meta={'item':zufang_item})

    '''
    ！！！该需求代码已单独写入spider.py文件中
    start_urls = ['https://www.anjuke.com/sy-city.html?from=HomePage_City']
    def parse(self, response):
        city_name = response.xpath('//div[@class="ajk-city-cell is-letter"]/ul[@class="ajk-city-cell-content"]/li/a/text()').extract()
        print("所有城市名",city_name)
    '''

    def parse(self, response):
        '''
        解析二手房信息
        :param response:
        :return:
        '''
        ershou_item = response.meta['item']
        title = response.xpath('//div[@class="property-content-title"]/h3/text()').extract()

        price = response.xpath(
            '//div[@class="property-price"]//span[@class="property-price-total-num"]/text()').extract()
        link = response.xpath('//div[@tongji_tag="fcpc_ersflist_gzcount"]/a/@href').extract()
        # print("二手标题", title)
        for titles, prices,links in zip(title, price,link):
            ershou_item['title'] = titles
            ershou_item['price'] = prices
            ershou_item['link'] = links
            print('ershou_item', ershou_item)
            yield ershou_item


    def zufang_parse(self,response):
        '''
        解析租房信息
        :return:
        '''
        zufang_item = response.meta['item']
        title = response.xpath('//div[@class="zu-info"]//h3/a/b[@class="strongbox"]/text()').extract()
        price = response.xpath('//div[@class="zu-side"]//strong/b[@class="strongbox"]/text()').extract()
        link = response.xpath('//div[@class="zu-info"]/h3/a/@href').extract()
        # print("租房标题",title)
        # 遍历之后存入item对象中
        for titles, prices,links in zip(title, price,link):
            # zufang_item = AjkItem_zufang()
            zufang_item['title'] = titles
            zufang_item['price'] = prices
            zufang_item['link'] = links
            print('zufang_item', zufang_item)
            yield zufang_item

if __name__ == '__main__':
    cmdline.execute(['scrapy', 'crawl', 'ajk_spider'])

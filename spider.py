import requests
from lxml import etree
import pypinyin
import pinyin
'''
需要安装的模块命令：
    -- pip install pypinyin
    -- pip install pinyin
    
该spider文件为单机爬虫
1.只负责获取城市信息
2.并将城市信息转为拼音形式存为文本文档
3.存为文本文档后该spider文件已弃用，后续scrapy爬虫只负责从“城市拼音信息.txt”中读取对应数据

'''
def get_data():
    '''
    1、请求城市接口
    2.解析所有城市名字
    :return:
    '''
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en',
        'referer': 'https://anjuke.com/',
        'cookie': 'aQQ_ajkguid=498DA19E-9FD6-D17B-BFD3-CX1202152247; id58=CrIgxGOJp8eRz9VtCJVVAg==; 58tj_uuid=4ebd12a9-e1b2-4062-b4c4-41a7e723d80e; wmda_uuid=37bfdf58aa9d487da264720577a39dc5; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; _ga=GA1.2.1077345957.1669965767; als=0; ajk-appVersion=; sessid=2474855D-6397-4FF1-AEB1-AAE9ABFFFE62; fzq_h=ae302dc4aaf3cb206f5240e243392e9d_1677132979637_ee944e543a3043e4bb23d83f02c33143_1996123441; wmda_session_id_6289197098934=1677132979883-cbbc2b6e-e371-25fe; _gid=GA1.2.282847989.1677132981; twe=2; new_session=1; init_refer=https%253A%252F%252Fcallback.58.com%252F; new_uv=4; xxzl_cid=fb99a2321ec74138a62ed9f0a2b28be6; xxzl_deviceid=rs20Gabj0AFO/MdNFARlbrNg55M69heJMMFIg6PGq3wDpFL4lCDQOAVl0d2JYSqP; ctid=27; obtain_by=2',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    url = 'https://www.anjuke.com/sy-city.html?from=HomePage_City'
    response = requests.get(url,headers= headers)
    html_data = response.text
    xml = etree.HTML(html_data)
    city_name = xml.xpath('//div[@class="ajk-city-cell is-letter"]/ul[@class="ajk-city-cell-content"]/li/a/text()')
    print(city_name)
    return city_name

def save_pingyin(word):
    '''
    1.将城市名字转换为拼音
    :return:
    '''
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i) # 拼接为完整地名
    # print('城市名拼音：',s)
    return s

def save_jianpin(word):
    '''
    1.将城市名字转换为简拼
    :return:
    '''
    j = pinyin.get_initial(word, delimiter="")
    print("城市简拼：",j)
    return j

if __name__ == '__main__':
    f = open('城市拼音信息.txt','a')
    city_name = get_data()
    for name in city_name:
        s = save_pingyin(name)  # 将汉字转为全拼
        j = save_jianpin(name) # 将汉字转为简拼
        print("全拼：{},简拼：{}".format(s,j))
        # 将组建好的拼音数据保存到文本文档 中间拼接冒号是为了便于scrapy中做切割取值处理
        f.write(name+":"+s+":"+j+'\n')
        f.flush()



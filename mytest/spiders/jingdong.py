import scrapy
from scrapy import Request, Selector

from mytest.items import JDItem


class JingdongSpider(scrapy.Spider):
    name = 'jingdong'
    allowed_domains = ["jd.com", "3.cn"]

    def start_requests(self):
        keywords = ['手机', '笔记本 游戏本', '显卡']
        for word in keywords:
            for page in range(1, 3):  # 每个关键字爬取10页数据，每页数据有56条
                url = f'https://search.jd.com/Search?keyword={word}&page={page}&s=56'
                yield Request(url=url)

    def parse(self, response, **kwargs):
        """解析产生一个个的item并且产生新的请求对象"""
        # 提取页面的商品框
        """
        //*[@id="J_goodsList"]/ul/li[2]/div
        //*[@id="J_goodsList"]/ul/li/div/div/a/em/text()[1]
        //*[@id="J_goodsList"]/ul/li[3]/div/div[3]/strong/i
        div/div/strong/a
        //*[@id="J_goodsList"]/ul/li[3]/div/div[7]/span/a
        //*[@id="J_goodsList"]/ul/li[3]/div/div[1]/a/img
        """
        lis = response.xpath('//*[@id="J_goodsList"]/ul/li')
        for li in lis:  # selector是一条商品信息的选择器，selectors是一页商品信息的选择器
            print('运行了。。。。')
            item = JDItem()
            title = li.xpath('div/div/a/em/text()').extract_first("").strip()  # 标题
            price = li.xpath('div/div/strong/i/text()').extract_first("")  # 价格
            comment_num = li.xpath('div/div/strong/a/text()').extract_first("")  # 评论数量
            shop = li.xpath('div/div/span/a/text()').extract_first("")  # 店铺
            img = li.xpath('div/div/a/img/@src').extract_first("")  # 图片链接

            print('******************************:', title)
            print('******************************:', price)
            print('******************************:', comment_num)
            print('******************************:', shop)
            print('******************************:', img)
            item['title'] = title
            item['price'] = price
            item['comment_num'] = comment_num
            item['shop'] = shop
            item['img'] = img
            yield item

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JDItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 商品标题
    price = scrapy.Field()  # 价格
    comment_num = scrapy.Field()  # 评论数量
    img = scrapy.Field()  # 图片链接
    shop = scrapy.Field()  # 店铺名称

    def __str__(self):
        return self.title
